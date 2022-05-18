"""
Настройки
"""

import discord, time

settings = {
    'bot_name': 'Arona',
    'token': 'ODMxODAzMTE2MDcxOTQ0MjEy.YHajBQ.nQEishYYihfRVj9zrDFDItulmBo',
    'app_id': 831803116071944212,
    'client_id': 831803116071944212,
    'perm_scope': 1375060978903, # Permission Integer.
    'prefix': 'a!',
    'key': 'Ключ some-random-api.md',
    'openweathermap_api_key': 'Ключ openweathermap.org',
    'owner': 'Ukraine Femboy#0001',
    'owner_id': '',
    'server_logs': '',
    'channel_logs': '',
    'outages': '',
    'github_channel': '',
    'idea_channel': '',
    'curr_version': '1.0.0',
    'support_server': 'https://discord.gg/udycpczJWE',
    'support_site': 'https://artur-orlik.gitbook.io/untitled/',
    'invite': 'https://discord.com/api/oauth2/authorize?client_id=831803116071944212&permissions=8&scope=bot%20applications.commands',
    'coin': '<a:neko_coin:960227763309129738>',
    'date_format': '%a, %d %b %Y %I:%M %p',
    'theme': '48,52,52'
}

started_at = int( # Время запуска бота. Не изменять.
    time.mktime(
        discord.utils.utcnow().timetuple()
    ) + 10800
) 
lastcommand = "Ещё ни разу команды не использовались."
used_commands = 0 # Счетчик использованных команд. Не трогать.

blacklist = [ # ID сервера/участника, который в ЧС бота.
    
]
supports = [ # ID сотрудников поддержки.
    
]
verified = [ # ID верифицированных серверов/участников.
    
]
beta_testers = [ # ID серверов, учавствующих в бета-тесте.
    
]
bug_hunters = [ # ID баг-хантеров.
    
]
bug_terminators = [ # ID баг-терминаторов.
    
]
testserver = [ # Тестовые сервера в формате discord.Object(id=ID).
     
]
shutted_down = [ # Названия слеш-команд, которые должны быть отключены.

]
