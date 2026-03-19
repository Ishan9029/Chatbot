import streamlit as st
import requests
import uuid
import json
import os

# =========================
# CONFIG
# =========================
CHAT_FILE = "chats.json"
MAX_CONTEXT_MESSAGES = 10

API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
    "Content-Type": "application/json"
}

MODEL = "llama-3.1-8b-instant"

SYSTEM_PROMPTS = {
    "General": "You are a helpful assistant.",
    "Programming": "You are a precise programming assistant. Use code blocks and concise explanations.",
    "Study": "You are a tutor. Explain step by step in simple language.",
    "Math": "Solve step by step with formulas and correct reasoning."
}

# =========================
# GROQ FUNCTION
# =========================


def query_groq(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return f"Error: {response.text}"

    data = response.json()

    return data["choices"][0]["message"]["content"]


# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="ThinkBot AI", layout="centered")
st.markdown(
    """
    <h1 style='text-align: center;'>🤖 ThinkBot AI</h1>
    <p style='text-align: center; font-size:18px; color: gray;'>
    Your fast AI assistant powered by Groq
    </p>
    """,
    unsafe_allow_html=True
)

# =========================
# LOAD / SAVE
# =========================


def load_chats():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)
    return {}


def save_chats():
    with open(CHAT_FILE, "w") as f:
        json.dump(st.session_state.chats, f, indent=2)


# =========================
# SESSION INIT
# =========================
if "chats" not in st.session_state:
    st.session_state.chats = load_chats()

if "current_chat" not in st.session_state:
    cid = str(uuid.uuid4())
    st.session_state.chats[cid] = {
        "title": "New Chat",
        "system": SYSTEM_PROMPTS["General"],
        "messages": []
    }
    st.session_state.current_chat = cid

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("💬 Chats")

    if st.button("➕ New Chat"):
        cid = str(uuid.uuid4())
        st.session_state.chats[cid] = {
            "title": "New Chat",
            "system": SYSTEM_PROMPTS["General"],
            "messages": []
        }
        st.session_state.current_chat = cid
        save_chats()
        st.rerun()

# =========================
# CHAT DISPLAY
# =========================
chat = st.session_state.chats[st.session_state.current_chat]
messages = chat["messages"]

for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# INPUT
# =========================
user_input = st.chat_input("Type a message...")

if user_input:
    if not messages:
        chat["title"] = user_input[:40]

    messages.append({"role": "user", "content": user_input})
    save_chats()

    with st.chat_message("assistant"):
        placeholder = st.empty()

        trimmed = messages[-MAX_CONTEXT_MESSAGES:]

        groq_messages = [
            {"role": "system", "content": chat["system"]},
            *trimmed
        ]

        response = query_groq(groq_messages)

        placeholder.markdown(response)

    messages.append({"role": "assistant", "content": response})
    save_chats()
