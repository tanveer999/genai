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
    Generate {total_recipes} high-quality recipes for a dish using only these ingredients:
    {ingredients}

    Exclude any recipes containing forbidden ingredients:
    {filter}

    For each recipe, provide:
    1. A clear title.
    2. Exact ingredient list (with quantities).
    3. Step-by-step instructions (no vague phrasing like "mix well").
    4. Optional: Cook time/servings if relevant.

    Format strictly as a numbered list—**only recipes**, no metadata or explanations.
    Example output structure:
    ---
    1. **Pasta Carbonara**
      Ingredients: 200g pasta, 50g pancetta (forbidden), 3 eggs
      Instructions: [Step 1], [Step 2]...

    2. **Chicken Stir-Fry**
      Ingredients: 4 chicken thighs, 1 bell pepper, 2 tbsp soy sauce
      Instructions: [Steps]
    ...
    ---
  """

  recipies = get_completion(prompt)

  print("Shopping List:")
  
  existing_ingredients = input("Enter list of ingredients you already have? ")

  # prompt = f"Produce shopping list for the above recipes. Group the ingredients by recipe. List only ingredients that are not already in my pantry. I have {existing_ingredients} in my pantry. Do not include any other text."
  
  prompt = f"""
    Generate a **grouped shopping list** for the recipes above, excluding:
    1. Ingredients already in your pantry: {existing_ingredients}
    2. Any ingredients from the excluded list: {filter}

    **Format Requirements:**
    - **Group by recipe title** (e.g., "Pasta Carbonara" → all its ingredients).
    - List only **unique items per group** (no duplicates across recipes).
    - Include **quantities/measurements** where needed (e.g., "2 cups flour").
    - Measurements should be in units like grams, liters, etc, not vague terms like "a pinch".
    - Sort alphabetically within each group for consistency.

    **Example Output:**
    ---
    1. **Pasta Carbonara**
    - 1 cup pasta
    - 3 eggs

    2. **Chicken Stir-Fry**
    - 4 chicken thighs
    - 1 bell pepper
    - 2 tbsp soy sauce
    ...
    ---
  """

  new_prompt = f"{recipies} {prompt}"

  get_completion(new_prompt)

if __name__ == "__main__":
  main2()