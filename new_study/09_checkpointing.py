"""Checkpointing(持久化)
将对话状态持久化到数据库
提示：如果导入不了则运行下方命令下载安装第三方库
pip install langgraph-checkpoint-sqlite
"""
from langgraph.checkpoint.sqlite import SqliteSaver
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
# 创建持久化 checkpointer(使用 with 语句)
with SqliteSaver.from_conn_string("sqlite_name") as checkpointer:
    agent = create_agent(
        model=model,
        tools=[],
        checkpointer=checkpointer  # 使用SQLite
    )
    config = {"configurable": {"thread_id": "user_1"}}

    # 第一次运行
    res = agent.invoke({"messages": [{"role": "user", "content": "我想学英语你可以教我吗"}]}, config)
    print(res)

# 程序重启后，对话仍然保留  注：上面运行第一次后可先注释掉 然后单独运行现在的代码查看效果
with SqliteSaver.from_conn_string("sqlite_name") as checkpointer:
    agent = create_agent(model=model, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "user_1"}}
    res = agent.invoke({"messages": [{"role": "user", "content": "我上次说我想学习什么来着"}]}, config)
    print(res)
