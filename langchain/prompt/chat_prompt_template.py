from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
  ('system', 'You are a helpful {domain} expert'),
  ('human', 'Explain the concept of {topic} in simple terms.')
])

prompt = chat_template.invoke({'domain': 'linux', 'topic': 'thread'})

print(prompt)