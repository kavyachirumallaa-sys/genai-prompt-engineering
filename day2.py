
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)


# Function with adjustable model parameters
def get_completion(prompt, temperature=0.2, max_tokens=200):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        },
    )
    return response.text


# Task 1: Experiment with temperature
prompt = "Write a creative two-line description of rain."

print("TASK 1: LOW TEMPERATURE")
print(get_completion(prompt, temperature=0.1))

print("\nTASK 1: HIGH TEMPERATURE")
print(get_completion(prompt, temperature=1.5))


# Task 2: Experiment with output token limits
prompt = """
Explain how Generative AI works, including training,
tokens, prompts, and model responses.
"""

print("\nTASK 2: LOW TOKEN LIMIT")
print(get_completion(prompt, max_tokens=30))

print("\nTASK 2: HIGH TOKEN LIMIT")
print(get_completion(prompt, max_tokens=200))


# Task 3: Experiment with context
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

print("\nTASK 3: CONTEXT EXPERIMENT")
print(get_completion(prompt, max_tokens=300))
