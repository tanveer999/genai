from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
  model="models/gemini-embedding-001",
  output_dimensionality=10
)

response = embedding.embed_query("What is the capital of India?")
print(response)
