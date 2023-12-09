import streamlit as st
import random
import time
from streamlit.components.v1 import html

with open('/css/elastic-styles.css') as f: 
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("EXPLORE AWAY")

with st.chat_message("assistant"):
    st.write('''Prompt suggestions:  
            'I want to go to Italy for 2 months while I work for a company in Miami.'  
            'What do I need to know as a tech nomad from USA working in Mexico.'  
            'How much could it cost to live and work in Morocco for 6 months' ''')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        
if prompt := st.chat_input("Enter a prompt"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})