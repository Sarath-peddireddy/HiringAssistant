import streamlit as st
from src.chatbot.assistant import HiringAssistant
from src.config import load_config

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_step" not in st.session_state:
        st.session_state.current_step = "greeting"
    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = {}

def main():
    st.title("TalentScout Hiring Assistant")
    
    # Initialize session state
    initialize_session_state()
    
    # Initialize the hiring assistant
    assistant = HiringAssistant()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Initial greeting
    if len(st.session_state.messages) == 0:
        initial_message = assistant.get_greeting()
        st.session_state.messages.append({"role": "assistant", "content": initial_message})
        with st.chat_message("assistant"):
            st.write(initial_message)
    
    # Get user input
    if user_input := st.chat_input("Type your response here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        
        # Get assistant response and next step
        response, next_step = assistant.process_input(user_input, st.session_state.current_step)
        
        # Update the current step
        st.session_state.current_step = next_step
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

if __name__ == "__main__":
    main() 