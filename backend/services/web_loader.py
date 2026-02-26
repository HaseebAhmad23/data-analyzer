from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_url(url: str):
    loader = WebBaseLoader(url)
    docs = loader.load()

    # split only if content is large enough to warrant it
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)
