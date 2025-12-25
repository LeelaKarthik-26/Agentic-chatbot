import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Loads and runs the langGraph AgenticAI application with Streamlit UI,
    This function initilizes the UI, handles user inputs, configures the LLM model,
    sets up the graph based on the selected usecase, and display the output 
    While implementing execetion handling for robustness.
    """

    # Loading thr UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load the user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")
