from .emailBot import MailBot
from .weatherBot import WheaterBot
from .utils import generateEmail
from datetime import datetime
from .validations import EmailValidation

from time import sleep

valid = EmailValidation()

class ForecastBot:
    def __init__(self, cityCoords = ['-22.739651', '-47.174052'], mailTo = 'icarogabrielsilva2019@gmail.com'):
        self.weatherConfig = {
            'cityCoords': cityCoords,
            'apiKey': '782cf97dc80bf5ae7be8c3a997990825',
            'units': 'metric'
        }
        self.mailTo = mailTo
        self.time = [False, False]

    def scheduleTime(self, hour = datetime.now().hour, minute = datetime.now().minute):
        valid.validateTimeInput(hour, minute)
        self.time[0] = hour
        self.time[1] = minute
        print(f'Schedule to {self.time[0]}:{self.time[1]}')
    
    def verifyTime(self):
        if not self.time[0] and not self.time[1]: return
        print(f'waiting until {self.time[0]}:{self.time[1]}...')
        while(True):
            if datetime.now().hour == self.time[0] and datetime.now().minute == self.time[1]: return

    def sendWeatherForecast(self):
        print(f'Starting the weather application...\n')
        self.verifyTime()
        try:
            weatherBot = WheaterBot(**self.weatherConfig)
            info = weatherBot.getWeather()
            email = generateEmail(info, self.mailTo)
            Emailbot = MailBot(**email)
            Emailbot.send()
        except Exception as error:
            print(f'Error ocurred -> {error}')
            sleep(15)
        finally:
            print(f'\nFinishing the weather application...')
