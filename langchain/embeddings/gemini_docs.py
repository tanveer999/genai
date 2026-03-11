from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
  model="models/gemini-embedding-001",
  output_dimensionality=5
)

documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]

response = embedding.embed_documents(documents)
print(response)

