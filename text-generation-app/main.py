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

def main1():
  prompt ="Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"

  response = get_completion(prompt)
  print(response)

def main2():
  total_recipes = input("How many recipes do you want to see? ")
  ingredients = input("Enter list of ingredients? ")
  filter = input("List of ingredients to exclude? ")

  # prompt = f"Show me {total_recipes} recipe for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used. Do not include any recipes that use ingredients from this list: {filter}. Just return the recipes, do not include any other text."

  prompt = f"""
    You are a recipe generator.

    Task:
    Generate exactly {total_recipes} recipe(s), no more, no less.

    Allowed ingredients:
    {ingredients}

    Forbidden ingredients (must never appear):
    {filter}

    Output rules (strict):
    - Return only a numbered list of recipes.
    - Start each recipe with: "<number>. <title>"
    - Include exactly these sections per recipe:
      Ingredients:
      - <quantity> <ingredient>
      Instructions:
      1) <specific action>
      2) <specific action>
    - No intro text, no summary, no notes, no markdown emphasis.
    - Do not output recipe number or anything after recipe {total_recipes}.
  """

  recipies = get_completion(prompt)

  print("Shopping List:")
  
  existing_ingredients = input("Enter list of ingredients you already have? ")

  # prompt = f"Produce shopping list for the above recipes. Group the ingredients by recipe. List only ingredients that are not already in my pantry. I have {existing_ingredients} in my pantry. Do not include any other text."
  
  prompt = f"""
    You are given generated recipes and must produce a shopping list.

    Task:
    Create a grouped shopping list from the recipes above.

    Exclusions (strict):
    - Do NOT include ingredients already in pantry: {existing_ingredients}
    - Do NOT include forbidden ingredients: {filter}

    Output format (strict):
    - Return only a numbered list of recipe groups.
    - Group heading format: "<number>. <recipe title>"
    - Under each group, list ingredients as:
      - <quantity> <ingredient>
    - Sort ingredient lines alphabetically within each recipe group.
    - Keep only one line per ingredient per group (no duplicates).
    - Use concrete units (g, kg, ml, l, tsp, tbsp, cups, pieces). No vague terms.
    - No markdown bold/italics, no intro text, no notes, no explanations.

    Validation rules:
    - If a recipe has no remaining ingredients after exclusions, write:
      - None
    - Never include any pantry or forbidden ingredient.
"""

  new_prompt = f"{recipies} {prompt}"

  get_completion(new_prompt)

if __name__ == "__main__":
  main2()