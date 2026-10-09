from typing import Literal

from src.graph.state import GraphState


def the_conditional(
    state: GraphState,
) -> Literal["goes_to_lower", "goes_to_upper", "fallback"]:
    if state["command"] == "uppercase":
        return "goes_to_upper"
    elif state["command"] == "lowercase":
        return "goes_to_lower"

    return "fallback"
