"""
核心概念
问题： 对话历史会无限增长 -> 超token、成本高、响应慢
解决： 使用中间件自动管理上下文长度
SummarizationMiddleware
"""

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain.chat_models import init_chat_model
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)
agent = create_agent(
    model=model,
    tools=[],
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model="deepseek-r1",  # 这里的模型可以选择便宜的模型，主要是根据历史信息生产摘要
            trigger=("tokens", 100),  # 超过 100 tokens 触发摘要
            summary_prompt="请总结对话,重点保留：姓名，待办事项"  # 这个参数是自定义摘要 如无特别需求可以不加
        )
    ]
)
"""
工作原理
对话历史：[消息1, 消息2, ..., 消息20] （超过 100 tokens）
    ↓
SummarizationMiddleware 自动触发
    ↓
摘要旧消息："用户是张三，在北京工作，喜欢编程..."
    ↓
新历史：[摘要, 最近消息] （减少到 50 tokens）

参数说明
参数      说明                           示例
model    生成摘要的模型（可用便宜模型）      必须
trigger  触发摘要的条件                  （"tokens", 500）或（"messages", 10）
keep     保留多少最近消息                 （"messages", 3）
注意：max_tokens_before_summary 和 messages_to_keep 参数已废弃，请使用trigger和keep


trim_messages(手动修剪)

from  langchain_core.messages import trim_messages

# 只保留最近N条消息
trimmed = trim_messages(
    messages,
    max_tokens=100,
    strategy="last",  # 保留最后的
    token_counter=len
)
适用场景
1.只需要最近几轮对话
2.不需要保留旧信息
3.简单直接
策略对比
策略                         优点                  缺点                 适用
SummarizationMiddleware    自动化、保留信息         摘要成本              长对话（推荐）
trim_messages              简单、精确              丢失旧信息            只要最近N轮

实际应用
客服机器人
agent = create_agent(
    model=model,
    tools=[查询订单, 查询物流],
    system_prompt="客服助手",
    checkpointer=InMemorySaver(),
    middleware=[
    SummarizationMiddleware(
        model="deepseek-r1",
        trigger=("tokens", 800),  # 超过 800 tokens 触发摘要
        keep=("messages", 5)  # 保留最近5条消息
    )
    ]
)


长期对话助手
agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        SummarizationMiddleware(
            model="deepseek-r1",
            trigger=("tokens", 1000),  # 超过 1000 tokens 触发摘要
            keep=("messages", 3)       # 保留最近 3 条消息
        )
    ],
    checkpointer=InMemorySaver()
)
"""
