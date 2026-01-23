# ## Task 1: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the `requests` library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests

BASE_URL = 'https://openweathermap.org/'
currentWeatherEndpoint = "data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

cityLat = 41.2995
cityLong = 69.2401


class WeatherApi:
    cityLat: float
    cityLong: float

    def __init__(self, cityLat: float, cityLong: float):
        self.cityLat = cityLat
        self.cityLong = cityLong

    def getCurrentWeather():
        print("Fuck you")






