from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    This class represents a chatbot node with tool integration.
    """
    def __init__(self, model):
        self.llm = model

    # optional process to generate a response with tool integration
    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke({'role': 'user', 'content': user_input})

        # simulate tool call
        tools_response = f"Tool intergation for: {user_input}"

        return {'messages': [llm_response, tools_response]}

    def create_chatbot(self, tools):
        """
        Returns a chatbot node funation.
        """
        llm_with_tools = self.llm.bind_tools(tools)
        
        def create_node(state: State):
            """
            chatbot logic for proessing the input state and returning a response
            """
            return {'messages': [llm_with_tools.invoke(state['messages'])]}

        return create_node