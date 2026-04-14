from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from langchain.chat_models import init_chat_model

# 模型初始化
model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# 向模型发送消息
res = model.invoke("你好呀")
# 获取大模型的回答
print(res)
