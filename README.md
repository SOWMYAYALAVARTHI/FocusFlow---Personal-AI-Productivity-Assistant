# 🧠 FocusFlow – Personal AI Productivity Assistant

**FocusFlow** is an intelligent, conversational productivity assistant built using the **Gemini 1.5 Flash API** and **Streamlit**. It helps users plan their day, stay focused, build better habits, and manage tasks — all through a friendly, emoji-enhanced chat interface.

---

## 🚀 Features

- 📅 Smart daily planning & task suggestions  
- 🎯 Focus techniques (Pomodoro, time-blocking, etc.)  
- 🧘 Motivational quotes & habit tips  
- 📚 Quick summaries of productivity methods  
- 💬 Friendly, lightweight UI with chat interaction  
- 🔐 Keeps your API key secure via `.env`

---

## 🛠 Tech Stack

- [Google Gemini 1.5 Flash API](https://ai.google.dev)
- [Streamlit](https://streamlit.io)
- Python 3.9+
- `.env` for secure key handling

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/yourusername/FocusFlow---Personal-AI-Productivity-Assistant.git
cd FocusFlow---Personal-AI-Productivity-Assistant

# Install dependencies
pip install streamlit google-generativeai python-dotenv

# Add your API key to .env
echo API_KEY=your_gemini_api_key_here > .env

# Run the chatbot
streamlit run app.py

## 📸 Screenshots

![FocusFlow Chatbot Demo]([FocusFlow_Demo.png](https://github.com/SOWMYAYALAVARTHI/FocusFlow---Personal-AI-Productivity-Assistant/blob/main/FocusFlow_Demo.png))


This project is for educational and demonstration purposes. Please do not use your Gemini API key in production without proper security and compliance.
