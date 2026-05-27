import pytest
from app import app

def test_home_page_loads():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_study_page_loads():
    client = app.test_client()
    response = client.get('/study')
    assert response.status_code == 200
