from src.graph.state import GraphState


def upper_case(state: GraphState) -> GraphState:
    response_text: str = state["output"].upper()

    return {**state, "output": response_text}
