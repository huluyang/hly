from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

template = ChatPromptTemplate.from_messages([
    ("system", "你是{what}"),
    ("user", "{input}")
])

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
# 使用 | 创建链
chain = template | model

# 直接调用链
res = chain.invoke({
    "what": "Python 导师",
    "input": "什么是字符串类型"
})

print(res.content)
