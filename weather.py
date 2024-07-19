import requests
from dataclasses import dataclass
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')
@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float

def get_lat_lon(city_name, API_key):
    resp = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}").json()
    if not resp:
        raise Exception(f"Город '{city_name}' не найден")
    data = resp[0]
    lat, lon = data.get("lat"), data.get('lon')
    return lat, lon

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric").json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp')
    )
    return data

def main(city_name):
    lat, lon = get_lat_lon(city_name, API_KEY)
    weather_data = get_current_weather(lat, lon, API_KEY)
    return weather_data