from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
# GEMINI_MODEL = "gemini-3-27b-it"
GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)

chat_history = [
  SystemMessage(content="you are a helpful assistant")
]

while True:
  user_input = input("you: ")
  chat_history.append(HumanMessage(content=user_input))
  
  if user_input.lower() == "exit":
    print("Exiting the chatbot. Goodbye!")
    break

  result = model.invoke(chat_history)
  chat_history.append(AIMessage(content=result.content))

  print("bot:", result.content)

print(chat_history)