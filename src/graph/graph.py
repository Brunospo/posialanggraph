from collections.abc import Sequence
from typing import Annotated, Literal, TypedDict

from langchain_core.messages import AIMessage, BaseMessage
from langgraph.graph import END, START, StateGraph, add_messages


class GraphState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    output: str
    command: Literal["uppercase", "lowercase", "unknown"]


def identify_intent(state: GraphState):
    # Pega a última mensagem enviada pelo usuário no chat
    latest_message = state["messages"][-1].content if state["messages"] else ""

    return {
        "output": f"Recebido: {latest_message}",
        "messages": [AIMessage(content=f"Processado com sucesso: {latest_message}")],
    }


def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("identify_intent", identify_intent)

    workflow.add_edge(START, "identify_intent")
    workflow.add_edge("identify_intent", END)

    return workflow.compile()


# O LangGraph Studio procura por esta variável 'graph' por padrão
graph = build_graph()
