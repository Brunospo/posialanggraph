from collections.abc import Sequence
from typing import Annotated, Literal, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class GraphState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    output: str
    command: Literal["uppercase", "lowercase", "unknown"]
