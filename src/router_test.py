from fastapi.testclient import TestClient

from src.server import create_server


def test_teste():

    app = create_server()
    client = TestClient(app)

    msg = "Make this message UPPER please"

    response = client.post("/chat", json={"question": msg})
    print(response.json())

    assert response.status_code == 200
    assert response.json() == "test"
