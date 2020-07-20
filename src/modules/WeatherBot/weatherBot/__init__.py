import json
import requests
from src.modules.WeatherBot.utils import filterApiInfo
from src.modules.WeatherBot.validations import WeatherValidation

valid = WeatherValidation()

class WheaterBot:
    def __init__(self, cityCoords = False, apiKey = False, units = False):
        valid.validateInput(cityCoords, apiKey, units)
        self.cityCoords = cityCoords
        self.apiKey = apiKey
        self.units = units

    def generateURL(self):
        return f'https://api.openweathermap.org/data/2.5/onecall?lat={self.cityCoords[0]}&lon={self.cityCoords[1]}&units={self.units}&appid={self.apiKey}'


    def getWeather(self):
        url = self.generateURL()
        apiResponse = requests.get(url).json()
        valid.validateContent(apiResponse)
        apiResponse = filterApiInfo(apiResponse)
        return apiResponse
