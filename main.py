import streamlit as st 
from backend import get_Client,get_gemini_response
st.title("My RAG Chatbot")
client=get_Client()
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
user_input = st.chat_input("Type your message ...")
if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.write(user_input)
    bot_reply = get_gemini_response(client,user_input)
    st.session_state.messages.append({"role":"assistant","content":bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
