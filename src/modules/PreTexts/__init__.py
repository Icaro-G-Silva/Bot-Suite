from src.modules.Colors import Colors
class PreText:
    MAIN_TITLE = r'''
  _____                    _       ____        _      _____       _ _       
 |_   _|                  ( )     |  _ \      | |    / ____|     (_) |      
   | |  ___ __ _ _ __ ___ |/ ___  | |_) | ___ | |_  | (___  _   _ _| |_ ___ 
   | | / __/ _` | '__/ _ \  / __| |  _ < / _ \| __|  \___ \| | | | | __/ _ \
  _| || (_| (_| | | | (_) | \__ \ | |_) | (_) | |_   ____) | |_| | | ||  __/
 |_____\___\__,_|_|  \___/  |___/ |____/ \___/ \__| |_____/ \__,_|_|\__\___|

    '''
    COVID_TITLE = r'''
   _____           _     _ ____        _   
  / ____|         (_)   | |  _ \      | |  
 | |     _____   ___  __| | |_) | ___ | |_ 
 | |    / _ \ \ / / |/ _` |  _ < / _ \| __|
 | |___| (_) \ V /| | (_| | |_) | (_) | |_ 
  \_____\___/ \_/ |_|\__,_|____/ \___/ \__|
                                           
'''
    WEATHER_TITLE = r'''
 __          __        _   _               ____        _   
 \ \        / /       | | | |             |  _ \      | |  
  \ \  /\  / /__  __ _| |_| |__   ___ _ __| |_) | ___ | |_ 
   \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|  _ < / _ \| __|
    \  /\  /  __/ (_| | |_| | | |  __/ |  | |_) | (_) | |_ 
     \/  \/ \___|\__,_|\__|_| |_|\___|_|  |____/ \___/ \__|
                                                               
'''
    ZAP_TITLE = r'''
  ______           ____        _   
 |___  /          |  _ \      | |  
    / / __ _ _ __ | |_) | ___ | |_ 
   / / / _` | '_ \|  _ < / _ \| __|
  / /_| (_| | |_) | |_) | (_) | |_ 
 /_____\__,_| .__/|____/ \___/ \__|
            | |                    
            |_|                    

'''

    MENU_ITEMS = f'''{Colors.BOLD}
        1) ZapBot
        2) WeatherBot
        3) CovidBot
        {Colors.ENDC}
        If you want to get out of here just type '{Colors.UNDERLINE}exit{Colors.ENDC}'
        If you don't remember how the Bots works just type '{Colors.UNDERLINE}help{Colors.ENDC}' :)
        '''
    
    HELP_MESSAGE = f'''{Colors.OKBLUE}
        Check the items out!

        ZapBot -> Whatsapp Bot that send messages to N contacts you want to.

        WeatherBot -> Weather Bot that catch the forecast informations according to the coordinates and send you a formatted email

        CovidBot -> Covid Bot that do the track of coronavirus in the Brazil and save the information into archives (json and txt){Colors.ENDC}'''

    ZAP_MENU = f'''{Colors.BOLD}
        1) Flood System ;p
        2) Schedule :o
        3) All done. Send it! :D
        {Colors.ENDC}
        If you want to abort the operation and get back to the menu just type '{Colors.UNDERLINE}abort{Colors.ENDC}'
        If you don't remember how any of these options works just type '{Colors.UNDERLINE}help{Colors.ENDC}' :)
    '''

    ZAP_HELP = f'''{Colors.OKBLUE}
        Check the items out!

        Flood System -> Able you to Flood the chat of the person you are sending message to!
                        You choose how many times I need to send the message!
        
        Scheduled -> Able you to schedule a time for me to send the message!
                     You can define the hour and minute, but you'll need to wait with me :D
        
        All done. Send it -> I'll execute!{Colors.ENDC}'''
    
    COVID_MENU = f'''{Colors.BOLD}
        The CovidBot just takes the actual stats of Coronavirus on Brazil!
        and print it on two archives: stats.txt and stats.json!
        These files are in the folder "covidStats"{Colors.ENDC}

        Are you ready to {Colors.UNDERLINE}go{Colors.ENDC} or you want to {Colors.UNDERLINE}abort{Colors.ENDC}
        If you want to see the scraping just type '{Colors.UNDERLINE}see{Colors.ENDC}'
    '''

    WEATHER_MENU = f'''{Colors.BOLD}
        1) Schedule!
        2) Change Latitude and Longitude!
        3) Change Email!
        4) Send the Forecast!
        {Colors.ENDC}
        If you want to abort the operation and get back to the menu just type '{Colors.UNDERLINE}abort{Colors.ENDC}'
        If you don't remember how any of these options works just type '{Colors.UNDERLINE}help{Colors.ENDC}'
    '''

    WEATHER_HELP = f'''{Colors.OKBLUE}
        Check the items out!

        Schedule -> Able you to schedule a time for me to send the message!
                    You can define the hour and minute, but you'll need to wait with me!

        Change Latitude and Longitude -> Able you to choose where I need to pick the Forecast information!
                                         By default, The Latitude and Longitude is on the city of Paulínia, Brazil!
        
        Change Email -> Able you to choose who I need to send the Forecast information to!
                        By default, The Email is yours! Icaro!!

        Send the Forecast -> I'll execute!{Colors.ENDC}'''
