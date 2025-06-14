# Insta-Client-Consultant Bot

An **AI-powered Instagram DM assistant** that logs into your business account, reads unread messages, remembers recent chat context, and responds like a **friendly client-solutions consultant (“Sivaraj”)**.

It combines:

| Layer         | Tech                                      |
|---------------|-------------------------------------------|
| Messaging     | [instagrapi](https://github.com/adw0rd/instagrapi) – login & DM handling |
| GenAI Model 1 | [Google Gemini](https://ai.google.dev/)  |
| GenAI Model 2 | [Ollama](https://ollama.com) – local LLMs |
| Prompting     | Custom client-management consultant prompt |
| Scheduler     | `while True + time.sleep()` loop          |

---

## ✨ Features

- ✅ Reads only **unread Instagram DMs**
- ✅ Maintains **recent conversation history** for reply context
- ✅ Uses **Ollama** (local) and **Gemini** (cloud) to generate replies
- ✅ **Acts like a technical consultant**, not a bot
- ✅ **Auto-replies and marks messages as seen**
- ✅ Modular prompt for changing behavior (support, sales, friend, etc.)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/insta-client-consultant.git
cd insta-client-consultant
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
