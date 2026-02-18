# Importing libraries
from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Loading values helper functions
extracted_data = load_pdf_files(data = "data/")
minimal_docs = filter_to_minimal_docs(extracted_data)
texts_chunk = text_split(minimal_docs)
embedding = download_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

# creating index in pinecone
index_name = "medical-chatbot"
if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension = 384, # dimension of the embeddings
        metric = "cosine", # cosine similarity
        spec = ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

# loading documents into pinecone index created
docsearch = PineconeVectorStore.from_documents(
    documents = texts_chunk,
    embedding = embedding,
    index_name = index_name
)
