import sys
sys.path.append('../')

import streamlit as st
from agent.customer_agent import create_agent


st.set_page_config(page_title="Service Agent", layout="centered")
st.title("🤖 AI KnowledgeBase Browser Agent")

# Initialize LangChain agent 
if "agent" not in st.session_state:
    st.session_state.agent = create_agent()


# UI Controls 
st.write("### Type your query below")
user_input = st.text_input("Ask a question or enter a user ID:")

# Agent interaction 
if st.button("Submit") and user_input:
    with st.spinner("Thinking…"):
        response = st.session_state.agent.run(user_input)
    st.success(response)
    st.session_state.transcribed_text = ""
    
    
    
    
