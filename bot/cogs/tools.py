# -*- coding: utf-8 -*-
import discord, datetime, sys, os, typing, requests
from discord import client, channel, mentions, http, utils, File, FFmpegPCMAudio, Webhook
from discord.ext import commands
from asyncio import sleep, TimeoutError
from discord import NotFound, Forbidden, app_commands
from discord.app_commands import Choice
import time as dt
import locale
from config import settings
import psutil

bot_color = discord.Color.from_rgb({settings["theme"]})

def is_shutted_down(interaction: discord.Interaction):
    return interaction.command.name not in shutted_down

class Tools(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.client.user or message.author.id in blacklist:
            return

        if message.channel.id == settings['github_channel']:
            await sleep(10) # Задержка, чтобы можно было успеть удалить сообщение.
            try:
                await message.publish()
            except:
                pass

        hello_list = "Привет","привет","Эй халоп","эй халоп","Hi","hi","Hello","hello"

        if message.content.startswith(hello_list):
            if not message.author.bot:
                await message.channel.send(f'Привет {message.author.name}!')
        
        if message.author.id == 963819843142946846: # Триггер на сообщения мониторинга.
            await sleep(3)
            if message.content == "mad.debug ping":
                await message.channel.send(int(round(self.client.latency, 3)*1000))
            if message.content == "mad.debug status":
                await message.channel.send("OK")

        if message.content.startswith(f"<@{settings['github_channel']}>"):
            await message.channel.send(f"Мой префикс `{settings['prefix']}`")

        await self.client.process_commands(message)

    @app_commands.command()
    async def version(self, interaction: discord.Interaction, ver: Choice[str] = None):
        global lastcommand
        if interaction.user.id in blacklist:
            embed=discord.Embed(title="Вы занесены в чёрный список бота!", color=discord.Color.red(), description=f"Владелец бота занёс вас в чёрный список бота! Если вы считаете, что это ошибка, обратитесь в поддержку: {settings['support_invite']}", timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=interaction.user.avatar.url)
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        lastcommand = "`/version`"
        embed = None
        if ver != None:
            ver = ver.name
        if ver == None or ver == '1.0.1':
            updated_at = datetime.datetime(2022, 5, 17, 20, 0, 0, 0)
            embed=discord.Embed(title=f'Версия `{settings["curr_version"]}`', color=discord.Color.orange(), timestamp=updated_at, description=f'> 1) Требование права на просмотр журнала аудита в `/getaudit`.\n> 2) Показ кол-во участников в сети в `/serverinfo`.\n> 3) Изменение вида `/serverinfo`.\n> 4) Добавление Select Menu в `/userinfo` и `/serverinfo`.\n> 5) Команды могут быть отключены владельцем бота.\n> 6) Добавлено новое развлечение: `/doors`.\n> 7) Использование кнопок и форм вместо реакций и сообщений.\n> 8) Добавлена команда `/weather`.\n> 9) Иногда, бот будет показывать свою версию в статусе.\n> 10) Добавлена команда `/ball`.\n> 11) Обновлен дизайн `/botinfo` и `/help`.')
        if ver == '1.0.0':
            updated_at = datetime.datetime(2022, 2, 17, 9, 0, 0, 0)
            embed=discord.Embed(title="Версия `0.3.6 [ОБТ]`", color=discord.Color.orange(), timestamp=updated_at, description=f'> 1) Добавлены таймштампы в `/serverinfo` и `/userinfo`.\n> 2) Добавлено поле "Присоединился" в `/userinfo`.\n> 3) Теперь видно, когда бот перезапускается в его статусе.\n> 4) Изменена аватарка.\n> 5) Изменен порядок аргументов по умолчанию в `/clearfrom`.\n> 6) Добавлена "Защита от дурака" в `/avatar` при вводе параметра `size`.\n> 7) Добавлено поле "Кол-во участников" в `/botinfo`.')
            embed.set_footer(text="Обновлено:")
        await interaction.response.send_message(embed=embed)

class Help_1(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label="Основное", description = "Список основных команд", emoji = '📋', value="value1"),
            discord.SelectOption(label="Экономика", description = "Команды для экономики", emoji = '💰', value="value2"),
            discord.SelectOption(label="Модерация", description = "Команды модерации", emoji = '🛂', value="value3"),
            discord.SelectOption(label="Музыка", description = "Музыкальные команды", emoji = '🎵', value = "value4"),
            discord.SelectOption(label="Развлечения", description = "Мини-игры и т. п.", emoji = '🎲', value="value5"),
            discord.SelectOption(label="Реакции", description="Различные реакции/эмоции", emoji="😀", value="value6"),
            discord.SelectOption(label="Утилиты", description = "Утилиты(мини приложения) бота", emoji = '💾', value="value7"),
            discord.SelectOption(label= "Настройки", description = "Только для администрации", emoji = '⚙', value = "value8"),
        ]

        super().__init__(placeholder='Помощь', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        icon = str(interaction.guild.icon.url)
        if self.values[0] == "value1":
            embed = discord.Embed(title="Основные команды 📋", description=f"`{settings["prefix"]}time` - узнать время\n`{settings["prefix"]}avatar` - получить аватарку\n`{settings["prefix"]}say` - сказать от имени бота\n`{settings["prefix"]}voting` - начать голосование\n`{settings["prefix"]}ball` - магический шар\n`{settings["prefix"]}gay` - тест на гея", color=bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif self.values[0] == "value2":
            embed = discord.Embed(title="Экономика 💰", description=f'`{settings["prefix"]}balance` - посмотреть баланс\n`{settings["prefix"]}profile` - посмотреть профиль\n`{settings["prefix"]}deposit` - положить депозит в банк\n`{settings["prefix"]}withdraw` - забрать депозит с банка\n`{settings["prefix"]}pay` перевести деньги пользователю\n`{settings["prefix"]}work` - работать\n`{settings["prefix"]}shop` - открыть магазин\n`{settings["prefix"]}add_shop` - добавить в магазин\n`{settings["prefix"]}remove_shop` - убрать из магазина', colour = bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        if self.values[0] == "value3":
            embed = discord.Embed(title="Модерация 🛂", description=f'`{settings["prefix"]}clear` - очистка сообщений\n`{settings["prefix"]}mute` - заглушить пользователя\n`{settings["prefix"]}unmute` - размутить пользователя\n`{settings["prefix"]}kick` - выгнать пользователя\n`{settings["prefix"]}ban` - забанить пользователя\n`{settings["prefix"]}niсk` - сменить ник пользователю\n`{settings["prefix"]}create` - создать', colour = bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif self.values[0] == "value4":
            embed = discord.Embed(title="Музыка 🎵 (BETA)", description=f'`{settings["prefix"]}join` - пригласить бота к голосовому чату\n`{settings["prefix"]}leave` - выгнать бота из голосового чата\n`{settings["prefix"]}play` - начать проигрывание\n`{settings["prefix"]}pause` - поставить на паузу\n`{settings["prefix"]}resume` - возобновить произведение\n`{settings["prefix"]}stop` - остановить проигрывание и выгнать бота', colour = bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        if self.values[0] == "value5":
            embed = discord.Embed(title="Развлечения 🎲", description=f'`{settings["prefix"]}achievement` - создать очивку\n`{settings["prefix"]}joke` - Анекдоты\n`{settings["prefix"]}ball` - магический шар\n`{settings["prefix"]}gay` - тест на гея\n`{settings["prefix"]}love` - измеритель любви\n`{settings["prefix"]}fake` - фейк\n`{settings["prefix"]}cube` - подкинуть игральную кость\n`{settings["prefix"]}draw` - рисование\n**🎮 Мини-игры**\n`{settings["prefix"]}tictactoe` - крестики нолики\n`{bot_prefix}casino` - казино', colour = bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif self.values[0] == "value6":
            embed = discord.Embed(title="Реакции/Эмоции 😀", description=f'`{settings["prefix"]}bite` - укусить\n`{settings["prefix"]}caress` - ласкать\n`{settings["prefix"]}confuse` - засмущаться\n`{settings["prefix"]}cry` - плакать\n`{settings["prefix"]}dance` - танцевать\n`{settings["prefix"]}suicide` - суицид\n`{settings["prefix"]}dead_inside` - 1000-7 я умер прости...\n`{settings["prefix"]}drink` - пить\n`{settings["prefix"]}eat` - кушать\n`{settings["prefix"]}false` - отказать\n`{settings["prefix"]}hit` - ударить\n`{settings["prefix"]}hug` - обнять\n`{settings["prefix"]}joy` - радоваться\n`{settings["prefix"]}kiss` - поцеловаться\n`{settings["prefix"]}laugh` - смеяться\n`{settings["prefix"]}lick` - лизать\n`{settings["prefix"]}lover` - признаться в любви\n`{settings["prefix"]}miss` - скучать\n`{settings["prefix"]}pat` - погладить\n`{settings["prefix"]}poke` - тыкнуть\n`{settings["prefix"]}rap` - вызвать на рэп батл\n`{settings["prefix"]}resurrected` - восреснуть\n`{settings["prefix"]}run` - бежать\n`{settings["prefix"]}sad` - грустить\n`{settings["prefix"]}sex` - выебать\n`{settings["prefix"]}shock` - шок\n`{settings["prefix"]}shot` - выстрельнуть\n`{settings["prefix"]}slap` - пощечина\n`{settings["prefix"]}slit` - щелбан\n`{settings["prefix"]}sleep` - спать\n`{settings["prefix"]}smoke` - курить\n`{settings["prefix"]}true` - cогласится\n', colour = bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        if self.values[0] == "value7":
            embed = discord.Embed(title="Утилиты 💾", description=f"`{settings["prefix"]}anime` - поиск аниме\n`{settings["prefix"]}ticket` - тикеты\n`{settings["prefix"]}giveaway` - розыгрыш\n`{settings["prefix"]}timer` - таймер\n`{settings["prefix"]}random` - рандомное число\n`{settings["prefix"]}info` - получить информацию\n`{settings["prefix"]}qrcode` - сделать QRcode\n`{settings["prefix"]}base64` - декодер base64\n`{settings["prefix"]}emoji` - инфо о эмодзи\n`{settings["prefix"]}eagle-tails` - орёл и решка\n**:chains: Акаунты**\n`{settings["prefix"]}wot_blitz` - посмотреть статистику акаунта WoTb", color=bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        elif self.values[0] == "value8":
            embed = discord.Embed(title="Настройки ⚙", description=f"`{settings["prefix"]}prefix` - поменять префикс боту\n`{settings["prefix"]}language` - сменить язык бота", color=bot_color)
            embed.set_thumbnail(url=icon)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, ephemeral=True)

class Help_2(discord.ui.Select):
    def __init__(self):

        options = [
            #discord.SelectOption(label="Бот завис", description = "Ему пизда", emoji = '⚠', value="value_1"),
            discord.SelectOption(label="У меня есть вопросы", description = "Связатся с поддержкой", emoji = '⁉', value="value_2"),
            discord.SelectOption(label="Я нашёл ошибку", description = "Расскажите об найденных ошибках", emoji = '⚠', value="value_3"),
            discord.SelectOption(label="Ваш бот помойка", description = "Оставть негативный отзыв", emoji = '🤡', value="value_4"),
        ]

        super().__init__(placeholder='Обратная связь', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
      #      if interaction.values[0] == "value_1":
      #          embed = discord.Embed(title="Утилиты", description=f"", color=bot_color)
      #          await interaction.send(embed=embed)

        if self.values[0] == "value_2":
            embed = discord.Embed(title="Обратная связь ⁉", description="Нажми на кнопку ниже что бы попасть на севрер поддержки", color=bot_color)
            view = discord.ui.View()
            button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Поддержка", url=settings["support_server"], emoji="<:icon_info:973689785002651758>")
            view.add_item(item=button)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{interaction.user.name} \u200b')
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        elif self.values[0] == "value_4":
            embed = discord.Embed(title="Плохой отзыв 🤡", description=f"Ебало офни школьник ебаный <a:clown:969231366984192050>", color=bot_color)
            await interaction.response.send_message(embed=embed, ephemeral=True)

class DropdownView_Help(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Help_1())
        self.add_item(Help_2())



@app_commands.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title="Информация", description=f'Привет я Arona мой префикс `{settings["prefix"]}`. Спасибо что добавили меня на этот сервер.\nЧто бы получить помощь по конкретной команде напиши `{settings["prefix"]}help [название]`\n\n<:status_offline:973548082111336458> - Бот отключён\n<:status_online:973547805069180948> - Бот перезапускается\n<:status_online_mobile:974001909381881916>, <:status_idle:973547681337184356>, <:status_streaming:973547511774056448> - Бот успешно работает\n<:status_dnd:973547976142258237> - Бот на тех-обслуживании (лучьше его не трогать)\n\n Основные команды\n`{settings["prefix"]}help` - получить помощь\n`{settings["prefix"]}news` - последние новости в изменениях бота\n`{settings["prefix"]}prefix` - смена префикса\n\n Статистика: ```md\n#Колчиество севреров обслуживаемых ботом: '+ str(len(client.guilds)) +'\n#Колчиество человек обслуживаемых ботом: '+ str(len(client.users)) +f'\n#Пинг: {round (client.latency * 1000)} ms\n```', color = bot_color)#{round (client.latency * 1000)}
    embed.set_thumbnail(url = ctx.guild.icon.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    async with ctx.typing():
        await asyncio.sleep(2)
    view = DropdownView_Help()
    await ctx.reply(embed=embed, view=view)

@help.command(aliases=["information"])
async def info(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}info", description=f"Получить информацию.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `information`\nВремя перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}info <type>`", inline=False)
    embed.add_field(name="Пример №1", value=f"`info bot`\n Информация о боте `{bot_owner}`.", inline=False)
    embed.add_field(name="Пример №2", value=f"`info server`\n Информация о сервере.", inline=False)
    embed.add_field(name="Пример №3", value=f"`info user`\n Информация участника сервера.", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["picture"])
async def avatar(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}avatar", description=f"Получить информацию.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `picture`\nВремя перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}info <type>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Не заданы")
    embed.add_field(name="Необходимые права для участника", value=f"— Не заданы")
    embed.add_field(name="Пример №1", value=f"`avatar user`\n Аватар участника сервера.", inline=False)
    embed.add_field(name="Пример №2", value=f"`avatar server`\n Аватарка этого сервера сервера.", inline=False)
    embed.add_field(name="Пример №3", value=f"`avatar bot`\n Аватарка бота `{bot_owner}`.", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["clean", "purge", "nuke"])
async def clear(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}purge", description=f"Очистить сообщения в чате.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `clean, clear, nuke`\nВремя перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}purge <filter> [argument] <amount>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Управлять сообщениями")
    embed.add_field(name="Необходимые права для участника", value=f"— Управлять сообщениями")
    embed.add_field(name="Пример №1", value=f"`purge all 100`\nОчистит 100 возможных сообщений в канале.", inline=False)
    #embed.add_field(name="Пример №2", value=f"`purge between 917494188889755649 917493675683098635`\nНачнет очистку от сообщения 917494188889755649 и закончит 917493675683098635", inline=False)
    #embed.add_field(name="Пример №3", value=f"`purge user 100 @{bot_owner}`\nОчистит 100 возможных сообщений в канале от участника {bot_owner}.", inline=False)
    #embed.add_field(name="Пример №4", value=f"`purge images 100`\nОчистит 100 возможных сообщений с фильтрацией вложения.", inline=False)
    #embed.add_field(name="Пример №5", value=f"`purge emojis 100`\nОчистит 100 возможных сообщений с фильтрацией эмодзи.", inline=False)
    embed.add_field(name=":warning: Модерация", value=f"Это команда модерации, доступная участникам сервера при определенных условиях.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["make"])
async def create(ctx):
    embed = discord.Embed(title=f'Команда {settings["prefix"]}create', description=f' Cоздать чат.', color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `make`\n Время перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}create <type> [name]`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Управлять каналами")
    embed.add_field(name="Необходимые права для участника", value=f"— Управлять каналами")
    embed.add_field(name="Пример №1", value=f'`create text Курлык-Курлык`\n Создаст текстовый чат с названием "Курлык-Курлык".', inline=False)
    embed.add_field(name="Пример №2", value=f'`create voice Общий`\n Создаст голосовой чат с названием "Общий".', inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["фейк", "unreal", "tin"])
async def fake(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}fake", description=f"Получить фейк.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `unreal, tin`\n Время перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}fake <type>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Не заданы")
    embed.add_field(name="Необходимые права для участника", value=f"— Не заданы")
    embed.add_field(name="Пример №1", value=f"`fake personality`\n Фейковая личности.", inline=False)
    embed.add_field(name="Пример №2", value=f"`fake card`\n Фейковая кредитная карта.", inline=False)
    embed.add_field(name="Пример №3", value=f"`fake nitro`\n Фейковое нитро.", inline=False)
    embed.add_field(name="Пример №4", value=f"`fake boost`\n Фейковый буст сервера.", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["paint", "palette"])
async def darw(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}darw", description=f"Рисовать картинки.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `paint, palette`\n Время перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}darw <color>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Не заданы")
    embed.add_field(name="Необходимые права для участника", value=f"— Не заданы")
    embed.add_field(name="Пример №1", value=f"`darw orange`\n оранжевый цвет [`🟧`].", inline=False)
    embed.add_field(name="Пример №2", value=f"`darw red`\n красный цвет [`🟥`].", inline=False)
    embed.add_field(name="Пример №3", value=f"`darw blue`\n синий цвет [`🟦`].", inline=False)
    embed.add_field(name="Пример №4", value=f"`darw green`\n зелёный цвет [`🟩`].", inline=False)
    embed.add_field(name="Пример №4", value=f"`darw white`\n белый цвет [`⬜`].", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["декодер"])
async def decoder(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}decoder", description=f"Декодер.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `Не заданы`\nВремя перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}decoder <type>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Не заданы")
    embed.add_field(name="Необходимые права для участника", value=f"— Не заданы")
    embed.add_field(name="Пример №1", value=f"`decoder base64`\n Декодировка base64.", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["кодер"])
async def coder(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}coder", description=f"Кодер.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `Не заданы`\n Время перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}coder <type>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Не заданы")
    embed.add_field(name="Необходимые права для участника", value=f"— Не заданы")
    embed.add_field(name="Пример №1", value=f"`coder base64`\n Декодировка base64.", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["билет"])
async def ticket(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}ticket", description=f"Ticket.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `Не заданы`\n Время перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}ticket <type>`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Упровление каналами")
    embed.add_field(name="Необходимые права для участника", value=f"— Не заданы")
    embed.add_field(name="Пример №1", value=f"`ticket create`\n Создание тикета.", inline=False)
    embed.add_field(name="Пример №1", value=f"`ticket close`\n Закрытие тикета.", inline=False)
    embed.add_field(name="<:icon_info:973689785002651758> Общая", value=f"Это команда общая, её может использовать каждый участник сервера.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@help.command(aliases=["розыгрыш"])
async def giveaway(ctx):
    embed = discord.Embed(title=f"Команда {settings["prefix"]}giveaway", description=f"Розыгрыш.", color = bot_color)
    embed.add_field(name="Основная информация", value=f"Псевдонимы: `Не заданы`\n Время перезарядки: `5 секунд`\n Использование: `{settings["prefix"]}giveaway <time> [prize]`", inline=False)
    embed.add_field(name="Необходимые права для бота", value=f"— Добавлять реакции")
    embed.add_field(name="Необходимые права для участника", value=f"— Управление сервером")
    embed.add_field(name="Пример №1", value=f"`giveaway 10m`\n Начать розыгрыш.", inline=False)
    embed.add_field(name=":warning: Модерация", value=f"Это команда модерации, доступная участникам сервера при определенных условиях.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.reply(embed=embed)

@app_commands.group(invoke_without_command = True, aliases=["information"])
async def info(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип информации не указан. Пожалуйста, вызовить команду помощи (`{settings["prefix"]}help info`)")

@info.command()
async def bot(ctx: commands.Context):
    #battery = psutil.sensors_battery()
    #percentbat = int(battery.percent)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    percentmem = int(mem.percent)

    embed = discord.Embed(
        color = bot_color,
        title=f"Информация о {settings["bot_name"]}",
        description=f"Последняя актульная информация о {settings["bot_name"]} представлена ниже",
        )
    embed.add_field(name="Основная информация:", value=f"Создатель:\n`{settings["owner"]}`\n Версия: `{settings["curr_version"]}`\nЯП: `Python`")
    embed.add_field(name="Система:", value=f"Пинг: `{round (client.latency * 1000)}` ms\n Система:\n`Windows 10`\nCPU: `{cpu}%`\n Память: `{percentmem}%`")
    embed.add_field(name="Статисктика:", value="Серверов: `"+ str(len(client.guilds))+"`\n Пользователей:\n`"+ str(len(client.users)) +"`")
    #embed.add_field(name="Сервер поддержки:", value=f"[Сервер поддержки]({bot_support})")
    #embed.add_field(name="Добавь бота на сервер:", value=f"[Добавь бота на сервер]({bot_add})")
    embed.set_thumbnail(url = client.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)
    
@info.command()
@commands.guild_only()
async def server(ctx):
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    #create_time = (ctx.guild.created_at.strftime(date_format))
    epoch_created_at = int(dt.mktime(ctx.guild.created_at.timetuple()))
    id = str(ctx.guild.id)
    #region = str(ctx.guild_region)
    memberCount = str(ctx.guild.member_count)

    textCount = len(ctx.guild.text_channels)
    voiceCount = len(ctx.guild.voice_channels)
    channelsCount = len(ctx.guild.text_channels + ctx.guild.voice_channels)

    icon = str(ctx.guild.icon.url)

    embed = discord.Embed(
        title=name,
        description=description,
        color=bot_color
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Создатель:", value=owner, inline=True)
    embed.add_field(name="Создан:", value=f"<t:{epoch_created_at}>(<t:{epoch_created_at}:R>)", inline=True)
    embed.add_field(name="ID сервера:", value=id, inline=True)
    #embed.add_field(name="Регион сервера:", value=region, inline=True)
    embed.add_field(name="Уастников:", value=memberCount, inline=True)
    embed.add_field(name="Текстовых чатов:", value=textCount, inline=True)
    embed.add_field(name="Голосовых чатов:", value=voiceCount, inline=True)
    embed.add_field(name="Всего чатов:", value=channelsCount, inline=True)
    if ctx.guild.banner:
        embed.add_image(url=ctx.guild.banner.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)
    
@info.command()
async def user(ctx, *, user: discord.Member = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    embed = discord.Embed(color=bot_color)
    embed.set_thumbnail(url=user.avatar.url)#name=str(user),
    t = user.status
    if t == discord.Status.online:
        d = "<:status_online:973547805069180948> В сети"

    t = user.status
    if t == discord.Status.offline:
        d = "<:status_offline:973548082111336458> Не в сети"

    t = user.status
    if t == discord.Status.idle:
        d = "<:status_idle:973547681337184356> Не активен"

    t = user.status
    if t == discord.Status.dnd:
        d = "<:status_dnd:973547976142258237>  Не беспокоить"
    embed.add_field(name="Активность:", value=d)
    embed.add_field(name="Статус:", value=user.activity)
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Позиция", value=str(members.index(user)+1))
    epoch_joined_at = int(dt.mktime(user.joined_at.timetuple()))
    epoch_created_at = int(dt.mktime(user.created_at.timetuple()))
    embed.add_field(name="Присоединился", value=f"<t:{epoch_joined_at}>(<t:{epoch_joined_at}:R>)")
    embed.add_field(name="Зарегистрирован", value=f"<t:{epoch_created_at}>(<t:{epoch_created_at}:R>)")
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Роли [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Разрешения на сервере", value=perm_string, inline=False)
    #embed.set_image(user.banner_url)
    embed.timestamp = datetime.datetime.utcnow()
    if user.banner:
        member = await client.fetch_user(user.id)
        banner_url = member.banner.url
        embed.set_image(url=banner_url)
    embed.set_footer(text='ID: ' + str(user.id) + f'\n\n{ctx.author.name} \u200b')
    return await ctx.reply(embed=embed)



async def setup(client):
    await client.add_cog(Tools(client))
    print('Cog "Tools" запущен!')
