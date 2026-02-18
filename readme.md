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
- next notebook experiment is done where complete code for pipeline is run on jupyter notebook and executed to check if it is working fine or not. use store_index to store the embeddings in the vector database.
- Next in modular coding, we have created separate files for each component of the pipeline and imported them in the main file.
- then we created html and css files for frontend development.
- created app using flask framework and ran on local host by using app.py file.
- pushed the code to github
- conversation buffer memory (on langchain) also can be added here
- from aws, an iam user "medical-chatbot" is created with ec2 and ecr permissions.
- for the user, under security credentials, created accesskeys (access and secret access key) for cli authentication.
- Elastic container registry (ECR) -> private repository -> medicalbot and saved URI
- EC2 instance -> create in us-east-1 region and name as medical-machine (ubuntu-t2.large)(keyvalue pari-medicalchatbot-RSA)(HTTPS, HTTP, SSH) (30gb storage)
- connect to ec2:
  - update machine (sudo apt-get upgrade -y and sudo apt-get upgrade) 
  - install docker: 
    - curl -fsSL https://get.docker.com -o get-docker.sh
    - sudo sh get-docker.sh
    - sudo usermod -aG docker ubuntu
    - newgrp docker
    - docker --version
- Now setup github actions (CI/CD): go to github repository and settings -> actions -> runners -> new self-hosted runner -> select linux -> run commands mentioned in download and configure one by one in ec2 instance(name of runner: self-hosted). github will be connected to aws and once github has any pushes, aws will automatically deploy the code.
- for authentication, secrets have to be added to github repository: secrets and variables -> actions -> AWS access keys, default region name, ecr repo name, pinecone api key, openai api key
- Create a file for Dockerfile and write commands there
- Create a file for github actions and 


## Other info:
- LLM models can be used in 3 ways:
  - Inference mode: ask prompt and get response (no learning)
  - Fine-Tuning mode: modify the model weights here. train model on new labeled data, adjust internal parameters, specialise it for a domain eg: RL using human feedback, Instruction tuning, LoRA/PEFT , Full fine-tuning (learning)(lots of data, high computational power, cost - disadvantages)
  - RAG: keep model fixed, connect to external data sources (knowledge base), retreive docuemnts, use tools/APIs, inject fresh context (knowledge based using custom data and connect to LLM)
- LLM's have context window which means they can only remember a limited amount of history i., 8192 tokens (tokens are the smallest unit of information)
- what is context window? - working memory of the model
- context window means how much information the model can use to make a decision.


