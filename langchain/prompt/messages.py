from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
# model = "gemini-2.5-flash"
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

messages = [
  SystemMessage(content="you are a helpful assistant"),
  HumanMessage(content="What is the capital of India?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content[0].get('text')))

print(messages)