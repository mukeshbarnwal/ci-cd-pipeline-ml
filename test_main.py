from unittest.mock import patch, MagicMock

# Patch OpenAI client before importing app
with patch("app.main.OpenAI") as MockOpenAI:
    mock_client = MagicMock()
    MockOpenAI.return_value = mock_client
    from app.main import app

from fastapi.testclient import TestClient

client = TestClient(app)


@patch("app.main.requests.post")
def test_predict_positive(mock_post):
    mock_post.return_value.json.return_value = [
        {"category": "Shipping"}
    ]

    response = client.post("/predict", json={"text": "delivery issue"})

    assert response.status_code == 200
    assert response.json()["category"] == "Shipping"
