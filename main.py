import os
from dotenv import load_dotenv
from google import genai

# Load the API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

def get_completion(prompt,temperature=0.2,max_tokens=200):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        },
    )
    return response.text



context = """
The student's name is Alex.
Alex is learning Python and Generative AI.
Alex has completed a lesson on prompt engineering.
"""

prompt = f"""
Use the information below to answer the question.

Context:
```{context}```

Question: What is Alex learning, and which lesson has Alex completed?
"""

print(get_completion(prompt, max_tokens=300))