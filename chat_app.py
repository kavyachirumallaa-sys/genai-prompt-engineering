
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found. Check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

st.set_page_config(page_title="My Gemini Chatbot", page_icon="💬")

st.title("💬 My Gemini Chatbot")
st.caption("A simple chatbot powered by Google's Gemini API")

# Store conversation history for this browser session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept a new message
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Convert Streamlit history to Gemini's expected format
    conversation_history = [
        {
            "role": "user" if msg["role"] == "user" else "model",
            "parts": [{"text": msg["content"]}]
        }
        for msg in st.session_state.messages
    ]

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=conversation_history
                )

                reply = response.text or "I couldn't generate a response."
                st.markdown(reply)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": reply
                })

            except Exception as e:
                st.error("The API request failed. Please try again.")
                st.caption(str(e))

# Clear conversation button
if st.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()
