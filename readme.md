# Medical chatbot
## About:
help required from doctors, additional assistance system for patients (feedback or suggestions based on patient's requirements)

## RAG Architecture:

- Load documents(Medical document PDF)
- Extract documents of the book
- Chunking the documents
- Embedding Model
- Vector Embeddings
- Pinecone Vector Database(Knowledge Base - Indexing and Similarity Search can be done here) (custom data source)
- LLM Model
- Chatbot

# Tools Used:
- Programming Language: Python
- LLM model: OpenAI GPT
- Orchestration framework: Langchain
- Vector database : Pinecone
- Frontend and Backend development : Flask
- Deployment : AWS -> CI/CD

## Process

- create folder structure in template.sh and run ./template.sh to create project structure as required. if required permissions are not available, run chmod +x template.sh to give additional permissions.
- requirements.txt file contains packages to install. For this project, we have to install in editable format. we wanted our project to work like a python package and so setup.py is required.
- install the requirments using command "pip install -r requirements.txt"
- next notebook experiment is done where complete code for pipeline is run on jupyter notebook and executed to check if it is working fine or not
- Next in modular coding, we have created separate files for each component of the pipeline and imported them in the main file.
- then we created html and css files for frontend development.
- created app using flask framework and ran on local host



## Other info:
- LLM models can be used in 3 ways:
  - Inference mode: ask prompt and get response (no learning)
  - Fine-Tuning mode: modify the model weights here. train model on new labeled data, adjust internal parameters, specialise it for a domain eg: RL using human feedback, Instruction tuning, LoRA/PEFT , Full fine-tuning (learning)(lots of data, high computational power, cost - disadvantages)
  - RAG: keep model fixed, connect to external data sources (knowledge base), retreive docuemnts, use tools/APIs, inject fresh context (knowledge based using custom data and connect to LLM)
- LLM's have context window which means they can only remember a limited amount of history i., 8192 tokens (tokens are the smallest unit of information)
- what is context window? - working memory of the model
- context window means how much information the model can use to make a decision.


