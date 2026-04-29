# 🧠 AI Debate System

A multi-agent AI system where two AI agents debate a topic and a judge agent evaluates the winner.

## 🚀 Live Demo
👉 https://your-render-link.onrender.com

---

## ⚙️ Features

- 🤖 Multi-Agent System (Debater A, Debater B, Judge)
- 🧠 Memory-augmented reasoning using ChromaDB (RAG)
- ⚡ Fast LLM responses using Groq API
- 🌐 Interactive UI built with Streamlit
- 🔁 Multi-round debates with contextual history

---

## 🏗️ Architecture

User → Streamlit UI → AI Agents → Memory (Vector DB) → Judge → Result

---

## 🧪 How It Works

1. User enters a debate topic
2. Debater A presents arguments
3. Debater B counters
4. This continues for multiple rounds
5. Judge agent evaluates and decides winner

---

## 📦 Tech Stack

- Python
- LangChain
- Groq LLM API
- ChromaDB (Vector Database)
- Streamlit

---

## 🛠️ Installation (Local)

```bash
git clone https://github.com/YOUR_USERNAME/AI-Debate-System.git
cd AI-Debate-System

pip install -r requirements.txt
