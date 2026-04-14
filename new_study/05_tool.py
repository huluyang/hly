from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL


@tool
def get_weather(city: str) -> str:
    """
    获取指定城市的天气信息

    参数：
        city: 城市名称，如"北京", "上海"
    返回：
        天气信息字符串
    """
    return f"{city}晴天, 温度 15°C"


# 测试工具函数
print(get_weather.invoke("北京"))

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
# 绑定到模型
model_with_tools = model.bind_tools([get_weather])
# AI可以决定是否调用工具
res = model_with_tools.invoke("北京天气如何")

# 检查AI是否调用工具
if res.tool_calls:
    print("AI 想调用工具")
else:
    print("AI 直接回答")
