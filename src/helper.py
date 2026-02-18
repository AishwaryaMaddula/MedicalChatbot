# Importing libraries
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
import torch

# Load pdf - Extract text from PDF files
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob = "*.pdf", # load only pdf files
        loader_cls = PyPDFLoader
    )
    documents = loader.load()
    return documents

# filtering off additional metadata and just using source, page_content
def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source") # obtain source from metadata
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs

# Splitting the text into chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500, # 500 tokens are considered a chunk
        chunk_overlap = 20
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk

# downloading model from huggingface
def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name = model_name,
        model_kwargs = {"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )
    return embeddings