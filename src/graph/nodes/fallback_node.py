from src.graph.state import GraphState


def fallback(state: GraphState) -> GraphState:
    message: str = (
        'Unknown command. try "make this uppercase" or "convert to lower case"'
    )

    return {**state, "output": message}
