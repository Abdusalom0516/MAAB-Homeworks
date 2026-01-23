# ## Task 1: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the `requests` library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import os
from dotenv import load_dotenv
import requests

load_dotenv()

city_lat = 41.2995
city_long = 69.2401

class WeatherApp:
    __BASE_URL = 'https://api.openweathermap.org/'
    __api_key = os.getenv("OPENWEATHER_API_KEY")

    def getCurrentWeather(self, *, city_lat: float, city_long: float):
        current_weather_endpoint = "data/2.5/weather"
        response = requests.get(self.__BASE_URL + current_weather_endpoint,
        params={"lat": city_lat, "lon": city_long, "appid": self.__api_key, "units": "metric"})

        if response:
            response = response.json()
            mainData = response["main"]

            temperature = mainData["temp"]
            humidity = mainData["humidity"]
            feels_like = mainData["feels_like"]
            name = response["name"]
            wind_speed = response["wind"]["speed"]
            temp_min = mainData["temp_min"]
            temp_max = mainData["temp_max"]

            print(f"Today the temperature is {temperature} C, the max temperature will be {temp_max} C, minimum temperature will be {temp_min} C, temperature feels like {feels_like} C, today humidity will be {humidity} and the wind speed will be {wind_speed}.")
        else:
            print(response.status_code)
            print(response.text)





# ## Task 2: Movie Recommendation System
#    1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.
import random
class MovieRecommendationApp:
    __BASE_URL = 'https://api.themoviedb.org/3/'
    __api_key = os.getenv("MOVIE_API_KEY")

    def __init__(self):
        pass

    def getGenres(self) -> None:
        genresEndpoint = "genre/movie/list?language=en"
        request = requests.get(self.__BASE_URL + genresEndpoint, headers={"accept": "application/json", "Authorization": f"Bearer {self.__api_key}"})
        if request:
            for genre in request.json()["genres"]:
                print(f'{genre["name"]} - ID: {genre["id"]}')
        else:
            return print("Genres not found!")

    def getRandomMovieRecommendation(self):
        self.getGenres()
        movieGenreID = input("Enter a genre ID: ")
        endpoint = f"discover/movie?include_adult=false&language=en-US&with_genres={movieGenreID}&limit=1&sort_by=popularity.desc"
        request = requests.get(self.__BASE_URL + endpoint, headers={"accept": "application/json", "Authorization": f"Bearer {self.__api_key}"})
        if request:
            moviesList = request.json()["results"]
            randomNumber = random.randint(0, len(moviesList)-1)
            chosenMovie = moviesList[randomNumber]

            print("FOUND ✅")
            print(f'Movie title: {chosenMovie["title"]}, overview of the movie: {chosenMovie["overview"]} and the movie released in {chosenMovie["release_date"]}.')
        else:
            print(request.status_code)
            print(request.reason)










if __name__ == "__main__":
    weatherApplication = WeatherApp()

    weatherApplication.getCurrentWeather(city_lat=city_lat, city_long=city_long)

    movieRecommendationApp = MovieRecommendationApp()

    movieRecommendationApp.getRandomMovieRecommendation()