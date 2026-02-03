import requests

# Базовый URL для учебного API
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_get_all_posts_status_code():
    """Проверка получения всех постов (должен быть 200 OK)"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_single_post():
    """Проверка получения конкретного поста по ID"""
    post_id = 1
    response = requests.get(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_create_post():
    """Проверка создания нового поста (возвращает 201 Created)"""
    payload = {
        "title": "QA Test",
        "body": "Automation is cool",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]

def test_delete_post():
    """Проверка удаления поста (возвращает 200 OK)"""
    post_id = 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200
