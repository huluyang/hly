"""
Agent = 模型 + 工具 + 自动决策
Agent的关键能力：
    理解用户问题
    自动判断是否需要工具
    选择合适的工具
    基于工具结果生成回答
"""
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

"""
@tool
def one_tool():
    pass


@tool
def tow_tool():
    pass


model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

agent = create_agent(
    model=model,
    tools=[one_tool, tow_tool],
    system_prompt="系统提示词"  # 可选参数   比如：你是天气助手 工作流程：1.提取用户的城市 2.使用get_weather工具获取天气结果 3.简洁清晰地回答 输出格式：-天气状况 -注意事项
)

res = agent.invoke({
    "messages": [{"role": "user", "content": "问题"}]
})"""


# --- 完整示例 ---
@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""  # AI读这个描述
    return f"{city}的天气晴"


@tool
def calculator(a: int, b: int) -> str:
    """执行加法运算"""  # AI读这个描述
    c = str(a + b)
    return c


model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
agent = create_agent(
    model=model,
    tools=[get_weather, calculator]
)

res = agent.invoke({
    "messages": [{"role": "user", "content": "1+10等于几"}]
})
print(res)
print(res["messages"][-1].content)

from langchain.messages import HumanMessage

# 带历史
res2 = agent.invoke({
    "messages": res["messages"] + [HumanMessage(content="上海的天气怎么样")]
})
print(res2)
print(res2['messages'][-1].content)  # 这个是获取最后一次回答的文本

# invoke() 一次性返回完成结果
# stream() 实时流式获取结果

for chunk, metadata in agent.stream({"messages": [HumanMessage(content="上海的天气怎么样")]}, stream_mode="messages"):
    print(chunk, metadata)
    if metadata.get("langgraph_node") == "model":
        if hasattr(chunk, "content") and chunk.content:
            print(chunk.content, end="", flush=True)
