#Ignore import error - IDK why the python is getting error here, but it still working
from src.modules.ZapBot import WhatsappBot
from src.modules.CovidBot import CovidTracker
from src.modules.WeatherBot import ForecastBot
from src.modules.Colors import Colors
from src.modules.PreTexts import PreText

import platform
from os import system
from time import sleep

class Interface:
    def __init__(self):
        #Interface Section
        self.title = PreText.MAIN_TITLE
        self.menuItems = PreText.MENU_ITEMS
        self.help = PreText.HELP_MESSAGE
        self.statusMenu = False

        #Zap Section
        self.zapTitle = PreText.ZAP_TITLE
        self.zapMenu = PreText.ZAP_MENU
        self.zapHelp = PreText.ZAP_HELP

        #Covid Section
        self.covidTitle = PreText.COVID_TITLE
        self.covidMenu = PreText.COVID_MENU

        #Weather Section
        self.weatherTitle = PreText.WEATHER_TITLE
        self.weatherMenu = PreText.WEATHER_MENU
        self.weatherHelp = PreText.WEATHER_HELP

    def menu(self):
        print(self.title)
        print('Welcome again Icaro! Which automation do you wanna use now?')
        while not self.statusMenu:
            print(self.menuItems)
            option = str(input('->')).lower().strip()
            if option == '1':
                self.zapBot()
                self.clearScreen()
                print(self.title)
                continue
            elif option == '2':
                self.weatherBot()
                self.clearScreen()
                print(self.title)
                continue
            elif option == '3':
                self.covidBot()
                self.clearScreen()
                print(self.title)
                continue
            elif option == 'help':
                print(self.help)
                continue
            elif option == 'exit':
                self.statusMenu = True
                continue
            else:
                self.menuError(option)
                continue
        print(f'{Colors.OKGREEN}Thank you and check back often!{Colors.ENDC}')

    def menuError(self, userInput):
        message = f'''{Colors.WARNING}
        Oops! You've done a little mistake:
        "{userInput}" is not recognized as an internal command ):{Colors.ENDC}
        Please try it again...'''
        print(message)
        sleep(2)

    def zapBot(self):
        self.clearScreen()
        print(self.zapTitle)
        print("I need to know what message you'd like to send O.o")
        message = str(input('Message: ')).strip()
        print("Now I need to know who to send it to!\nIf you'll send for more than one person, separate the names with a comma!")
        sendTo = list(str(input('People: ')).split(','))
        for index, _ in enumerate(sendTo):
            sendTo[index].strip()
        print(f'\nOk I just save your content, check it out:\nMessage: {message}\nPeople: {sendTo}\n')
        status = False
        while not status:
            print('Select the option that fits for you (You can join more than one option):')
            print(self.zapMenu)
            option = str(input('->')).strip().lower()
            if option == '1':
                print('\nHow many times do you want to send the message?')
                flood = int(input('->'))
                print(f"Ok! I'll send {flood} times!\n")
                continue
            elif option == '2':
                print("Tell me the hour you need me to send the message:")
                hour = int(input('->'))
                print("Tell me the minute you need me to send the message:")
                minute = int(input('->'))
                print(f"Ok! I'll send the message at {hour}:{minute} !")
                continue
            elif option == '3':
                status = True
                continue
            elif option == 'abort': return
            elif option == 'help':
                print(self.zapHelp)
                continue
            else:
                self.menuError(option)
                continue
        whatsappBot = WhatsappBot(message, sendTo)
        if 'hour' in locals():
            if hour == 0:
                if minute != 0: whatsappBot.scheduleTime(minute=minute)
            else: whatsappBot.scheduleTime(hour, minute)
        if 'flood' in locals():
            if flood != 0:
                whatsappBot.sendFlood(flood)
                return
        whatsappBot.sendMessages()
        return

    def weatherBot(self):
        self.clearScreen()
        print(self.weatherTitle)
        status = False
        while not status:
            print('Select the option that fits for you (You can join more than one option):')
            print(self.weatherMenu)
            option = str(input('->')).strip().lower()
            if option == '1':
                print("Tell me the hour you need me to send the email:")
                hour = int(input('->'))
                print("Tell me the minute you need me to send the email:")
                minute = int(input('->'))
                print(f"Ok! I'll send the email at {hour}:{minute} !\n")
                continue
            elif option == '2':
                print('Insert the Latitude first:')
                latitude = str(input('->')).strip().replace(' ','')
                print('Now, the Longitude:')
                longitude = str(input('->')).strip().replace(' ','')
                coords = [latitude, longitude]
                print(f'Ok! The Latitude and longitude setted to: {coords}\n')
                continue
            elif option == '3':
                print('What the Email address I need to send the Forecast Information to?')
                email = str(input('->')).strip()
                print(f'Ok! The email setted now is: {email}\n')
                continue
            elif option == '4':
                status = True
                continue
            elif option == 'help':
                print(self.weatherHelp)
                continue
            elif option == 'abort': return
            else:
                self.menuError(option)
                continue
        
        if 'coords' in locals():
            if 'email' in locals(): forecastBot = ForecastBot(coords, email)
            else: forecastBot = ForecastBot(coords)
        else:
            if 'email' in locals(): forecastBot = ForecastBot(..., email)
            else: forecastBot = ForecastBot()
        
        if 'hour' in locals():
            if hour == 0:
                if minute != 0: forecastBot.scheduleTime(minute=minute)
            else: forecastBot.scheduleTime(hour, minute)
        
        forecastBot.sendWeatherForecast()
        return

    def covidBot(self):
        self.clearScreen()
        print(self.covidTitle)
        status = False
        while not status:
            print(self.covidMenu)
            option = str(input('->')).strip().lower()
            if option == 'go':
                status = True
                print('You may see some error but, do not care about them... :p')
                covidTracker = CovidTracker(True)
                covidTracker.fetch()
                continue
            elif option == 'see':
                status = True
                covidTracker = CovidTracker()
                covidTracker.fetch()
                continue
            elif option == 'abort': return
            else:
                self.menuError(option)
                continue
        return

    def clearScreen(self):
        system('cls') if platform.system() == 'Windows' else system('clear')
