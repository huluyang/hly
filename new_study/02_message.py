from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
"""
简单介绍
messages = [
    SystemMessage(content="系统提示词"),
    HumanMessage(content="用户消息"),
    AIMessage(content="AI回复")
]

"""

messages = [
    SystemMessage(content="你是一个python专家"),
    HumanMessage(content="什么是字符串类型")
]

res = model.invoke(messages)
print(res)
print(res.content)  # 只提取回答中的文字部分

"""
详细介绍  作为了解
invoke 返回一个AIMessage对象
res.content  # str - AI 的回复文本
res.response_metadata  # dict - AI响应的原数据
res.id  # str - 消息唯一 ID
res.usage_metadata  # dict - Token 使用情况
res.additional_kwargs  # dict - 其他额外信息


"""
