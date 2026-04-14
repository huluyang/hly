"""
Structured Output(结构化输出)
核心概念  将LLM的自然语言输出转为结构化python对象
"""

from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from env_utils import DEEPSEEK_BASE_URL, DEEPSEEK_API_KEY


class Person(BaseModel):
    """人物信息"""
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")
    occupation: str = Field(description="职业")


model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# 创建结构化输出的LLM
structured_llm = model.with_structured_output(Person)

# 调用
result = structured_llm.invoke("张三是一名30岁的软件工程师")

# result 是 Person 实例
print(result.name)  # "张三"
print(result.age)  # 30
print(result.occupation)  # "软件工程师"

"""
了解 枚举类型
from enum import Enum

class Priority(str, Enum):
    LOW = "低"
    MEDIUM = "中"
    HIGH = "高"

class Task(BaseModel):
    title: str
    priority: Priority  # 只能是 LOW/MEDIUM/HIGH
"""

# 列表提取
from typing import List


class Person(BaseModel):
    name: str
    age: int


class PeopleList(BaseModel):
    people: List[Person]  # 多个 Person 对象


structured_llm = model.with_structured_output(PeopleList)
result = structured_llm.invoke("张三 30岁， 李四 25岁")

print(result.people)  # [Person(name='张三', age=30), Person(name='李四', age=25)]


# 嵌套模型

class Address(BaseModel):
    city: str
    district: str


class Company(BaseModel):
    name: str
    address: Address  # 嵌套模型


structured_llm = model.with_structured_output(Company)
result = structured_llm.invoke("阿里巴巴在杭州滨江区")
# result.address.city = "杭州"
# result.address.district = "滨江区"
"""
实际应用
1.客户信息提取
2.产品评论分析
"""


# 2.产品评论分析
class Review(BaseModel):
    product: str
    rating: int = Field(description="评分 1-5")
    pros: List[str] = Field(description="优点列表")
    cons: List[str] = Field(description="缺点列表")


structured_llm = model.with_structured_output(Review)

review = structured_llm.invoke("""
iPhone 15 很棒！摄像头强大，手感好。但是价格贵，没有充电器。4分。
""")
print(review)
# review.product = "iPhone 15"
# review.rating = 4
# review.pros = ["摄像头强大", "手感好"]
# review.cons = ["价格贵", "没有充电器"]
