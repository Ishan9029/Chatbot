# 🤖 Ishan BOT (AI Chatbot)

A fast and modern AI chatbot built using **Streamlit** and powered by the **Groq API (LLaMA 3.1 models)**.
This project provides a clean chat interface with multi-chat support and customizable system prompts.

---

## 🚀 Features

* 💬 Multi-chat conversation system
* 🧠 Custom system prompts (General, Programming, Study, Math)
* ⚡ Ultra-fast responses using Groq API
* 🖥️ Clean and simple UI with Streamlit
* 📁 Chat history management
* 🔄 Context-aware responses

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API (LLaMA 3.1)
* Requests

---

## 📂 Project Structure

```
chatbot/
│
├── app.py               # Main Streamlit app
├── requirements.txt    # Dependencies
├── chats.json          # Chat storage (optional)
├── README.md           # Project documentation
└── .gitignore          # Ignore unnecessary files
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Ishan9029/Chatbot.git
cd Chatbot
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup API Key (IMPORTANT)

Create a folder:

```
.streamlit
```

Inside it, create a file:

```
secrets.toml
```

Add your Groq API key:

```toml
GROQ_API_KEY = "your_api_key_here"
```

> ⚠️ Never upload this file to GitHub

---

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This app can be deployed for free using:

👉 Streamlit Community Cloud

### Steps:

1. Push your code to GitHub
2. Go to Streamlit Cloud
3. Create a new app
4. Add your `GROQ_API_KEY` in **Secrets**
5. Deploy

---

## 🔐 Security Note

* API keys are stored securely using Streamlit Secrets
* `.streamlit/secrets.toml` is excluded using `.gitignore`
* Never expose your API key publicly

---

## ⚡ Supported Models

* `llama-3.1-8b-instant` (recommended)
* `llama-3.1-70b-versatile`

---

## 📸 Screenshots (Optional)

*Add screenshots of your chatbot UI here for better presentation*

---

## 🎯 Future Improvements

* Typing animation (streaming responses)
* Voice assistant integration
* Chat export feature
* Dark mode UI enhancements

---

## 👨‍💻 Author

**Ishan Ahmed**

* GitHub: https://github.com/Ishan9029

---

## ⭐ Contribute / Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🛠️ Improve it

---

## 📄 License

This project is open-source and available under the MIT License.
