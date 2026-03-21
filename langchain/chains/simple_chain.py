from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(model="qwen3.5:2b", base_url="http://localhost:11434")

prompt = PromptTemplate(
  template="Generate 5 interesting facts about {topic}",
  input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "olympics"})

print(result)

# chain.get_graph().print_ascii()