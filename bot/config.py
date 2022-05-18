"""
Настройки бота, указывайте всё как нужно, если вы что-то не укажите или укажите не правельно бот или его функции не будут корректно работать!
"""

import discord, time

settings = {
    'bot_name': 'Arona', # Сюда пишите желаемый ник вашего бота
    'token': 'T1PA_TUt-TokeN-1233312', # Сюда впишите ваш TOKEN Discord Developers
    'app_id': 123455678910111213, # Сюда впишите APPLICATION ID с Discord Developers
    'client_id': 123455678910111213, # Сюда впишите CLIENT ID с Discord Developers
    'perm_scope': 1375060978903, # Permission Integer.
    'prefix': '!', # Сюда впишите префикс который будет в вашем боте
    'openweathermap_api_key': 'Ключ openweathermap.org', # Сюда введите API ключ с сайта openweathermap.org
    'owner': '', # Сюда введите ваш ник Disord с тэгом
    'owner_id': '', # Сюда введите ваш префикс
    'server_logs': '', # Сюда укажите ID сервера с логами бота
    'channel_logs': '', # Сюда укажите ID чата с логами бота
    'outages': '',
    'github_channel': '',
    'idea_channel': '', # Сюда укажите ID чата с идеями для бота
    'curr_version': '1.0.0', # Тут указана версия бота
    'support_server': 'https://discord.gg/udycpczJWE', # Сюда укажите сервер поддержки вашего бота
    'support_site': '', # Сюда укажите сайт вашего бота
    'invite': '', # Сюда впишите ссылку приглашения вашего бота
    'coin': '', # Сюда укажите смайлик валюты бота
    'date_format': '%a, %d %b %Y %I:%M %p', # Тут формат даты. Ничего не изменять
    'theme': '' # Сюда впишите цветовую(только RGB) тему вашего бота
}

started_at = int( # Время запуска бота. Не изменять
    time.mktime(
        discord.utils.utcnow().timetuple()
    ) + 10800
) 
lastcommand = "Ещё ни разу команды не использовались."
used_commands = 0 # Счетчик использованных команд. Не трогать

blacklist = [ # ID сервера/участника, который в ЧС бота
    
]
supports = [ # ID сотрудников поддержки
    
]
verified = [ # ID верифицированных серверов/участников
    
]
beta_testers = [ # ID серверов, учавствующих в бета-тесте
    
]
bug_hunters = [ # ID баг-хантеров
    
]
bug_terminators = [ # ID баг-терминаторов
    
]
