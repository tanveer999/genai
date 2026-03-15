from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# GEMINI_MODEL = "gemini-3-flash-preview"
# GEMINI_MODEL = "gemini-3-27b-it"
GEMINI_MODEL = "gemini-2.5-flash"

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)

class Review(BaseModel):

  key_themes: list[str] = Field(description="The main themes or topics discussed in the review")
  summary: str = Field(description="A brief summary of the review")
  sentiment: Literal['pos', 'neg', 'neu'] = Field(description="The overall sentiment of the review (positive, negative, neutral)")
  pros: Optional[list[str]] = Field(default=None, description="List all the pros inside a list")
  cons: Optional[list[str]] = Field(default=None, description="List all the cons inside a list")
  username: Optional[str] = Field(default=None, description="The username of the reviewer")

structured_model = model.with_structured_output(Review)

user_review = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
bulky and not good for one hand use
Bloatware i one ui
expensive


"""
#Review by Luffy

result = structured_model.invoke(user_review)
print(result)