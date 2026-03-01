from urllib import response

import tiktoken
from openai import OpenAI

client = OpenAI(
  base_url="http://localhost:1234/v1",
  api_key="lm-studio"
)
MODEL = "mistralai/ministral-3-3b"

def get_completion(prompt):
  messages = [{"role": "user", "content": prompt}]

  response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=0.1,
    max_tokens=1000,
    stream=True
  )

  full_response = []
  for chunk in response:
    delta = chunk.choices[0].delta.content
    if delta:
      print(delta, end="", flush=True)
      full_response.append(delta)

  print()
  return "".join(full_response)

def main2():

  while True:
    task = input("What linux task do you want to accomplish? ")

    prompt = f"""
      You are a Linux CLI expert.

      User task:
      {task}

      Goal:
      Return a useful Linux command only if the task is valid and actionable.

      Output format (strict):
      If task is valid:
      COMMAND: <single executable command; pipelines allowed>
      OPTIONS: <semicolon-separated entries in this exact form: command: option = brief meaning>
      EXPLANATION: <1 short sentence>

      If task is invalid, nonsense, or not actionable:
      NEEDS_CLARIFICATION: <1 short sentence asking user to restate clearly>

      Rules:
      - Return either the 3-line valid format OR the 1-line NEEDS_CLARIFICATION format.
      - No markdown, no code fences, no bullet points.
      - If COMMAND contains multiple commands (e.g., pipes), include options for EACH command segment.
      - Split combined short flags (e.g., -rh => -r and -h) and explain both.
      - Include long options with assigned values (e.g., --max-depth=1) including what the value means.
      - If a command has no options, include: command: none
      - Prefer safe, non-destructive commands.
      - If destructive action is required, prefer safer flags when possible (e.g., -i, --dry-run).
    """
    
    get_completion(prompt)
    print("\n---\n")

if __name__ == "__main__":
  main2()