from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_MODEL = "gemma-3-27b-it"
# GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)
parser = StrOutputParser()

prompt = PromptTemplate(
  template="write a joke about {topic}",
  input_variables=["topic"]
)

prompt2 = PromptTemplate(
  template="explain the following joke - {text}",
  input_variables=["text"]
)

joke_gen_chain = RunnableSequence(prompt, model, parser)
parallel_chain = RunnableParallel({
  "joke": RunnablePassthrough(),
  "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "langchain"})

print(result)