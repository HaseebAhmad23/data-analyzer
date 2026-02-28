from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_community.chat_models import ChatOllama
# from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS


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
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # For gemeni
    # llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    # For ollama free model
    # llm = ChatOllama(model="mistral",temperature=0.3, num_predict=300)
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
