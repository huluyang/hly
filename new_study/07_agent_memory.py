"""内存基础"""
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
# 1.创建 Agent 时添加 checkpointer
agent = create_agent(
    model=model,
    tools=[],
    checkpointer=InMemorySaver()  # 添加内存
)

# 2. 调用时指定 thread_id
config = {"configurable": {"thread_id": "id_1"}}

# 第一轮
agent.invoke(
    {"messages": [{"role": "user", "content": "我叫小明"}]},
    config=config
)

res = agent.invoke(
    {"messages": [{"role": "user", "content": "我叫什么？"}]},
    config=config
)
print(res["messages"][-1].content)

"""
备注:InMemorySaver 为短期内存（进程结束就丢失)
thread_id 是区分不同会话的标识 比如聊天应用、多轮任务
checkpointer 自动处理1.读取之前的历史 2.追加新消息 3.调用模型（传入完整历史） 4.保存新历史
在存在 tool工具调用的情况下 Agent同样会记住工具调用的结果 不会重复调用工具
"""

"""
实际应用场景
1.聊天机器人
def handle_user_message(user_id: str, message: str):
    config = {"configurable": {"thread_id": f"user_{user_id}"}}
    res = agent.invoke(
    {"messages": [{"role":"user", "content": message}]},
    config
    )
    return res["messages"][-1].content

2.多轮任务助手
def process_task(task_id: str, user_input: str):
    config = {"configurable": {"thread_id": f"task_{task_id}"}}
    response = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]},
    config
    )
    return response['messages'][-1].content
    
    
3.客服系统
agent = create_agent(
    model=model,
    tool=[查询订单, 查询物流],
    system_prompt="你是客服助手， 记住用户的订单号",
    checkpointer=InMemorySaver()
)
def customer_service(session_id: str, message: str):
    config = {"configurable": {"thread_id": session_id}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config
    )
    return response['messages'][-1].content
核心要点
1.默认无内存：每次invoke是全新开始
2.添加内存：checkpointer=InMemorySaver()
3.会话管理：config={"configurable": {"thread_id": "xxx"}}
4.自动保存：checkpointer自动管理历史
5.多会话: 不同thread_id=不同会话
6.记住工具：也会记住工具调用结果
限制
1.进程重启后丢失
2.无限增长（需要管理上下文）
3.不支持跨进程共享
"""
