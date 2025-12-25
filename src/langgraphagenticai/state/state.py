from typing_extensions import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the strecture of the state used in graph
    """
    messages: Annotated[List, add_messages]