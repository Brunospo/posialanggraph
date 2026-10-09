from langgraph.graph import END, START, StateGraph

from src.graph.nodes.chat_response_node import chat_response
from src.graph.nodes.conditional_node import the_conditional
from src.graph.nodes.fallback_node import fallback
from src.graph.nodes.identify_intent_node import identify_intent
from src.graph.nodes.lower_case_node import lower_case
from src.graph.nodes.upper_case_node import upper_case
from src.graph.state import GraphState


def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("identify_intent", identify_intent)
    workflow.add_node("chat_response", chat_response)
    workflow.add_node("upper_case", upper_case)
    workflow.add_node("lower_case", lower_case)
    workflow.add_node("fallback", fallback)

    workflow.add_edge(START, "identify_intent")
    workflow.add_conditional_edges(
        "identify_intent",
        the_conditional,
        {
            "goes_to_upper": "upper_case",
            "goes_to_lower": "lower_case",
            "fallback": "fallback",
        },
    )
    workflow.add_edge("upper_case", "chat_response")
    workflow.add_edge("lower_case", "chat_response")
    workflow.add_edge("fallback", "chat_response")
    workflow.add_edge("chat_response", END)

    return workflow.compile()
