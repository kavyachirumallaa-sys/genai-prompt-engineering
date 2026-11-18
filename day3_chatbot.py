
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)

# Store conversation history
conversation_history = []

print("Chatbot started!")
print("Type 'exit' to stop.\n")


while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    if user_message.lower() == "clear":
        conversation_history.clear()
        print("Chatbot: Conversation history cleared!\n")
        continue

    conversation_history.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=conversation_history
        )

        bot_reply = response.text

        if not bot_reply:
            bot_reply = "I couldn't generate a response. Please try again."

    except Exception as e:
        print("Chatbot: Sorry, the API request failed.")
        print("Error:", e)
        continue

    conversation_history.append({
        "role": "model",
        "parts": [{"text": bot_reply}]
    })

    print("Chatbot:", bot_reply, "\n")
