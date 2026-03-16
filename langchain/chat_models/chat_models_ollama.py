from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model="qwen3.5:2b", base_url="http://localhost:11434")

response = model.invoke("What is the capital of India?")
print(response.content)