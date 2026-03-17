from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOllama(model="qwen3.5:2b", base_url="http://localhost:11434")

class Person(BaseModel):

  name: str = Field(description="The name of the person")
  age: int = Field(gt=18, description="The age of the person, must be greater than 18")
  city: str = Field(description="Name of city the person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
  template = "Generate name,age and city of fictional {place} person \n {format_instruction}",
  input_variables=['place'],
  partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'place': "indian"})

# print(prompt)

# result = model.invoke(prompt)

# result1 = parser.parse(result.content)

# print(result1)

chain = template | model | parser

final_result = chain.invoke({'place': "indian"})
print(final_result)