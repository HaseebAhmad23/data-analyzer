from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_community.chat_models import ChatOllama
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def create_rag_chain(docs):
    # For openai
    embeddings = OpenAIEmbeddings()

    # For gemeni
    # embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    # embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    # embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")

    # For Ollama free model
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vector_store = FAISS.from_documents(docs, embeddings)

    # For openai
    # llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # For gemeni
    # llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    # For ollama free model
    # llm = ChatOllama(model="mistral",temperature=0.3, num_predict=300)
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:

{context}

Question: {question}

If the answer is not in the context, say "I don't have enough information to answer that."
""")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
