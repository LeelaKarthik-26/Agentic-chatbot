import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import Groqllm
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultstreamlit

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
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # configure the LLM model
            obj_llm_config = Groqllm(user_controls_input= user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not me initialized.")
                return

            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected.")
                return

            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultstreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Graph setup failed: {str(e)}")
                return
        
        except Exception as e:
            st.error(f"Error: Graph setup failed: {str(e)}")
            return