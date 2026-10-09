from langchain_core.messages import AIMessage

from src.graph.state import GraphState


def chat_response(state: GraphState) -> GraphState:
    response_text = state["output"]

    ai_message = AIMessage(response_text)

    return {**state, "messages": [ai_message]}
