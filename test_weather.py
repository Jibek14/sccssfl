import pytest
import os
from dotenv import load_dotenv
from weather import get_lat_lon, get_current_weather
load_dotenv()
API_KEY = os.getenv('API_KEY')


def test_get_lat_lon():
    city_name = 'Toronto'
    lat, lon = get_lat_lon(city_name, API_KEY)
    assert lat is not None
    assert lon is not None

def test_get_current_weather():
    lat, lon = get_lat_lon('Toronto', API_KEY)
    weather_data = get_current_weather(lat, lon, API_KEY)
    assert weather_data.main is not None
    assert weather_data.description is not None
    assert weather_data.icon is not None
    assert weather_data.temperature is not None
