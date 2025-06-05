# 🧠 Django Chatbot with SQLite3 & Ollama Integration

This is a Django-based chatbot project that connects user data via SQLite3 and utilizes a locally hosted [Ollama](https://ollama.com/) language model (`qwen:4b`) for generating intelligent responses.

---

## 🚀 Features

* 💬 Interactive chatbot built with Django
* 🧑‍💃 User messages stored and managed via `db.sqlite3`
* 🧠 Local integration with Ollama's `qwen:4b` model for response generation
* 🔐 Basic user data handling and history storage
* 🛠️ Easily customizable for different LLM models

---

## 📁 Project Structure

```
chatbot_project/
├── chatbot/             # Django app handling chat logic
│   ├── models.py        # SQLite models for chat history
│   ├── views.py         # Main chat views
│   ├── urls.py          # Routes for chatbot
│   └── templates/       # Frontend chat UI
├── chatbot_project/
│   ├── settings.py      # Django settings
│   └── urls.py          # Root routing
├── manage.py            # Django CLI
└── README.md
```

---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/django-chatbot-ollama.git
   cd django-chatbot-ollama
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Start the Django development server:**

   ```bash
   python manage.py runserver
   ```

5. **Make sure your Ollama model (`qwen:4b`) is running locally:**

   ```bash
   ollama pull qwen:4b
   ollama run qwen:4b
   ```

---

## 🧠 Ollama Integration

The chatbot connects to a local Ollama model through HTTP API calls (typically on `http://localhost:11434`). Make sure the Ollama service is running before starting the chatbot.

In `views.py`:

```python
response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "qwen:4b", "prompt": user_input}
)
```

---

## 🗓️ Database

* Uses SQLite3 by default (`db.sqlite3`)
* Stores user messages and bot responses
* Easily replaceable with PostgreSQL or MySQL if scaling is needed

---

## 📌 Example Usage

Once running, navigate to:

```
http://127.0.0.1:8000/chat/
```

Start chatting with your AI-powered assistant. All conversations are stored and managed seamlessly via Django ORM.

---

## 📌 License

This project is licensed under the MIT License.




