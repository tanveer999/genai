from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
# GEMINI_MODEL = "gemma-3-27b-it"
GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
parser = StrOutputParser()

class Feedback(BaseModel):

  sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback either positive or negative")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
  template="Classify the sentiment of the following review as either positive or negative \n {feedback} \n {format_instructions}",
  input_variables=['feedback'],
  partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
  template="Write an appropriate generic response to this positive feedback for the customer \n {feedback}",
  input_variables=['feedback']
)

prompt3 = PromptTemplate(
  template="Write an appropriate generic response to this negative feedback for the customer \n {feedback}",
  input_variables=['feedback']
)

branch_chain = RunnableBranch(
  (lambda x:x.sentiment == "positive", prompt2 | model | parser),
  (lambda x:x.sentiment == "negative", prompt3 | model | parser),
  RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "this is worst product"})

print(result)

