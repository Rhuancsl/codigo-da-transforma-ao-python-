# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run()

# test_app.py (pytest)
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_soma(client):
    response = client.get("/soma/2/3")
    json_data = response.get_json()
    assert json_data["resultado"] == 5
