# test_main.py
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

@patch("main.requests.post")
def test_predict_positive(mock_post):
    mock_post.return_value.json.return_value = [{"label": "POSITIVE", "score": 0.99}]
    response = client.post("/predict", json={"text": "I love this product"})
    assert response.status_code == 200
    assert response.json()["sentiment"][0]["label"] == "POSITIVE"
