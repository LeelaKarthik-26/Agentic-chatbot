import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI():
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖"+ self.config.get_page_title(), layout="wide")
        st.header("🤖"+ self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM:", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select model:", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter API key:", type="password")
                
                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to proceed. Don't have an API Key? Get it from here: https://console.groq.com/keys")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase:", usecase_options)
            
            # Tavily API Key
            if self.user_controls["selected_usecase"] == "chatbot with web" or self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Enter Tavily API key:", type="password")

                # Validate Tavily API Key
                if not self.user_controls.get("TAVILY_API_KEY"):
                    st.warning("Please enter your Tavily API Key to proceed. Don't have an API Key? Get it from here: https://app.tavily.com/home")
            
            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📅 AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "🕰️ Select time frame:",
                        ["Today", "Yesterday", "This Week", "This Month", "This Year"],
                        index=0
                    )
                
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.TimeFrame = time_frame

                
        return self.user_controls