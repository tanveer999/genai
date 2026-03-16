from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1", api_key="lm-studio", temperature=0.6
)

# response = model.invoke("What is the capital of India?")
# print(response.content)

template1 = PromptTemplate(
  template="Write a detailed report on {topic}",
  input_variables=["topic"]
)

template2 = PromptTemplate(
  template="Write a 5 line summary on the following text. \n {text}",
  input_variables=["text"]
)

#########

# prompt1 = template1.invoke({"topic": "climate change"})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({"text": result.content})

# result1 = model.invoke(prompt2)

# print(result1.content)

#########

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "climate change"})

print(result)