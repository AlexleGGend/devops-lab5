import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import app

client = TestClient(app)


def test_get_existed_user():
    """Тест получения существующего пользователя"""
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1


def test_get_nonexistent_user():
    """Тест получения несуществующего пользователя"""
    response = client.get("/users/999")
    assert response.status_code == 404


def test_create_user():
    """Тест создания пользователя"""
    response = client.post("/users", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"


def test_update_user():
    """Тест обновления пользователя"""
    response = client.put("/users/1", json={"name": "Updated Name"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"


def test_delete_user():
    """Тест удаления пользователя"""
    response = client.delete("/users/1")
    assert response.status_code == 204
