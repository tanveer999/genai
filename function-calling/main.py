import json
from urllib import response

import tiktoken
from openai import OpenAI

client = OpenAI(
  base_url="http://localhost:1234/v1",
  api_key="lm-studio"
)
MODEL = "mistralai/ministral-3-3b"

def get_completion(prompt,tools):
  stream = client.responses.create(
    model=MODEL,
    input=prompt,
    temperature=0.1,
    max_output_tokens=1000,
    stream=True,
    tools=tools
  )

  full_response = []

  for event in stream:
    event_type = getattr(event, "type", None)

    # Official Responses API text-delta event
    if event_type == "response.output_text.delta":
      delta = getattr(event, "delta", "")
      if delta:
        print(delta, end="", flush=True)
        full_response.append(delta)

    # Fallback for dict-like stream events (some gateways/adapters)
    elif isinstance(event, dict) and event.get("type") == "response.output_text.delta":
      delta = event.get("delta", "")
      if delta:
        print(delta, end="", flush=True)
        full_response.append(delta)

  print()
  return "".join(full_response)

def get_current_weather(location, unit="celsius"):
  return f"The current weather in {location} is 20 degrees {unit}"

def main():
  tools = [
      {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "Country, State , City eg: San Francisco, Texas",
            },
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
          },
          "required": ["location"],
        },
      }
  ]

  input_list = [{"role": "user", "content": "What's the weather like in Boston?"}]

  response = client.responses.create(
    model=MODEL,
    input=input_list,
    tools=tools
  )

  input_list += response.output

  for item in response.output:
    if item.type == "function_call":
      if item.name == "get_current_weather":
        weather = get_current_weather(**json.loads(item.arguments))

        input_list.append({
          "type": "function_call_output",
          "call_id": item.call_id,
          "output": json.dumps({
            "weather": weather
          })
        })

  print("final input:")
  print(input_list)

  response = client.responses.create(
    model=MODEL,
    instructions="Respond with just the weather info provided by the tool",
    input=input_list,
    tools=tools
  )

  print("Final response:")
  print(response.model_dump_json(indent=2))

  print("\n" + response.output_text)



if __name__ == "__main__":
  main()
  

  

  # while True:
  #     prompt = input("Enter a prompt: ")
  #     response = get_completion(prompt)

  #     print("\n----\n")
