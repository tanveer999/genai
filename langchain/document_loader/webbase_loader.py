from langchain_community.document_loaders import WebBaseLoader
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
  template="Answer the following question \n {question} from the following {text}",
  input_variables=["question", "text"]
)

url = "https://www.amazon.in/LG-P7020NGAZ-Fully-Automatic-Washing-Machine/dp/B09DD573SY/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.TjdhOiPP7u3yM2KPu-P1vglxYQ0O-_RimQBIZnSRaeRf4nZ226IDI0J697lc90jLPMYdud0Uj5yXefJWz6GVjWUFfAB7eFqszGCgpcavDVm0xtpOYw8hOussKHy-y0UhGyEK6Ld4i2B8M51xooLLEBgiKQJAqCSvpgGzV_m_jDq1Do4udiK7myYmvR1WDNHVsIdeJojKu0ZX6BkE4jIVFiFsTy8LmjmmLrksIVRMADFyOxLh3m4wHsMpNZnZ4ga6tA6WPUDaC-fM7Zp7Li6aFiurzZp6ruZWNZ2a7wCt5Ng.DptizpzrvvYEJkhYA7NidTmYhVPz9RdwRNClaxsw3ZI&dib_tag=se&pd_rd_r=142cbc73-c61b-40e7-93b2-6c91928c1928&pd_rd_w=kQCUG&pd_rd_wg=yTnJj&qid=1774285051&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
  "question": "what is this product",
  "text": docs[0].page_content
})

print(result)