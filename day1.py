
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)


# Basic function to get a response from Gemini
def get_completion(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text


# Task 1: Clear instructions
prompt = """
Explain Python to a complete beginner.
Give exactly 3 bullet points.
Use simple English.
Keep each bullet to one sentence.
"""

print("TASK 1: CLEAR INSTRUCTIONS")
print(get_completion(prompt))


# Task 2: Using delimiters
text_to_summarize = """
Generative AI can create text, images, and code.
Developers use APIs to integrate AI models into applications.
Prompt engineering helps developers guide model responses.
"""

prompt = f"""
Summarize the text between the triple backticks
in exactly two bullet points.

Text:
```{text_to_summarize}```
"""

print("\nTASK 2: DELIMITERS")
print(get_completion(prompt))


# Task 3: Request JSON output
prompt = """
Give 3 useful Python tips.
Return the result as a valid JSON object.
Use the key "tips" with a list of 3 strings.
Do not include Markdown or explanations outside the JSON.
"""

print("\nTASK 3: JSON OUTPUT")
print(get_completion(prompt))


# Task 4: Output constraints
prompt = """
Explain why Python is useful.
Give exactly 3 bullet points.
Each bullet must contain fewer than 15 words.
Use simple English.
Do not include an introduction or conclusion.
"""

print("\nTASK 4: OUTPUT CONSTRAINTS")
print(get_completion(prompt))


# Task 5: Reusable text summarizer
def summarize_text(text):
    prompt = f"""
    Summarize the text enclosed in triple backticks.
    Preserve the main ideas and use simple English.

    Text:
    ```{text}```
    """
    return get_completion(prompt)


sample_text = """
Python is a popular programming language.
It is used in web development, automation, data science,
and artificial intelligence. Its readable syntax makes it
a useful language for beginners.
"""

print("\nTASK 5: TEXT SUMMARIZER")
print(summarize_text(sample_text))
