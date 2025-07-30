import requests
from config.settings import API_KEYS

class WeatherFetcher:
    @staticmethod
    def get_openweather(lat, lon):
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEYS['openweathermap']}&units=metric"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_weatherapi(location):
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEYS['weatherapi']}&q={location}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_weatherbit(lat, lon):
        url = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={API_KEYS['weatherbit']}"
        response = requests.get(url)
        return response.json()