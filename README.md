# 🧠 LearnLike5 – Explain Complex Ideas Like You're 5!

**LearnLike5** is a simple AI-powered agent that takes complex concepts and explains them like you're 5 years old – using analogies, stories, and simple language.

## ✨ What It Does

- Accepts a complex topic from the user  
- Uses **Google Gemini API** to break it down step-by-step  
- Simulates how an AI agent "thinks" (Thought → Action → Observation → Answer)  
- Outputs a friendly, kid-style explanation  
- Built with **Streamlit** for a quick and interactive UI

## 🚀 Tech Stack

- Python 🐍  
- Streamlit 🎈  
- Google Gemini API(free-tier)  
- Prompt Chaining / Reasoning Framework  
- `.env` for managing API keys

## 🛠️ Setup Instructions

1. Clone the repo  
   ```bash
   git clone https://github.com/anagha253/LearnLike5.git
   cd LearnLike5
   ```

2. Create a virtual environment  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add your Gemini API key:  
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the app  
   ```bash
   streamlit run app.py
   ```

## 💡 Example Prompt

> Topic: "Quantum Physics"

🧠 Thought → Action → Observation  
🗣️ Final Answer → "Imagine your toys suddenly disappearing and appearing somewhere else..."

## 📌 Future Improvements

- Add voice input support  
- Handle multiple follow-up questions  
- Deploy with user input logging (privacy-safe)

## 📚 Inspiration

This project was inspired by the idea that **learning can be fun and simple if explained the right way**.
