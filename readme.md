# Medical chatbot
## About:
help required from doctors, additional assistance system for patients (feedback or suggestions based on patient's requirements)

## Architecture:


# Tools Used:
- Orchestration framework: Langchain
- Vector database : pinecone
- Frontend development : Flask
- Deployment : AWS

## Uses:

- LLM models can be used in 3 ways:
  - Inference mode: ask prompt and get response (no learning)
  - Fine-Tuning mode: modify the model weights here. train model on new labeled data, adjust internal parameters, specialise it for a domain eg: RL using human feedback, Instruction tuning, LoRA/PEFT , Full fine-tuning (learning)(lots of data, high computational power, cost - disadvantages)
  - RAG: keep model fixed, connect to external data sources (knowledge base), retreive docuemnts, use tools/APIs, inject fresh context (knowledge based using custom data and connect to LLM)