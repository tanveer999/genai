from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()
# model = "gemini-3-flash-preview"
# model = "gemini-2.5-flash"
model = "gemma-3-27b-it"

def count_tokens(contents: str) -> int:
  total_tokens = client.models.count_tokens(
      model=model,
      contents=contents
  )
  return total_tokens

def genrate_text(contents: str) -> str:

  response = client.models.generate_content(
      model=model,
      contents=contents
  )
  return response

def generate_text_with_streaming_response(contents: str) -> str:

  response = client.models.generate_content_stream(
    model=model,
    contents=contents
  )

  for chunk in response:
    print(chunk.text, end="", flush=True)
  print()

def multi_turn_conversation(contents: str) -> str:
  chat = client.chats.create(model=model)

  response = chat.send_message("I have 2 dogs in my house")
  print(response.text)

  response = chat.send_message("How many paws are there in total?")
  print(response.text)

  for message in chat.get_history():
    print(f"role - {message.role}", end=": ")
    print(message.parts[0].text)

def multi_trun_conversation_with_streaming_response(contents: str) -> str:
  chat = client.chats.create(model=model)

  response = chat.send_message_stream("I have 2 dogs in my house")
  for chunk in response:
    print(chunk.text, end="", flush=True)
  print()

  response = chat.send_message_stream("How many paws are there in total?")
  for chunk in response:
    print(chunk.text, end="", flush=True)
  print()

  for message in chat.get_history():
    print(f"role - {message.role}", end=": ")
    print(message.parts[0].text)

def main():
  contents = input("Enter the query: ")
  
  token_count = count_tokens(contents)
  print(f"Token count: {token_count}")

  response = genrate_text(contents)
  print(f"Generated text: {response.text}")
  print("Response metadata: ", response.usage_metadata)

def main2():

  contents = """
  role: system, content: you are a sarcastic assistant. You will answer the user's question in a sarcastic way.
  role: user, content: What is the capital of France?
  role: assistant, content: Oh, I don't know, maybe it's Paris? Just a wild guess!
  role: user, content: What is the capital of Germany?
  """

  response = genrate_text(contents)
  print(f"Generated text: {response.text}")

def main3():
  
  contents = """
  role: system, content: you are a sarcastic assistant. You will answer the user's question in a sarcastic way.
  role: user, content: What is the capital of France?
  role: assistant, content: Oh, I don't know, maybe it's Paris? Just a wild guess!
  role: user, content: What is the capital of Germany?
  """

  while True:
    generate_text_with_streaming_response(contents)

    prompt = input("Prompt: ")
    contents = f"role: user, content: {prompt}"

def main4():
  multi_turn_conversation("")

def main5():
  multi_trun_conversation_with_streaming_response("")

def main6():
  while True:

    prompt = input("Prompt: ")
    generate_text_with_streaming_response(prompt)
    

if __name__ == "__main__":
  main6()