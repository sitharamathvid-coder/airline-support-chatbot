import streamlit as st
import requests

# 🔗 Your n8n webhook URL
WEBHOOK_URL = "http://localhost:5678/webhook/airline-chat"

st.set_page_config(page_title="✈️ Airline Chatbot", layout="centered")

st.title("✈️ Airline Support Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask about flights, baggage, delays...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... ✈️"):

            try:
                response = requests.post(
                    WEBHOOK_URL,
                    json={"chatInput": user_input},
                    timeout=60   # 🔥 prevents hanging forever
                )

                # Handle non-200 responses
                if response.status_code != 200:
                    bot_reply = f"⚠️ Server error: {response.status_code}"
                else:
                    data = response.json()

                    # Safe parsing
                    bot_reply = (
                        data.get("output")
                        or data.get("message")
                        or "⚠️ No response from system"
                    )

            except requests.exceptions.Timeout:
                bot_reply = "⏳ Server is taking too long. Please try again."

            except Exception as e:
                bot_reply = f"⚠️ Error: {str(e)}"

        st.markdown(bot_reply)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})