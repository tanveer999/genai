from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch ,RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_MODEL = "gemma-3-27b-it"
# GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
parser = StrOutputParser()


prompt1 = PromptTemplate(
  template="write a detailed report on {topic}",
  input_variables=["topic"]
)

prompt2 = PromptTemplate(
  template="Summarize the following text \n {text}",
  input_variables=["text"]
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
  (lambda x: len(x.split()) > 3000, RunnableSequence(prompt2, model, parser)),
  RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "langchain"})

print(result)