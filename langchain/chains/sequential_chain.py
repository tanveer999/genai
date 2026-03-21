from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(model="qwen3.5:2b", base_url="http://localhost:11434")
parser = StrOutputParser()

prompt1 = PromptTemplate(
  template="Generate detailed report about {topic}",
  input_variables=['topic']
)

prompt2 = PromptTemplate(
  template="Summarize the report in 5 points from the following text \n {text}",
  input_variables=['text'],
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "olympics"})

print(result)

chain.get_graph().print_ascii()