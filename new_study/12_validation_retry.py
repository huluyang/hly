"""
Validation & Retry (验证和重试)
确保 LLM应用的可靠性和数据质量
在生产环境中，需要处理三类问题
1.网络错误-临时性连接问题（用with_retry）
2.模型故障-主模型不可用（用with_fallbacks）
3.输出质量-LLM输出不符合要求（用验证+重试循环）
"""

# with_retry - 自动重试
from langchain.chat_models import init_chat_model
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# 添加重试机制

llm_with_retry = model.with_retry(
    retry_if_exception_type=(ConnectionError, TimeoutError),
    wait_exponential_jitter=True,  # 指数退避 + 随机抖动
    stop_after_attempt=3  # 做多重试3次
)
"""
wait_exponential_jitter  参数的作用
第1次失败 → 等待 1秒 + 随机值
第2次失败 → 等待 2秒 + 随机值  
第3次失败 → 等待 4秒 + 随机值
"""
res = llm_with_retry.invoke("你好")

# with_fallbacks() - 降级方案
# 主模型
primary_model = init_chat_model(...)

# 备用模型
fallback_model = init_chat_model(...)

# 配置降级
llm_with_fallbacks = primary_model.with_fallbacks([fallback_model])

res = llm_with_fallbacks.invoke("你好")
# 主模型正常 使用主模型 主模型失败 自动切换到备用模型


# Ptdantic 验证

from pydantic import BaseModel, Field, field_validator, ValidationError


class User(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=0, le=150)  # 0-150 岁
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('邮箱必须包含 @')
        return v


# 使用
try:
    user = User(name="张三", age=200, email="aaaa")  # 失败案例
except ValidationError as e:
    print(e.errors())  # 查看错误详情
"""
!!!重要：调用顺序必须是
1.with_structured_output() - 先创建结构化输出
2.with_retry() - 再添加重试
3.with_fallbacks() - 最后添加降级
# 1. 先创建结构化输出（必须先调用！）
structured_primary = model.with_structured_output(Product)

# 2. 备用模型（也要先创建结构化输出）
fallback_model = init_chat_model("groq:llama-3.1-8b-instant")
structured_fallback = fallback_model.with_structured_output(Product)

# 3. 添加重试（在结构化输出之后）
primary_with_retry = structured_primary.with_retry(
    retry_if_exception_type=(ConnectionError, TimeoutError),
    stop_after_attempt=2
)

# 4. 添加降级（最后一步）
robust_llm = primary_with_retry.with_fallbacks([structured_fallback])

# 使用
result = robust_llm.invoke("提取产品信息...")
# → 输出自动验证（Pydantic）
# → 网络错误会重试
# → 主模型失败会降级

structured_output → retry → fallbacks
（从内到外包装）
"""
