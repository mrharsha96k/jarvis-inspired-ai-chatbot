#  Jarvis-Inspired AI Web Chatbot

An interactive AI web application inspired by JARVIS, featuring a central animated core for user input and a dedicated response panel for AI-generated answers.

##  Features
- AI-powered chatbot using **Groq API**
- Central animated interface (GIF-based Jarvis core)
- Search box embedded inside the animation
- Right-side response panel
- Click-to-speak  voice output using Web Speech API
- Clean, futuristic UI

##  Tech Stack
- Python
- Flask
- Groq API (LLM)
- HTML, CSS, JavaScript
- Web Speech API

##  How It Works
1. User enters a question inside the animated core.
2. The query is sent to the Flask backend.
3. Groq AI processes the request.
4. The response appears in the right-side panel.
5. User can click the response to hear it spoken aloud.

##  Run Locally
```bash
python app.py
