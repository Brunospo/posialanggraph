from fastapi.testclient import TestClient

from src.server import create_server


def test_upper_case():

    app = create_server()
    client = TestClient(app)

    msg = "Make this message UPPER please"

    response = client.post("/chat", json={"question": msg})

    assert response.status_code == 200
    assert response.json() == msg.upper()


def test_lower_case():

    app = create_server()
    client = TestClient(app)

    msg = "Make this message LOWER please"

    response = client.post("/chat", json={"question": msg})

    assert response.status_code == 200
    assert response.json() == msg.lower()


def test_fallback():

    app = create_server()
    client = TestClient(app)

    msg = "HY there!"

    response = client.post("/chat", json={"question": msg})

    assert response.status_code == 200
    assert (
        response.json()
        == 'Unknown command. try "make this uppercase" or "convert to lower case"'
    )
