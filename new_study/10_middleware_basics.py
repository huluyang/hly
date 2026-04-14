"""Middleware Basics(中间件基础)
核心概念  Agent执行过程中的钩子函数
"""

from langchain.agents.middleware import AgentMiddleware
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent


class MyMiddleware(AgentMiddleware):
    def before_model(self, state, runtime):
        """模型调用前执行"""
        print("准备调用模型")
        return None

    def after_agent(self, state, runtime):
        """模型响应后执行"""
        print("模型已响应")
        return None


model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[MyMiddleware()]
)

"""执行顺序
agent = create_agent(
    model=model,
    middleware=[Middleware1(), Middleware2(), Middleware3()]
)
1. Middleware1.before_model   ↓ 正序
2. Middleware2.before_model   ↓
3. Middleware3.before_model   ↓

   [模型调用]

6. Middleware3.after_model    ↑ 逆序
5. Middleware2.after_model    ↑
4. Middleware1.after_model    ↑


实际应用
1.日志中间件
class LoggingMiddleware(AgentMiddleware):
    def before_model(self, state, runtime):
        print(f"[日志] 消息数: {len(state.get('messages', []))}")
        return None

    def after_model(self, state, runtime):
        last_msg = state.get('messages', [])[-1]
        print(f"[日志] 响应类型: {last_msg.__class__.__name__}")
        return None
2.计数中间件
class CallCounterMiddleware(AgentMiddleware):
    def after_model(self, state, runtime):
        count = state.get("model_call_count", 0)
        return {"model_call_count": count + 1}

# 需要 checkpointer 来保存自定义状态
agent = create_agent(
    model=model,
    middleware=[CallCounterMiddleware()],
    checkpointer=InMemorySaver()
)
3.消息修剪中间件
class MessageTrimmerMiddleware(AgentMiddleware):
    def __init__(self, max_messages=5):
        super().__init__()
        self.max_messages = max_messages

    def before_model(self, state, runtime):
        messages = state.get('messages', [])
        if len(messages) > self.max_messages:
            # 只保留最近的 N 条消息
            return {"messages": messages[-self.max_messages:]}
        return None
4.输出验证中间件
class OutputValidationMiddleware(AgentMiddleware):
    def after_model(self, state, runtime):
        last_msg = state.get('messages', [])[-1]
        content = getattr(last_msg, 'content', '')

        if len(content) > 1000:
            print("[警告] 响应过长")

        return None
5.限流中间件
class MaxCallsMiddleware(AgentMiddleware):
    def __init__(self, max_calls=10):
        super().__init__()
        self.max_calls = max_calls

    def before_model(self, state, runtime):
        count = state.get("call_count", 0)
        if count >= self.max_calls:
            return {"jump_to": "__end__"}  # 达到限制，直接结束
        return None

    def after_model(self, state, runtime):
        count = state.get("call_count", 0)
        return {"call_count": count + 1}
内置中间件
SummarizationMiddleware(自动摘要)
from langchain.agents.middleware import SummarizationMiddleware

agent = create_agent(
    model=model,
    middleware=[
        SummarizationMiddleware(
            model="deepseek-r1",  # 可用便宜模型
            trigger=500  # 超过500 token触发总结摘要
            )
    ],
    checkpointer=InMemorySaver()
)
作用：
1.消息超过token限制时自动摘要
2.保留最近消息 + 旧消息摘要

HumanInTheLoopMiddleware(人工审核)
from langchain.agents.middleware import HumanInTheLoopMiddleware

agent = create_agent(
    model=model,
    tools=[send_email],
    middleware=[
        HumanInTheLoopMiddleWare(
            interrupt_on={"send_email": True}  # 调用此工具前暂停
        )
    ]
)

PIIMiddleware(敏感信息处理)
from langchain.agents.middleware import PIIMiddleware

agent = create_agent(
    model=model,
    middleware=[
        PIIMiddleware("email", strategy="redact"),  # 邮箱脱敏
        PIIMiddleware("phone_number", strategy="block")  # 电话拦截
    ]
)


最佳实践
# 1. 生产环境推荐配置
agent = create_agent(
    model=model,
    tools=[...],
    middleware=[
        MessageTrimmerMiddleware(max_messages=20),  # 限制消息数
        SummarizationMiddleware(model=..., max_tokens=2000), # 自动摘要
        LoggingMiddleware(),  # 日志记录
    ],
    checkpointer=SqliteSaver.from_conn_string("...")
)

# 2. 开发环境
agent = create_agent(
    model=model,
    tools=[...],
    middleware=[
        LoggingMiddleware(),  # 只要日志
    ]
)

# 3. 测试环境
agent = create_agent(
    model=model,
    tools=[...],
    middleware=[
        MaxCallsMiddleware(max_calls=5),  # 防止测试费用爆炸
    ]
)
"""
