import pytest
from app import app

def test_home():
    response_get = app.test_client().get('/', follow_redirects=True)
    assert response_get.status_code == 200  # Redirecting to login page

def test_login():
    data = dict(username='testUser',password='testPassword',instance_url='https://central.xnat.org')
    response_post = app.test_client().post('/login', data=data, follow_redirects=True)
    response_get = app.test_client().get('/login')
    assert response_post.status_code == 200  # Redirecting to dashboard
    assert response_get.status_code == 200


def test_dashboard():
    response_get = app.test_client().get('/dashboard')
    assert response_get.status_code == 200