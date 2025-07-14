import sys
sys.path.append('../')
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from config import OPENAI_API_KEY
from config import DATA_DIR
from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import CharacterTextSplitter
import os


embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def get_vector_store(docs):
    # store_path = os.path.join(r"G:\tiger-mvp\data\docs", "faiss_index")

    # if os.path.exists(store_path):
    #     store = FAISS.load_local(store_path, embedding_model)
    # else:
    #     store = FAISS.from_documents(docs, embedding_model)
    #     store.save_local(store_path)
    # return store
    return FAISS.from_documents(docs, embedding_model)

# def load_company_docs(doc_folder="./data/docs"):
#     all_docs = []
#     splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     for filename in os.listdir(doc_folder):
#         full_path = os.path.join(doc_folder, filename)
#         if filename.endswith(".txt"):
#             loader = TextLoader(full_path)
#         elif filename.endswith(".pdf"):
#             loader = PyPDFLoader(full_path)
#         elif filename.endswith(".docx"):
#             loader = UnstructuredWordDocumentLoader(full_path)
#         else:
#             continue
#         docs = loader.load()
#         for doc in docs:
#             doc.metadata["source"] = filename
#         split_docs = splitter.split_documents(docs)
#         all_docs.extend(split_docs)

#     return get_vector_store(all_docs)

def load_company_docs(doc_folder=DATA_DIR):

    all_docs = []
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    for filename in os.listdir(doc_folder):
        full_path = os.path.join(doc_folder, filename)
        if filename.endswith(".txt"):
            loader = TextLoader(full_path)
        elif filename.endswith(".pdf"):
            loader = PyPDFLoader(full_path)
        elif filename.endswith(".docx"):
            loader = UnstructuredWordDocumentLoader(full_path)
        else:
            continue

        docs = loader.load()
        for doc in docs:
            doc.metadata["source"] = filename

        split_docs = splitter.split_documents(docs)
        all_docs.extend(split_docs)

    return get_vector_store(all_docs)
