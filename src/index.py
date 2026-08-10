from src.server import create_server

if __name__ == "__main__":
    import uvicorn

    app = create_server()
    uvicorn.run(app, host="0.0.0.0", port=3000)
