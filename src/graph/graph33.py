# from langgraph.graph import END, START, MessagesState, StateGraph
# from rich import print


# def build_graph():
#     pass


# def mock_llm(state: MessagesState):
#     return {"messages": [{"role": "ai", "content": "hello world"}]}


# graph = StateGraph(MessagesState)
# graph.add_node(mock_llm)
# graph.add_edge(START, "mock_llm")
# graph.add_edge("mock_llm", END)
# graph = graph.compile()

# result = graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
# print(result)

from collections.abc import Sequence
from typing import Annotated, Literal, TypedDict

from langchain_core.messages import AIMessage, BaseMessage
from langgraph.graph import END, START, StateGraph, add_messages


class GraphState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    output: str
    command: Literal["uppercase", "lowercase", "unknown"]


def identify_intent(state: GraphState):
    return {
        "output": "test",
        "messages": [AIMessage(content="Processado.........")],
    }


def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("identify_intent", identify_intent)

    workflow.add_edge(START, "identify_intent")
    workflow.add_edge("identify_intent", END)

    return workflow.compile()
