from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "你好 {user_name}, 我来帮你学习 {what}"
)
prompt = template.format(user_name="小明", what="python")
print(prompt)

# 部分变量填充
template = PromptTemplate.from_template(
    "你好 {user_name}, 我来帮你学习 {what}"
)
partial_template = template.partial(user_name="小明")
prompt = partial_template.format(what="python")
print(prompt)

# invoke() - 返回 PromptValue
template = PromptTemplate.from_template("你好{name}")
# 返回 PromptValue
prompt_value = template.invoke({"name": "张三"})
# 获取文本
print(prompt_value.text)

# 聊天消息模板
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}"),
    ("user", "{question}")
])

messages = template.format_messages(role="Python 导师", question="什么是字符串类型")
print(messages)

# 返回 ChatPromptValue 对象
prompt_value = template.invoke({
    "role": "Python 导师",
    "question": "什么是字符串类型"
})
print(prompt_value)

messages = prompt_value.to_messages()
print(messages)
