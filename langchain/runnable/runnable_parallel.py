from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_MODEL = "gemma-3-27b-it"
# GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
parser = StrOutputParser()

prompt1 = PromptTemplate(
  template="Generate a Tweet about a {topic}",
  input_variables=['topic']
)

prompt2 = PromptTemplate(
  template="Generate a LinkedIn post about a {topic}",
  input_variables=['topic']
)

parallel_chain = RunnableParallel(
  {
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser)
  }
)

result = parallel_chain.invoke({"topic": "langchain"})

print(result)