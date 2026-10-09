from src.graph.state import GraphState


def lower_case(state: GraphState) -> GraphState:
    response_text: str = state["output"].lower()

    return {**state, "output": response_text}
