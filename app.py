import streamlit as st
import google.generativeai as genai
import dotenv
import os
dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
def response(messages):
  try:
    response = model.generate_content(messages)
    return response
  except Exception as e:
    return f"Error: {str(e)}"

def fetch_conversation_history():
  if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "user", "parts": "System prompt: FocusFlow - You are a friendly and highly efficient AI productivity assistant. Greet the user warmly and ask how you can help with their productivity today. Based on their input, respond clearly and concisely with helpful suggestions, organized steps, or motivational tips. You can help with tasks like:– Creating or organizing to-do lists 📝– Planning a productive day or week 📅– Explaining productivity techniques (e.g., Pomodoro, time-blocking) ⏱– Offering quick summaries of productivity concepts 📊– Suggesting focus or habit-building strategies 💡Keep responses under 100 words. Use emojis to enhance clarity and keep the tone upbeat, focused, and supportive. Include links or visuals (YouTube/tutorials/images) if the user asks for examples. Always encourage users to take small, manageable steps."}
    ]
  return st.session_state["messages"]
st.title("FocusFlow - Personal AI Productivity Assistant")
user_input = st.chat_input("You: ")

if user_input:
  messages = fetch_conversation_history()
  messages.append({"role": "user", "parts": user_input})
  response = response(messages)
  messages.append({"role": "model", "parts": response.candidates[0].content.parts[0].text})

  for message in messages:
    if message["role"] == "model":
      st.write(f"FocusFlow: {message['parts']}")
    elif message["role"] == "user" and "System prompt" not in message["parts"]:
      st.write(f"You: {message['parts']}")
