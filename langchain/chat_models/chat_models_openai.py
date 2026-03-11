from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1", api_key="lm-studio", temperature=0.6
)

response = model.invoke("What is the capital of India?")
print(response.content)