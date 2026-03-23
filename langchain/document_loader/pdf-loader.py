from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_MODEL = "gemma-3-27b-it"
# GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
parser = StrOutputParser()

prompt = PromptTemplate(
  template="write summary for the following poem \n {poem}",
  input_variables=["poem"]
)

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

print(len(docs))
