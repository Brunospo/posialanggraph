from typing import Literal

from src.graph.state import GraphState


def identify_intent(state: GraphState) -> GraphState:
    messages = state.get("messages", [])
    user_input: str = messages[-1].content if messages else ""
    user_input_lower: str = user_input.lower()

    meu_comando: Literal["uppercase", "lowercase", "unknown"] = "unknown"

    if "upper" in user_input_lower:
        meu_comando = "uppercase"
    elif "lower" in user_input_lower:
        meu_comando = "lowercase"

    return {**state, "command": meu_comando, "output": user_input}
