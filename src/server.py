from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from src.graph.graph import build_graph


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=5)


def create_server() -> FastAPI:
    app = FastAPI()

    @app.post("/chat")
    async def chat(request: ChatRequest):
        try:
            question = request.question
            response = build_graph().invoke({"messages": question})
            return response["output"]
        except Exception as ecx:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ecx)
            ) from ecx

    return app
