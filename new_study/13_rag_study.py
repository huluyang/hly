"""
RAG 基础
检索增强生成
工作流程：
    1.离线：文档->分割->向量嵌入->存入向量数据库
    2.在线： 用户查询->检错相关文档->提供给LLM->生成答案

"""

# 1.文档加载
from langchain_community.document_loaders import TextLoader

# 加载文本文件
loader = TextLoader("story.txt", encoding="utf-8")
documents = loader.load()  # 是一个 Document 对象列表
print(documents)  # Document 包含：page_content(文本) 和 metadata(元数据)
"""
常用的Loaders:
    TextLoader - 文本文件
    PyPDFLoader - PDF文件
    WebBaseLoader - 网页
    CSVLoader - CSV文件
"""

# 2.文本分割
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,  # 每块最大字符数
    chunk_overlap=30,  # 块之前的重叠
    separators=["\n\n", "\n", "。"]  # 分割优先级
)

chunk = splitter.split_documents(documents)
print(chunk)
# 3.向量嵌入（Embeddings）

from langchain.embeddings import init_embeddings
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

embeddings = init_embeddings(
    model="text-embedding-v1",
    provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    check_embedding_ctx_length=False  # 如果是百炼平台  必须加这个 不然会报错
)

result = embeddings.embed_query("你好")
print(result)

# 向量数据库
from langchain_community.vectorstores import FAISS

vector = FAISS.from_documents(chunk, embeddings)
# 此时，向量存储到了内存当中

# vector.save_local("faiss_name")  # 将向量存储本地化
# vector = FAISS.load_local("faiss_name", embeddings, allow_dangerous_deserialization=True)  # 读取本地向量数据库文件

# 创建检索器并配置每次召回最相关的3个文档片段
retriever = vector.as_retriever(search_kwargs={"k": 3})
res = retriever.invoke("哆啦 A 梦的道具是什么？")
print(res)

# 4.构建 RAG 链
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

model = init_chat_model(
    model="deepseek-r1",
    model_provider="openai",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# 定义 Prompt 模板
template = """请根据以下上下文信息回答问题。如果上下文中没有相关信息，请说"我不知道"。

上下文：
{context}

问题：{question}

答案："""

prompt = ChatPromptTemplate.from_template(template)


# 将检索到的文档转换为字符串
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


# 构建 RAG 链
rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
)

# 测试问答
answer = rag_chain.invoke("哆啦 A 梦的道具是什么？")
print(answer)
