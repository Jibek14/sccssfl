import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Weather App' in response.get_data(as_text=True)

def test_weather_request(client):
    response = client.post('/', data={'cityName': 'Toronto'})
    assert response.status_code == 200
    assert 'Weather in Toronto' in response.get_data(as_text=True)


def test_invalid_city(client):
    response = client.post('/', data={'cityName': 'InvalidCity'})
    assert response.status_code == 200
    assert "Ошибка: Город 'InvalidCity' не найден" in response.get_data(as_text=True)
