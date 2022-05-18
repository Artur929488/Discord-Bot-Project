# -*- coding: utf-8 -*-
from ast import Lambda, alias
from cgitb import text
from dis import disco
from io import BytesIO
import json
from multiprocessing import Event
from pydoc import cli, describe
from sqlite3.dbapi2 import Connection, Cursor, connect
from tabnanny import check
from turtle import color, title
from types import MemberDescriptorType
from unicodedata import name 
from unittest import async_case
from urllib import response
from xml.dom.minicompat import EmptyNodeList
import discord
from discord import client, channel, mentions, http, utils, File, FFmpegPCMAudio, Webhook
from discord.colour import Color
from discord.ext import commands
import os, sqlite3
import string
from PIL import Image, ImageDraw, ImageFont, ImageChops
import io
import asyncio
import datetime
import time as dt
from discord.ext.commands import bot as bo
from discord.ext.commands.core import command
from discord.flags import Intents
from discord.utils import get
from discord.gateway import DiscordWebSocket
import animec
import random
from youtube_dl import YoutubeDL
from asyncio import sleep
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
import httpx
from bs4 import BeautifulSoup
from functools import partial
import itertools   
import numpy as np
import operator
import aiohttp
import sys
from pymongo import MongoClient
from config import settings
from tabulate import tabulate
from Cybernator import Paginator as pag
import requests
from typing import Optional
from easy_pil import Editor, load_image_async, Font
import spotdl
from math import pi, tau, e, sqrt
from TagScriptEngine import Interpreter, block
import locale
from faker import Faker
import re
import qrcode as qr 
import base64 as bas64
from sty import fg, bg, ef, rs
import threading
import akinator as Akinator
import uuid
from discord.ext.commands import cooldown, BucketType
import psutil
import traceback
from dotenv import load_dotenv
import subprocess
from pypresence import Presence

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

intents = discord.Intents.default()
intents.presences = True
intents.members = True 
intents.message_content = True

client = commands.Bot( command_prefix = settings['prefix'], intents=intents )
client.remove_command( 'help' )

#------------------------------------------------------------------------------------------------------------- 
#-------------------------------------------------------------------------------------------------------------

bot_name=settings['bot_name']
bot_version=settings['curr_version']
bot_prefix=settings['prefix']
bot_owner=settings['owner']
bot_color=discord.Color.from_rgb(settings['theme'])
bot_lang='`RU` :flag_ru:'
bot_site=settings['support_site']
bot_support=settings['support_server']
bot_add=settings['invite']
year='2022'
bot_coin=settings['coin']
date_format=settings['date_format']

ы="ы"
ё="ё"
ъ="ъ"

#------------------------------------------------------------------------------------------------------------- 
#-------------------------------------------------erorr-------------------------------------------------------

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(title="Ошибка: У бота отсутствуют разрешения", description="У бота не достаточно прав для этой команды! Обратитесь к администрации сервера что бы боту выдали права.", colour=discord.Color.red())
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed, delete_after=15)
        await ctx.message.add_reaction('⚠')
    if isinstance(error, commands.CommandNotFound):
        embed2 = discord.Embed(title="Ошибка: Команда не найдена", description="Проверте написали ли вы команду правильно и есть ли она в боте.", colour=discord.Color.red())
        embed2.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed2.timestamp = datetime.datetime.utcnow()
        embed2.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed2, delete_after=15)
        await ctx.message.add_reaction('❌')
    if isinstance(error, commands.MissingPermissions):
        embed3 = discord.Embed(title="Ошибка: У вас нет прав", description="У вас не достаточно прав для использования данной команды.", colour=discord.Color.red())
        embed3.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed3.timestamp = datetime.datetime.utcnow()
        embed3.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed3, delete_after=15)
        await ctx.message.add_reaction('🚫')
    if isinstance(error, commands.NSFWChannelRequired):
        embed3 = discord.Embed(title='Ошибка: Только для чатов "NSFW"', description='Команда может использоватся только в чатах с отметкой "NSFW".', colour=discord.Color.red())
        embed3.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed3.timestamp = datetime.datetime.utcnow()
        embed3.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed3, delete_after=15)
        await ctx.message.add_reaction('🔞')

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.event
async def on_guild_join(guild):
    if guild.system_channel is not None:
        embed = discord.Embed(title='Приветствую!', description=f'**Привет! Я {bot_name} бот для твоего сервера!**\n\nНе много о себе:\n-Мой префикс: `{bot_prefix}`\n-Мой создатель: `{bot_owner}`\n-Мой язык: {bot_lang}\n-Язык на котором я написан: `Python`\n-Моя версия: `{bot_version}`', color=bot_color)
        embed.set_thumbnail(url=client.user.avatar.url)
        embed_link = discord.Embed(title='Сервер поддержки!', description=f'Сервер поддержки {bot_name} в Discord\n[{bot_name} Bot | Support]({bot_support})', color=discord.Color.from_rgb(86,97,246))
        embed_link.set_thumbnail(url="https://play-lh.googleusercontent.com/Wvjx6rVlC1rGWKkln3r-23ICKV--sxEEUuq7jd15BeJan8v-wS7TGwm0NHXqqon18w")
        await guild.system_channel.send(embed=embed)
        await guild.system_channel.send(embed=embed_link)
    elif guild.system_channel is None:
        user = client.get_user(guild.owner.id)
        embed = discord.Embed(title='Приветствую!', description=f'**Привет! Я {bot_name} бот для твоего сервера!**\n\nНе много о себе:\n-Мой префикс: `{bot_prefix}`\n-Мой создатель: `{bot_owner}`\n-Мой язык: {bot_lang}\n-Язык на котором я написан: `Python`\n-Моя версия: `{bot_version}`', color=bot_color)
        embed.set_thumbnail(url=client.user.avatar.url)
        embed_link = discord.Embed(title='Сервер поддержки!', description=f'Сервер поддержки {bot_name} в Discord\n[{bot_name} Bot | Support]({bot_support})', color=discord.Color.from_rgb(86,97,246))
        embed_link.set_thumbnail(url="https://play-lh.googleusercontent.com/Wvjx6rVlC1rGWKkln3r-23ICKV--sxEEUuq7jd15BeJan8v-wS7TGwm0NHXqqon18w")
        await user.send(embed=embed)
        await user.send(embed=embed_link)

#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------последние-новости-бота----------------------------------------------

@client.command()
async def news(ctx):
    embed = discord.Embed(title=f"Последние новости {bot_name}", description="Последние новости изменений Mayuko\n\n**:mailbox_with_mail: Новости**\n", color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)
  
#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------------приглосить-бота-----------------------------------------------

@client.command()
async def invite(ctx):
    embed = discord.Embed(title=f"Пригласить {bot_name} на свой сервер", description=f"Нажми на кнопку ниже что бы добавить бота на свой сервер.", color  = bot_color)
    view = discord.ui.View()
    button = discord.ui.Button(style=discord.ButtonStyle.grey, label="Добавь бота на сервер", url=bot_add, emoji="<:icon_link:969231366329864192>")
    view.add_item(item=button)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed, view=view)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------инфо--------------------------------------------------------

@client.group(invoke_without_command = True, aliases=["information"])
async def info(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип информации не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help info`)")

#----------------------------------------------инфо-о-боте----------------------------------------------------

@info.command()
async def bot(ctx: commands.Context):
    #battery = psutil.sensors_battery()
    #percentbat = int(battery.percent)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    percentmem = int(mem.percent)

    embed = discord.Embed(
        color = bot_color,
        title=f"Информация о {bot_name}",
        description=f"Последняя актульная информация о {bot_name} представлена ниже",
        )
    embed.add_field(name="Основная информация:", value=f"Создатель:\n`{bot_owner}`\n Версия: `{bot_version}`\nЯП: `Python`")
    embed.add_field(name="Система:", value=f"Пинг: `{round (client.latency * 1000)}` ms\n Система:\n`Windows 10`\nCPU: `{cpu}%`\n Память: `{percentmem}%`")
    embed.add_field(name="Статисктика:", value="Серверов: `"+ str(len(client.guilds))+"`\n Пользователей:\n`"+ str(len(client.users)) +"`")
    #embed.add_field(name="Сервер поддержки:", value=f"[Сервер поддержки]({bot_support})")
    #embed.add_field(name="Добавь бота на сервер:", value=f"[Добавь бота на сервер]({bot_add})")
    embed.set_thumbnail(url = client.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

#---------------------------------------------инфо-о-сервере--------------------------------------------------
    
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

#--------------------------------------инфо-о-пользователе--------------------------------------------------
    
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

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------добавить-бота-на-сервер----------------------------------------------

@client.command()
async def addbot(ctx):
  embed = discord.Embed(
        color = bot_color,
        title="Добавь бота на сервер!",
        description=f"\n\n[Добавить бота на сервер]({bot_add}) ",
        )
  embed.set_thumbnail(url = client.user.avatar.url)
  embed.set_footer(text = f'{bot_owner} © {year} Все права защищены')
  await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------некдот---------------------------------------------------------

@client.command()
async def joke(ctx):
  embed = discord.Embed(
        color = 0xff9900,
        title="Команды для **анекдотов**",
        description="**<:smile:920714719873105951> Анекдоты**\n`m!buckwheat_and_cat` - Гречка и кошка\n`m!ment_and_man` - Мент и мужик",
        )
  embed.set_thumbnail(url = client.user.avatar.url)
  embed.set_footer(text = f'{bot_owner} © {year} Все права защищены')
  embinf = discord.Embed(title='`Информация о команде m!info`', description='**Описание:**\nИнформация о данном боте', color=0xff9900)
  embinf.set_thumbnail(url = client.user.avatar.url)
  await ctx.reply(embed=embed)

@client.command(pass_context=True)#Гречка и кошка
async def buckwheat_and_cat(ctx):
    embed=discord.Embed(title='Анекдот: Гречка и кошка', description='**Кошке приносят кушать. \n Понедельник. \n - Вау!!!!!!!!!!!!!!!!!!!! ГРЕЧКААААА!!!!!!!!!!!!!! \n Вторник. \n -Вау! Гречка. \n Среда. \n - Мда, гречка \n Четверг. \n -гречка? \n Пятница. \n -опять гречка \n Суббота. \n Миска пустая \n Воскресение. \n Миска пустая \n Понедельник. \n - Вау!!!!!!!!!!!!!!!!!!!! ГРЕЧКААААА!!!!!!!!!!!!!!**', colour = discord.Color.from_rgb(240, 140, 149))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    await ctx.send(embed = embed)

@client.command(pass_context=True)#Мент и мужик
async def ment_and_man(ctx):
    embed=discord.Embed(title='Анекдот: Мент и мужик', description='**Останавливает мент какого-то мужика. Тот говорит: \n - Пожалуйста, отпустите меня, я на работу опаздываю. \n - А кем вы работаете? \n - Я метатель ножей в цирке. \n - Не верю, докажите. \n Тот достает десяток ножей начинает жонглировать. \n Мимо проезжает машина с супружеской парой. Муж говорит жене: \n - Хорошо, что я пить бросил. Видела, какие теперь тесты пошли? **', colour = discord.Color.from_rgb(240, 140, 149))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def lwalpdad(ctx):
    embed=discord.Embed(title='Анекдот: Гречка', description='**! **', colour = discord.Color.from_rgb(240, 140, 149))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    await ctx.send(embed = embed)

@client.command(pass_context=True)
async def asdadsadt(ctx):
    embed=discord.Embed(title='Анекдот: Гречка', description='**! **', colour = discord.Color.from_rgb(240, 140, 149))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    await ctx.send(embed = embed)


#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=["голосование"])
async def voting(ctx, *, arg = None):
    if arg is None:
        await ctx.send('Укажите текст')
    else:
        msg = await ctx.send(embed = discord.Embed(title = f'Голосование', description = f'Голосуйте по реакциям! \n> {arg}', color=bot_color))
        await ctx.message.delete()
        await msg.add_reaction('👍') 
        await msg.add_reaction('👎')

#-------------------------------------------------------------------------------------------------------------
#--------------------------------------изминение-ника---------------------------------------------------------

@client.command()
# проверьте, есть ли у пользователя разрешение на изменение своего имени
@commands.has_permissions(change_nickname=True)
async def nick(ctx, member: discord.Member, *, nickname):
    await member.edit(nick=nickname)
    await ctx.send(f'Ник был изменен на {member.mention}.')

# сбросить никнейм, если новое имя не было дано
@nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        member = ctx.author
        await member.edit(nick=None)
        await ctx.send(f'Никнейм был сброшен на {member.mention}.')

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------онлайн----------------------------------------------------------

@client.command()
async def online(ctx):
    embed = discord.Embed( title = 'Все работает успешно!', colour = discord.Color.green() )
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')

    await ctx.send( embed = embed )

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------время-----------------------------------------------------------

@client.command( pass_context = True )
async def  time( ctx ):
    emb = discord.Embed( title = 'Ваше время:', description = 'Текущее время в вашем регионе', colour = bot_color, url = 'https://www.timeserver.ru')

    emb.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url )
    emb.set_footer( text = 'Спасибо что посмотрели время при помощи нашего бота!' )
    #emb.set_image( url = 'https://sun9-35.userapi.com/c200724/v2000714757/14f24/BL06miOGVd8.jpg' )
    emb.set_thumbnail( url = 'https://sun9-35.userapi.com/c200724/v200724757/14f24/BL06miOGVd8.jpg' )

    now_date = datetime.datetime.now()
    emb.add_field( name = 'Время', value = 'Время: {}'.format( now_date )) 

    await ctx.message.delete()
    await ctx.send( embed = emb )

#-------------------------------------------------------------------------------------------------------------
#------------------------------------сказать-от-имени-бота----------------------------------------------------

@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    try:
        await ctx.send(message)
    except:
        await ctx.send("Введите сообщение!")

@client.command()
async def embsay(ctx, *, message):#, color, gif
  await ctx.message.delete()
  embed = discord.Embed(description=message, colour = bot_color)#0x8A2BE2 !embsay werewr 0x8A2BE2 https://images-ext-1.discordapp.net/external/GYuNEswE3mP8mofMPeVg5wrKjQChZR43QBhAwh3cE5A/https/media.discordapp.net/attachments/867815327323783208/937442969806573638/36ce7f19e23442e11fc70ee146f614fc.gif
  await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------да----------------------------------------------------------------

@client.command(pass_context=True)#команда для курить
async def true(ctx):
    embed=discord.Embed(title='Реакция: принят', colour = discord.Color.green())
    true=['https://c.tenor.com/uxokb6B56XMAAAAd/papers-please.gif']
    embed.set_image(url=random.choice(true))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#------------------------------------------нет----------------------------------------------------------------

@client.command(pass_context=True)#команда для курить
async def false(ctx):
    embed=discord.Embed(title='Реакция: отказ', colour = discord.Color.red())
    false=['https://c.tenor.com/cxZ2dpPz1k0AAAAC/papers-please.gif']
    embed.set_image(url=random.choice(false))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------аватарка------------------------------------------------------------

@client.group(invoke_without_command = True, aliases=["picture"])
async def avatar(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип аватарки не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help avatar`)")
    
@avatar.command(pass_context=True, aliases=['юсер'])
async def user(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(title= 'Аватарка '+str(member), colour = bot_color)
    embed.set_image(url=member.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed=embed)

@avatar.command(pass_context=True, aliases=['сервера', 'сервер'])
async def server(ctx):
    embed = discord.Embed(title='Аватарка ', colour = bot_color)
    embed.set_image(url=ctx.guild.icon.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed=embed)

@avatar.command(pass_context=True, aliases=['бот'])
async def bot(ctx):
    embed = discord.Embed(title=f'Аватарка {bot_name}', colour = bot_color)
    embed.set_image(url=client.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#------------------------------------Команды-модерация--------------------------------------------------------

# kick
@client.command(aliases=['кик'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason):
    await ctx.channel.purge(limit = 1)
    
    embed = discord.Embed(title = 'Пользователь кикнут!', color = 0x9400D3, colour = discord.Color.red() )
    embed.add_field(name = 'Модератор / админ:', value = ctx.message.author.mention, inline = False)
    embed.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
    embed.add_field(name= 'Причина:', value = reason, inline = False)
    embed.set_thumbnail(url = 'https://c.tenor.com/ZblfUV4T1y0AAAAd/press-f-f-discord.gif')
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed = embed)
    await member.send(f'Вы кикнуты по причине "{reason}"!')
    await member.kick( reason = reason)
    #await ctx.send(f'Данный пользователь нарушил правила сервера и был забанен {member.mention }.')

@kick.error
async def clear_errorqw(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'У вас нету нужных прав для управления этой командой!', inline = False)
        embed.set_image(url = 'https://c.tenor.com/ZblfUV4T1y0AAAAd/press-f-f-discord.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указано имя пользователя', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = 'm!kick @user причина', inline = False)
        embed.set_image(url = 'https://c.tenor.com/ZblfUV4T1y0AAAAd/press-f-f-discord.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указана причина', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = 'm!kick @user причина', inline = False)
        embed.set_image(url = 'https://c.tenor.com/ZblfUV4T1y0AAAAd/press-f-f-discord.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)


# Ban
@client.command(aliases=['бан'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason):
    await ctx.channel.purge(limit = 1)
    
    embed = discord.Embed(title = 'Пользователь забанен!', color = 0x9400D3, colour = discord.Color.red() )
    embed.add_field(name = 'Модератор / админ:', value = ctx.message.author.mention, inline = False)
    embed.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
    embed.add_field(name= 'Причина:', value = reason, inline = False)
    embed.set_thumbnail(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed = embed)
    await member.send(f'Вы забанены по причине "{reason}"!')
    await member.ban( reason = reason)
    #await ctx.send(f'Данный пользователь нарушил правила сервера и был забанен {member.mention }.')

@ban.error
async def clear_errorqw(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'У вас нету нужных прав для управления этой командой!', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указано имя пользователя', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = f'{bot_prefix}ban @user причина', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указана причина', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = f'{bot_prefix}ban @user причина', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

@client.command(aliases=['разбан']) 
async def unban(ctx, *, member): 
    banned_users = await ctx.guild.bans() 
    member_name, member_discriminator = member.split('#') 
    for ban_entry in banned_users: user = ban_entry.user 
    if (user.name, user.discriminator) == (member_name, member_discriminator): 
        await ctx.guild.unban(user) 
        await ctx.channel.send(f"Unbanned: {user.mention}")

@unban.error
async def clear_errorqw(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'У вас нету нужных прав для управления этой командой!', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указано имя пользователя', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = f'{bot_prefix}unban @user', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {client.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with client.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False

@client.command(aliases=['мут'])
@commands.has_permissions(administrator = True)
async def mute( ctx, member: discord.Member, until: int):
    await ctx.channel.purge( limit = 1 )

    handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
    if handshake:

   # await member.add_roles( mute_role )
        embed = discord.Embed(title = 'Пользователь в муте!', color = 0x9400D3, colour = discord.Color.red() )
        embed.add_field(name = 'Модератор / админ:', value = ctx.message.author.mention, inline = False)
        embed.add_field(name = 'Замучен:', value = member.mention, inline = False)
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        return await ctx.send(embed=embed)

@mute.error
async def clear_errorqw(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'У вас нету нужных прав для управления этой командой!', inline = False)
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указано имя пользователя', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = f'{bot_prefix}mute @user причина', inline = False)
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указана причина', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = f'{bot_prefix}mute @user причина', inline = False)
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(administrator = True)
async def unmute( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'AC-Mute' )

    await member.remove_roles( mute_role )
    embed = discord.Embed(title = 'Снят мут!', color = 0x9400D3, colour = discord.Color.red() )
    embed.add_field(name = 'Модератор / админ:', value = ctx.message.author.mention, inline = False)
    embed.add_field(name = 'Снят мут с:', value = member.mention, inline = False)
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await member.send(f'Привет котик ты размутен :з')
    await ctx.send(embed = embed)

@unmute.error
async def clear_errorqw(ctx, error):

    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'У вас нету нужных прав для управления этой командой!', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

    if isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title = 'Ошибка!', color =0xff060e, colour = discord.Color.red() )
        embed.add_field(name = 'Причина ошибки:', value = 'Не указано имя пользователя', inline = False)
        embed.add_field(name = 'Пример использования команды:', value = f'{bot_prefix}unmute @user', inline = False)
        embed.set_image(url = 'https://c.tenor.com/TbfChfHKkOUAAAAM/ban-button.gif')
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed = embed)

@client.group(invoke_without_command = True, aliases=["clean", "purge", "nuke"])
@commands.has_permissions(manage_messages = True)
async def clear(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип очистки чата не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help clear`)")

@clear.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def all(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(title='Команда: Очистить чат :recycle:', description=f'Было очищено {limit} сообщений', colour = bot_color)
        embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.send(embed=embed)
        await ctx.message.delete()

@client.group(invoke_without_command = True, aliases=["make"])
@commands.has_permissions(manage_channels = True)
async def create(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип чата не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help create`)")

@create.command()
@commands.has_permissions(administrator = True)#
async def text(ctx, *, text_name):
    guild = ctx.guild
    await guild.create_text_channel(name=text_name)
    embed=discord.Embed(title='Команда: Создать чат', description='{}, чат создан!'.format(ctx.message.author.mention), color = bot_color)
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@create.command()
@commands.has_permissions(administrator = True)#
async def voice(ctx, *, voice_name):
    guild = ctx.guild
    await guild.create_voice_channel(name=voice_name)
    embed=discord.Embed(title='Команда: Создать голосовой чат', description='{}, голосовой чат создан!'.format(ctx.message.author.mention), color = bot_color)
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.send(embed=embed)
    await ctx.message.delete()

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------NSFW-----------------------------------------------------------


@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Рандомный мем:", description="", color = 0xff9900)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Epicentr/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)

#-------------------------------------рандомный-кот-----------------------------------------------------------

@client.command(pass_context=True)
async def cat(ctx):
    embed = discord.Embed(title="Рандомный кот:", description="", color = 0xff9900)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/cat/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)

#-------------------------------------рандомная-собака---------------------------------------------------------

@client.command(pass_context=True)
async def dog(ctx):
    embed = discord.Embed(title="Рандомная сучка:", description="", color = 0xff9900)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/DOG/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)


#------------------------------------------------------------------------------------------------------------

@client.command()
async def neko(ctx):
    embed = discord.Embed(title="Neko:", description="Рандомная кошка-девочка", color = discord.Color.from_rgb(235, 121, 106))
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/NekoGirl/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{ctx.author.name} \u200b')
            await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=['таймер'], pass_context=True)
async def timer(ctx, arg):
  tim = arg
  tim = int(tim)
  update_emb = discord.Embed(title = "Таймер", description = f"Ещё осталось: **{tim}**", color = bot_color)
  update_emb.set_image(url="https://i.gifer.com/152H.gif")
  update_emb.timestamp = datetime.datetime.utcnow()
  update_emb.set_footer(text=f'{ctx.author.name} \u200b')
  msg = await ctx.send(embed = update_emb)
  while tim > -1:
    update_emb2 = discord.Embed(title = "Таймер", description = f"Ещё осталось: **{tim}**", color = discord.Color.green())
    update_emb2.set_image(url="https://i.gifer.com/152H.gif")
    update_emb2.timestamp = datetime.datetime.utcnow()
    update_emb2.set_footer(text=f'{ctx.author.name} \u200b')
    tim = tim - 1
    await msg.edit(embed=update_emb2)
    await asyncio.sleep(1)
  if tim <= 0:
    await asyncio.sleep(5)
    #await msg.delete()

#-------------------------------------------------------------------------------------------------------------

@client.command()
@commands.is_nsfw()
async def nsfw_trap(ctx):
    trap = requests.get("https://api.waifu.pics/nsfw/trap")
    embed = discord.Embed(title='Трап:', color=bot_color)
    embed.set_image(url=trap.json()["url"])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@client.command()
@commands.is_nsfw()
async def nsfw_neko(ctx):
    neko = requests.get("https://api.waifu.pics/nsfw/neko")
    embed = discord.Embed(title='Неко:', color=bot_color)
    embed.set_image(url=neko.json()["url"])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@client.command()
@commands.is_nsfw()
async def nsfw_waifu(ctx):
    waifu = requests.get("https://api.waifu.pics/nsfw/waifu")
    embed = discord.Embed(title='Вайфу:', color=bot_color)
    embed.set_image(url=waifu.json()["url"])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@client.command()
@commands.is_nsfw()
async def nsfw_blowjob(ctx):
    blowjob = requests.get("https://api.waifu.pics/nsfw/blowjob")
    embed = discord.Embed(title='Работа ротиком:', color=bot_color)
    embed.set_image(url=blowjob.json()["url"])
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=['орёл-решка'])
async def eagle_tails(ctx):
    await ctx.send(random.choice(['орел', 'решка']))
choice = random.randint(0, 100) # случайное число от 0 до 100
if choice < 50:
   print('')
else:
   print('')

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=['шар'])
async def ball(ctx, *, question ):
    answer = random.choice(["Нет", "Да", "Скорее всего", "Скорее нет", "Скорее да", "100%", "Уверен да", "Не за что", "Некогда", "У меня дикий понос", "Не за что", "Не знаю 🤔", "Уверен нет"])
    embed = discord.Embed(title="Магический шар 🔮", color=bot_color)
    embed.add_field(name="Вопрос:", value=f"> {question}")
    embed.add_field(name="Ответ:", value=f"{answer}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=["тест-на-гея", "гей", "гей-тест"])
async def gay(ctx, member: discord.Member = None):
    if member is None:
        answer = random.randint(0, 100)
        embed = discord.Embed(title="Тест на гея :rainbow_flag:", description=f"{ctx.author.mention}, решил пройти тест на гея. Он на `{answer}%` гей!", color=bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
    else:
        answer = random.randint(0, 100)
        embed = discord.Embed(title="Тест на гея :rainbow_flag:", description=f"{ctx.author.mention}, решил запустить тест на гея для {member.mention} он на `{answer}%` гей!", color=bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

@client.command(aliases=["тест-на-транса", "транс", "транс-тест"])
async def trans(ctx, member: discord.Member = None):
    if member is None:
        answer = random.randint(0, 100)
        embed = discord.Embed(title="Тест на транса :transgender_flag:", description=f"{ctx.author.mention}, решил пройти тест на транса. Он на `{answer}%` транс!", color=bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
    else:
        answer = random.randint(0, 100)
        embed = discord.Embed(title="Тест на транса :transgender_flag:", description=f"{ctx.author.mention}, решил запустить тест на транса для {member.mention} он на `{answer}%` транс!", color=bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

@client.command(aliases=["любовь"])
async def love(ctx, member: discord.Member = None):
        love_list=[
          f"||{random.randint(1, 9)}% █                         ||",
        f"||{random.randint(10, 19)}% ██                        ||",
        f"||{random.randint(20, 29)}% ████                      ||",
        f"||{random.randint(30, 39)}% ██████                    ||",
        f"||{random.randint(40, 49)}% ████████                  ||",
        f"||{random.randint(50, 59)}% ███████████               ||",
        f"||{random.randint(60, 69)}% ██████████████            ||",
        f"||{random.randint(70, 79)}% ██████████████████        ||",
        f"||{random.randint(80, 89)}% ████████████████████      ||",
        f"||{random.randint(90, 99)}% ███████████████████████   ||",
      f"||{random.randint(100, 101)}% ██████████████████████████||",
        ]
        random_love = random.choice(love_list)
        embed = discord.Embed(title="❤ Измеритель любви ❤", description=f"💗 {ctx.author.mention}\n💗 {member.mention}\n\n{random_love}", color=bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=['random', 'рандом'])
async def rand(ctx, num1 = None, num2 = None):
    author= ctx.message.author
    avatar = author.avatar.url
    if num1 != None:
        if num2 != None:
            x = int(num1)
            y = int(num2)
            if x < y:
                value = random.randint(x,y)
                embed=discord.Embed(title='Случайное число', description=f'{author.mention}, вот ваше число: \n> **{value}**', colour = bot_color)
                embed.set_author(name=f"{author}", icon_url=f"{avatar}")
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=f'{ctx.author.name} \u200b')
                await ctx.reply(embed=embed)
            else:
                await ctx.reply("Первое число больше второго")
        else:
            await ctx.reply('Вы не ввели наибольшее число!')
    else:
        await ctx.reply('Вы не ввели наименьшее число')

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------музыка---------------------------------------------------------

load_dotenv()
players = {}

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        embed = discord.Embed(title=f'Бот присоеденился к каналу: {channel}', description=f'Напишите `{bot_prefix}leave` чтоб бот вышел из голосового канала.', colour = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
        voice = await channel.connect()

@client.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice=get(client.voice_clients,guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        embed = discord.Embed(title=f'Бот отключился от канала: {channel}', description=f'Напишите `{bot_prefix}join` чтоб бот пресоеденисля к голосовому каналу.', colour = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

# command to play sound from a youtube URL
@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        embed = discord.Embed(title=f'<a:cd:969180333092274237> Музыка', description=f'Что бы выключить трэк напишите `{bot_prefix}stop`. Что бы поставить трэк на паузу напишите `{bot_prefix}pause`.', color = bot_color)
        #embed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar.url}")
        embed.add_field(name='**Трэк:**', value=url, inline = False)
        #embed.add_field(name='**Автор:**', value='None', inline = False)
        #embed.add_field(name='**Ссылка:**', value=f'{url}', inline = False)
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/Y9ec_ju_jMFXEYbE-Ie5kPp5R5im0556dCBV7EPvn8M/https/www.youtube.com/img/desktop/yt_1200.png?width=672&height=672')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

# check if the bot is already playing
    else:
        embed = discord.Embed(title=f"<a:cd:969180333092274237> Музыка", description=f"Подождите пока текущая песня закончится или используйте команду `{bot_prefix}stop`.", colour = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        embed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar.url}")
        await ctx.send(embed=embed)
        return

# command to resume voice if it is paused
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        embed = discord.Embed(title=f'Воспроизведение трэка', description=f'{ctx.message.author.mention} воспроизводит трэк чтоб его поставить на паузу напишите `{bot_prefix}pause`.', color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.channel.reply(embed=embed)
    else:
        embed = discord.Embed(title=f'Воспроизведение трэка', description=f'Музыка уже играет! Что бы её оставновить напишите `{bot_prefix}stop`.', color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.channel.reply(embed=embed)


# command to pause voice if it is playing
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        embed = discord.Embed(title=f'Пауза', description=f'{ctx.message.author.mention} Ставит трэк на паузе чтоб его возобновить напишите `{bot_prefix}resume`.', color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.channel.reply(embed=embed)
    else:
        embed = discord.Embed(title=f'Пауза', description=f'Музыка уже на паузе чтоб его возобновить напишите `{bot_prefix}resume`.', color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.channel.reply(embed=embed)


# command to stop voice
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        embed = discord.Embed(title=f'Остановить', description=f'{ctx.message.author.mention} выключает музыку! Что бы начать проигровние музыки напишите `{bot_prefix}play ссылка`.', color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.channel.reply(embed=embed)
    else:
        embed = discord.Embed(title=f'Остановить', description=f'Сейчас ничего не играет! Что бы начать проигровние музыки напишите `{bot_prefix}play ссылка`.', color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.channel.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = ctx.author

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Настала очередь <@" + str(player1.id) + f"> что бы осуществить ход напишите `{bot_prefix}place [место]`")
        elif num == 2:
            turn = player2
            await ctx.send("Настала очередь <@" + str(player2.id) + f"> что бы осуществить ход напишите `{bot_prefix}place [место]`")
    else:
        await ctx.send("Игра уже идет! Закончите его, прежде чем начинать новую игру")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                #print(count)
                if gameOver == True:
                    await ctx.send(mark + " победил!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Ничья")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Вы выбрали не то число или это место уже занято")#Выберете число от 1 до 9 чтоб осуществить ход
        else:
            await ctx.send("Сейчас очередь другого игрока")
    else:
        await ctx.send(f"Пожалуйста, начните новую игру, используя команду `{bot_prefix}tictactoe [@user]`")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Пожалуйста, укажите игрока для игры.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Пожалуйста, не забудьте упомянуть/пинговать игроков (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Пожалуйста, введите позицию, которую вы хотите отметить.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Пожалуйста, не забудьте ввести целое число.")

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

connection = sqlite3.connect('database.db') # или :memory:
cursor = connection.cursor()
timestamp = datetime.datetime.now().strftime("%H:%M:%S")
print(f"[BOT {timestamp}] Подключение к DataBase")

@client.event
async def on_ready():
    while True:
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.competing, name=f'{bot_prefix}help'))
        await asyncio.sleep(12)
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.competing, name=f'💛💙 Україна переможе'))
        await asyncio.sleep(8)
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.competing, name=f'#CloseTheSkyUkraine'))
        await asyncio.sleep(8)
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.competing, name=f'discord.gg/udycpczJWE'))
        await asyncio.sleep(10)
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.competing, name=f'чел снизу гей ↓'))
        await asyncio.sleep(8)

async def on_ready():
    await client.change_presence(status = discord.Status.dnd)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS servers (
        guild TEXT,
        server_id INT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        id INT,
        wallet BIGINT,
        bank BIGINT,
        rep INT,
        lvl INT,
        marry INT,
        guild TEXT,
        server_id INT
    )""")
 
    cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
        role_id INT,
        id INT,
        cost BIGINT
    )""")

    for guild in client.guilds:
        for member in guild.members:
            if cursor.execute(f"SELECT server_id FROM servers WHERE server_id = {guild.id}").fetchone() is None:
                cursor.execute(f"INSERT INTO servers VALUES ('{guild}', {guild.id})")
            if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 300, 1000, 0, 1, 0, '{guild}', {guild.id})")
            else:
                pass
 
    connection.commit()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f'[BOT {timestamp}] client connected')

@client.event
async def on_member_remove(member):
    if member.guild.id == 974027749679321138:
        channel = client.get_channel(974027750069375010)
        embed = discord.Embed(title="Мы будем скучать 😥", description=f"{member.mention}, вышёл с сервера(", color=bot_color)
        await channel.send(embed=embed)

@client.event
async def on_member_join(member):
    if member.guild.id == 974027749679321138:
        channel = client.get_channel(974027750069375010)
        embed = discord.Embed(title="Добро пожаловать!", description=f"{member.mention}, прежде чем начать общение прочти <#974027749704466522>", color=bot_color)
        await channel.send(embed=embed)
async def on_member_join(member):
    if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 300, 1000, 0, 1, 0, {member.guild.id})")
        connection.commit()
    else:
        pass
 
 
@client.command(aliases = ['cash', 'bal', 'баланс'])
async def balance(ctx, member: discord.Member = None):
    if member is None:
        embed = discord.Embed(title=f'Баланс пользователя {ctx.author}', description = f""":dollar: На руках: **{cursor.execute("SELECT wallet FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} {bot_coin}**\n:credit_card: В банке: **{cursor.execute("SELECT bank FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} {bot_coin}**\n:moneybag: Всего: **{cursor.execute("SELECT wallet + bank FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} {bot_coin}**\n\nЧто бы заработать больше денег отправтесь на роботу: `{bot_prefix}work`""",color = bot_color)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
        
    else:
        embed = discord.Embed(title=f'Баланс пользователя {member}', description = f""":dollar: На руках: **{cursor.execute("SELECT wallet FROM users WHERE id = {}".format(member.id)).fetchone()[0]} {bot_coin}**\n:credit_card: В банке: **{cursor.execute("SELECT bank FROM users WHERE id = {}".format(member.id)).fetchone()[0]} {bot_coin}**\n:moneybag: Всего: **{cursor.execute("SELECT wallet + bank FROM users WHERE id = {}".format(member.id)).fetchone()[0]} {bot_coin}**""",color = bot_color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
 
@client.command(aliases = ['level', 'лвл', 'уровень'])
async def lvl(ctx, member: discord.Member = None):
    if member is None:
        embed = discord.Embed(title=f'Уровень пользователя {ctx.author}', description = f""":bar_chart: Уровень: **{cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]}**\n\n Общайся с другими что бы прокочать свой уровень""", color = bot_color)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
        
    else:
        embed = discord.Embed(title=f'Уровень пользователя {member}', description = f""":bar_chart: Уровень: **{cursor.execute("SELECT lvl FROM users WHERE id = {}".format(member.id)).fetchone()[0]}**\n\n Общайся с другими что бы прокочать свой уровень""", color = bot_color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def award(ctx, member: discord.Member = None, amount: int = None):
    if member is None:
        await ctx.send(embed = discord.Embed (f"**{ctx.author}**, укажите пользователя, которому желаете выдать определенную сумму", color = bot_color))
    else:
        if amount is None:
            await ctx.send(embed = discord.Embed (f"**{ctx.author}**, укажите сумму, которую желаете начислить на счет пользователя", color = bot_color))
        elif amount < 1:
            await ctx.send(embed = discord.Embed (f"**{ctx.author}**, укажите сумму больше 1 {bot_coin}", colour = bot_color))
        else:
            cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(amount, member.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')
 
 
@client.command()
@commands.has_permissions(administrator = True)
async def take(ctx, member: discord.Member = None, amount = None):
    if member is None:
        await ctx.send(f"**{ctx.author}**, укажите пользователя, у которого желаете отнять сумму денег")
    else:
        if amount is None:
            await ctx.send(f"**{ctx.author}**, укажите сумму, которую желаете отнять у счета пользователя")
        elif amount == 'all':
            cursor.execute("UPDATE users SET cash = {} WHERE id = {}".format(0, member.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')
        elif int(amount) < 1:
            await ctx.send(f"**{ctx.author}**, укажите сумму больше 1 :leaves:")
        else:
            cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(int(amount), member.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')
 
@client.command()
async def pay(ctx, member: discord.Member = None, amount: int = None):
    if member is None:
        await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите пользователя, которому желаете перевести определенную сумму", color = bot_color))
    else:
        if amount is None:
            await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите сумму, которую желаете начислить на счет пользователя", color = bot_color))
        elif amount < 1:
            await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите сумму больше 1 {bot_coin}", colour = bot_color))
        else:
            cursor.execute("UPDATE users SET bank = bank + {} WHERE id = {}".format(amount, member.id))
            cursor.execute("UPDATE users SET bank = bank - {} WHERE id = {}".format(amount, ctx.author.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')

@client.command(aliases=['deposit'])
async def dep(ctx, amount: int = None):
        if amount is None:
            await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите сумму, которую желаете начислить в банк", color = bot_color))
        elif amount < 1:
            await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите сумму больше 1 {bot_coin}", colour = bot_color))
        else:
            cursor.execute("UPDATE users SET bank = bank + {} WHERE id = {}".format(amount, ctx.author.id))
            cursor.execute("UPDATE users SET wallet = wallet - {} WHERE id = {}".format(amount, ctx.author.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')

@client.command(aliases=['wd'])
async def withdraw(ctx, amount: int = None):
        if amount is None:
            await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите сумму депозита, которую желаете снять", color = bot_color))
        elif amount < 1:
            await ctx.reply(embed = discord.Embed (f"**{ctx.author}**, укажите сумму больше 1 {bot_coin}", colour = bot_color))
        else:
            cursor.execute("UPDATE users SET bank = bank - {} WHERE id = {}".format(amount, ctx.author.id))
            cursor.execute("UPDATE users SET wallet = wallet + {} WHERE id = {}".format(amount, ctx.author.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')

@client.command(aliases=['работать', 'работа'])
@commands.cooldown(1, 900, commands.BucketType.user)
async def work(ctx):
            work = random.choice(['горничной', 'официантом', 'врачём', 'водителем', 'таксистом', 'поваром', 'уборщиком', 'стриптизёром', 'доставщиком Glovo', 'парикмахером', 'продавцом', 'электриком', 'сантехником', 'консультантом', 'дальнобойщиком', 'учителем', 'аптекарем'])
            amount = random.randint(100, 300)
            embed = discord.Embed(title=f"Работать", description=f"{ctx.author.mention} вы успешно поработали **{work}**, и заработали **{amount} {bot_coin}**", colour = bot_color)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{ctx.author.name} \u200b')
            await ctx.reply(embed=embed)
            cursor.execute("UPDATE users SET wallet = wallet + {} WHERE id = {}".format(amount, ctx.author.id))
            connection.commit()

@work.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
        embed = discord.Embed(title=f"Ты уже поработал!",description=f"Можешь отдыхнать ещё `{retry_after}` сек.", color=bot_color)#error.retry_after:.2f
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

@client.command(aliases = ['add-shop'])
@commands.has_permissions(administrator = True)
async def add_shop(ctx, role: discord.Role = None, cost: int = None):
    if role is None:
        await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете внести в магазин")
    else:
        if cost is None:
            await ctx.send(f"**{ctx.author}**, укажите стоимость для даннойй роли")
        elif cost < 0:
            await ctx.send(f"**{ctx.author}**, стоимость роли не может быть такой маленькой")
        else:
            cursor.execute("INSERT INTO shop VALUES ({}, {}, {})".format(role.id, ctx.guild.id, cost))
            connection.commit()
 
            await ctx.message.add_reaction('✅')
 
 
@client.command(aliases = ['remove-shop'])
@commands.has_permissions(administrator = True)
async def remove_shop(ctx, role: discord.Role = None):
    if role is None:
        await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете удалить из магазина")
    else:
        cursor.execute("DELETE FROM shop WHERE role_id = {}".format(role.id))
        connection.commit()
 
        await ctx.message.add_reaction('✅')
 
 
@client.command(aliases = ['магазин'])
async def shop(ctx):
    embed = discord.Embed(title = f'Магазин {ctx.guild.name}', color=bot_color)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')

    counter = 0
 
    for row in cursor.execute("SELECT role_id, cost FROM shop WHERE id = {}".format(ctx.guild.id)):
        if ctx.guild.get_role(row[0]) != None:
            counter += 1
            embed.add_field(
                name = f"№{counter} "+"{"+f" \n Цена: {row[1]} {bot_coin} \n Роль:",
                value = f"{ctx.guild.get_role(row[0]).mention}"+"\n**}**",
                inline = False
            )
        else:
            pass
 
    await ctx.reply(embed = embed)
 
@client.command(aliases = ['buy-role'])
async def buy(ctx, role: discord.Role = None):
    if role is None:
        await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете приобрести")
    else:
        if role in ctx.author.roles:
            await ctx.send(f"**{ctx.author}**, у вас уже имеется данная роль")
        elif cursor.execute("SELECT cost FROM shop WHERE role_id = {}".format(role.id)).fetchone()[0] > cursor.execute("SELECT wallet FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]:
            await ctx.send(f"**{ctx.author}**, у вас недостаточно средств для покупки данной роли")
        else:
            await ctx.author.add_roles(role)
            cursor.execute("UPDATE users SET wallet = wallet - {} WHERE id = {}".format(cursor.execute("SELECT cost FROM shop WHERE role_id = {}".format(role.id)).fetchone()[0], ctx.author.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')
 
 
@client.command(aliases = ['+rep'])
async def rep(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"**{ctx.author}**, укажите участника сервера")
    else:
        if member.id == ctx.author.id:
            await ctx.send(f"**{ctx.author}**, вы не можете указать смого себя")
        else:
            cursor.execute("UPDATE users SET rep = rep + {} WHERE id = {}".format(1, member.id))
            connection.commit()
 
            await ctx.message.add_reaction('✅')
 
 
@client.command(aliases = ['lb'])
async def leaderboard(ctx):
    embed = discord.Embed(title = 'Топ 10 сервера')
    counter = 0
 
    for row in cursor.execute("SELECT name, wallet FROM users WHERE server_id = {} ORDER BY wallet DESC LIMIT 10".format(ctx.guild.id)):
        counter += 1
        embed.add_field(
            name = f'# {counter} | `{row[0]}`',
            value = f'Баланс: {row[1]}',
            inline = False,
            colour = bot_color
        )
 
    await ctx.send(embed = embed)


@client.command(aliases = ['профиль'])
async def profile(ctx, member: discord.Member = None):
    if member is None:
        id_marry = cursor.execute("SELECT marry FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]
        embed = discord.Embed(title=f'Профиль пользователя {ctx.message.author}', description=f'**На руках:**\n{cursor.execute("SELECT wallet FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} {bot_coin}\n\nВ банке: {cursor.execute("SELECT bank FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} {bot_coin}\n\n**:zap: Уровень:**\n{cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]}\n\n**:military_medal: Репутация:**\n{cursor.execute("SELECT rep FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]}\n\n**:cake: День рождения:**\nне указано\n\n**💞 Свадьба:**\n<@{id_marry}>\n\n', colour = bot_color)
        embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.set_thumbnail(url=ctx.message.author.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)
    else:
        id_mamber_marry = cursor.execute("SELECT marry FROM users WHERE id = {}".format(member.id)).fetchone()[0]
        embed = discord.Embed(title=f'Профиль пользователя {member}', description=f'**На руках:**\n{cursor.execute("SELECT wallet FROM users WHERE id = {}".format(member.id)).fetchone()[0]} {bot_coin}\n\nВ банке: {cursor.execute("SELECT bank FROM users WHERE id = {}".format(member.id)).fetchone()[0]} {bot_coin}\n\n**:zap: Уровень:**\n{cursor.execute("SELECT lvl FROM users WHERE id = {}".format(member.id)).fetchone()[0]}\n\n**:military_medal: Репутация:**\n{cursor.execute("SELECT rep FROM users WHERE id = {}".format(member.id)).fetchone()[0]}\n\n**:cake: День рождения:**\nДата не указана\n\n**💞 Свадьба:**\n<@{id_mamber_marry}>\n\n', colour = bot_color)
        embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

@client.command(aliases=["казино"])
async def casino(ctx, amount: int):
    def check(m):
        return m.author.id == ctx.author.id
     
    embed = discord.Embed(description=f"{ctx.author.mention} какое число выпадет? от 1 до 6 🎲", color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

    try:
        # Ожидание ответа от пользователя. timeout - время ожидания.
        answer = await client.wait_for("message", check=check, timeout=30)
        answer = answer.content
    except TimeoutError:
        # Если время ожидания вышло.
        return await ctx.reply('Время вышло!')

    # Число от 1 до 6
    number = random.randint(1, 6)

    if re.match(r'[1-6]', answer):
        if number == int(answer):
            embed = discord.Embed(title=f"Вы выйграли {amount*3} {bot_coin}", color=discord.Color.green())
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{ctx.author.name} \u200b')
            cursor.execute("UPDATE users SET bank = bank + {} WHERE id = {}".format(amount*3, ctx.author.id))
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title=f"Вы проиграли {amount*3} {bot_coin}", color=discord.Color.red())
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{ctx.author.name} \u200b')
            cursor.execute("UPDATE users SET bank = bank - {} WHERE id = {}".format(amount*3, ctx.author.id))
            return await ctx.reply(embed=embed)
    else:
        return await ctx.reply('Нужно указать число!')

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def minecraft(ctx, arg):
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()

    description = json_data["server"]["motd"]
    online = str(json_data["server"]["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(
        title=arg + "",
        description='Описание: ' + description + '\nОнлайн: ' + online + '\nИгроков: ' + playerCount,
        color=discord.Color.dark_green()
    )
    embed.set_thumbnail(url="https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1")

    await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------wot-blitz-----------------------------------------------------------
 
login_dict = {
}

def get_account_id(player, server):
    data = requests.get(
        f"https://api.wotblitz.{server}/wotb/account/list/?application_id=95523cc25e231e510f678729e21a9e10&search={player}")
    json_data = json.loads(data.text)
    info = json_data['data']
    account_id = info[0]['account_id']
    return account_id


def get_clan_id(account_id, server):
    data = requests.get(
        f"https://api.wotblitz.{server}/wotb/clans/accountinfo/?application_id=95523cc25e231e510f678729e21a9e10&account_id={account_id}")
    json_data = json.loads(data.text)
    total_data = json_data['data']
    player_id_category = total_data[f'{account_id}']
    if player_id_category is None:
        clan_id = None
    else:
        clan_id = player_id_category['clan_id']
    return clan_id

@client.command()
async def wot_blitz(ctx, player=None, *, server=None):
    if player is None and server is None:
        try:
            for key in login_dict:
                if key == f"{ctx.author.id}":
                    print(login_dict[key])
                    player = login_dict[key][0]
                    #print(player)
                    server = login_dict[key][1]
                else:
                    print(key)
        except:
            await ctx.send("Произошла ошибка, свяжитесь с владельцем бота")

    if server is None:
        await ctx.send("Пожалуйста, введите сервер.")
    else:
        if server == "eu" or server == "Eu" or server == "EU":
            server = "eu"
        elif server == "na" or server == "NA":
            server = "com"
        elif server == "ru" or server == "Ru" or server == "RU":
            server = "ru"
        elif server == "asia" or server == "Asia" or server == "ASIA":
            server = "asia"
        else:
            await ctx.send("Пожалуйста, введите действительный сервер.")

    if player is None:
        await ctx.send("Пожалуйста, введите ник игрока.")
    else:
        try:
            account_id = get_account_id(player=player, server=server)

            data = requests.get(
                f"https://api.wotblitz.{server}/wotb/account/info/?application_id=95523cc25e231e510f678729e21a9e10&account_id={account_id}")
            json_data = json.loads(data.text)

            # json subcatagory scraping
            total_data = json_data['data']
            player_id_category = total_data[f'{account_id}']
            player_nickname = player_id_category['nickname']
            statistic = player_id_category['statistics']
            player_stats = statistic['all']

            total_wins = player_stats['wins']
            total_losses = player_stats['losses']
            total_random_battles = player_stats['battles']
            total_frags = player_stats['frags']

            damage_dealt = player_stats['damage_dealt']
            damage_received = player_stats['damage_received']

            player_last_battle = datetime.datetime.fromtimestamp(player_id_category['last_battle_time'])
            account_creation_date = datetime.datetime.fromtimestamp(player_id_category['created_at'])

            embed = discord.Embed(title=f"`{player_nickname}` Статистика игры",
                          description="<:WoTB_logo:961241112998182963> Статистика всей игры игрока WoTBlitz:",
                          colour=bot_color)

            winrate = float("{0:.2f}".format(total_wins / total_random_battles * 100))
            damage_ratio = float("{0:.2f}".format(damage_dealt / damage_received))

            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar.url)
            embed.add_field(name=':triangular_flag_on_post: **Боёв**', value=f'┕`{total_random_battles}`',
                            inline=True)
            embed.add_field(name=':100: **Побед**', value=f'┕`{total_wins}`', inline=True)
            embed.add_field(name=':flag_white: **Поражений**', value=f'┕`{total_losses}`', inline=True)
            embed.add_field(name=':dart: **Винрейт**', value=f'┕`{winrate}%`', inline=True)
            embed.add_field(name=':no_entry_sign: **Унечтожено/Фрагов**', value=f'┕`{total_frags}`', inline=True)
            embed.add_field(name=':hourglass_flowing_sand: **Коэффициент урона**', value=f'┕`{damage_ratio}`', inline=True)
            embed.add_field(name=f":clock1: Создан: `{account_creation_date.strftime('%Y-%m-%d %H:%M:%S')}`",
                            value='==================================', inline=False)

            clan_id = get_clan_id(account_id=account_id, server=server)
            if clan_id is None:
                embed.add_field(name=':x: **Ошибка**', value=f'┕`{player_nickname}` либо не состоит в клане, либо '
                                                            f'произошла ошибка. Пожалуйста свяжитесь c __**{bot_owner}'
                                                            f'**__ если у вас есть какие-нибудь вопросы '
                                                            f'или опасения.', inline=False)
                embed.set_footer(
                    text=f"Сервер: {server} | ID Blitz Account: {account_id} | Последний бой: {player_last_battle.strftime('%Y-%m-%d %H:%M:%S')}")

            else:
                data = requests.get(
                    f"https://api.wotblitz.{server}/wotb/clans/info/?application_id=95523cc25e231e510f678729e21a9e10&clan_id={clan_id}")
                json_data = json.loads(data.text)

                total_data = json_data['data']
                clan_id_category = total_data[f'{clan_id}']
                clan_name = clan_id_category['name']
                member_count = clan_id_category['members_count']

                embed.add_field(name=':trident: **Клан**', value=f'┕`{clan_name}`', inline=True)
                embed.add_field(name=':pencil: **Количество игроков**', value=f'┕`{member_count}`', inline=True)

                embed.set_footer(
                    text=f"Сервер: {server} | ID Blitz Account: {account_id} | Последний бой: {player_last_battle.strftime('%Y-%m-%d %H:%M:%S')}")

            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send(f"Пользователь `{player}` не найден.")
       
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------wot---------------------------------------------------------------

login_dict = {
}

def get_account_id_wot(player, server):
    data = requests.get(
        f"https://api.worldoftanks.{server}/wot/account/list/?application_id=22bd610df6329f43159fa91df2b0d969&search={player}")
    json_data = json.loads(data.text)
    info = json_data['data']
    account_id = info[0]['account_id']
    return account_id


def get_clan_id(account_id, server):
    data = requests.get(
        f"https://api.worldoftanks.{server}/wot/clans/accountinfo/?application_id=22bd610df6329f43159fa91df2b0d969&account_id={account_id}")
    json_data = json.loads(data.text)
    total_data = json_data['data']
    player_id_category = total_data[f'{account_id}']
    if player_id_category is None:
        clan_id = None
    else:
        clan_id = player_id_category['clan_id']
    return clan_id

@client.command()
async def wot(ctx, player=None, *, server=None):
    if player is None and server is None:
        try:
            for key in login_dict:
                if key == f"{ctx.author.id}":
                    print(login_dict[key])
                    player = login_dict[key][0]
                    #print(player)
                    server = login_dict[key][1]
                else:
                    print(key)
        except:
            await ctx.send("Произошла ошибка, свяжитесь с владельцем бота")

    if server is None:
        await ctx.send("Пожалуйста, введите сервер.")
    else:
        if server == "eu" or server == "Eu" or server == "EU":
            server = "eu"
        elif server == "na" or server == "NA":
            server = "com"
        elif server == "ru" or server == "Ru" or server == "RU":
            server = "ru"
        elif server == "asia" or server == "Asia" or server == "ASIA":
            server = "asia"
        else:
            await ctx.send("Пожалуйста, введите действительный сервер.")

    if player is None:
        await ctx.send("Пожалуйста, введите ник игрока.")
    else:
        try:
            account_id = get_account_id_wot(player=player, server=server)

            data = requests.get(
                f"https://api.worldoftanks.{server}/wot/account/info/?application_id=22bd610df6329f43159fa91df2b0d969&account_id={account_id}")
            json_data = json.loads(data.text)

            # json subcatagory scraping
            total_data = json_data['data']
            player_id_category = total_data[f'{account_id}']
            player_nickname = player_id_category['nickname']
            statistic = player_id_category['statistics']
            player_stats = statistic['all']

            total_wins = player_stats['wins']
            total_losses = player_stats['losses']
            total_random_battles = player_stats['battles']
            total_frags = player_stats['frags']

            damage_dealt = player_stats['damage_dealt']
            damage_received = player_stats['damage_received']

            player_last_battle = datetime.datetime.fromtimestamp(player_id_category['last_battle_time'])
            account_creation_date = datetime.datetime.fromtimestamp(player_id_category['created_at'])

            embed = discord.Embed(title=f"`{player_nickname}` Статистика игры",
                          description="<:WoTB_logo:961241112998182963> Статистика всей игры игрока WoTBlitz:",
                          colour=bot_color)

            winrate = float("{0:.2f}".format(total_wins / total_random_battles * 100))
            damage_ratio = float("{0:.2f}".format(damage_dealt / damage_received))

            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar.url)
            embed.add_field(name=':triangular_flag_on_post: **Боёв**', value=f'┕`{total_random_battles}`',
                            inline=True)
            embed.add_field(name=':100: **Побед**', value=f'┕`{total_wins}`', inline=True)
            embed.add_field(name=':flag_white: **Поражений**', value=f'┕`{total_losses}`', inline=True)
            embed.add_field(name=':dart: **Винрейт**', value=f'┕`{winrate}%`', inline=True)
            embed.add_field(name=':no_entry_sign: **Унечтожено/Фрагов**', value=f'┕`{total_frags}`', inline=True)
            embed.add_field(name=':hourglass_flowing_sand: **Коэффициент урона**', value=f'┕`{damage_ratio}`', inline=True)
            embed.add_field(name=f":clock1: Создан: `{account_creation_date.strftime('%Y-%m-%d %H:%M:%S')}`",
                            value='==================================', inline=False)

            clan_id = get_clan_id(account_id=account_id, server=server)
            if clan_id is None:
                embed.add_field(name=':x: **Ошибка**', value=f'┕`{player_nickname}` либо не состоит в клане, либо '
                                                            f'произошла ошибка. Пожалуйста свяжитесь c __**Феликс#0001'
                                                            f'**__ если у вас есть какие-нибудь вопросы '
                                                            f'или опасения.', inline=False)
                embed.set_footer(
                    text=f"Сервер: {server} | ID Blitz Account: {account_id} | Последний бой: {player_last_battle.strftime('%Y-%m-%d %H:%M:%S')}")

            else:
                data = requests.get(
                    f"https://api.worldoftanks.{server}/wot/clans/info/?application_id=22bd610df6329f43159fa91df2b0d969&clan_id={clan_id}")
                json_data = json.loads(data.text)

                total_data = json_data['data']
                clan_id_category = total_data[f'{clan_id}']
                clan_name = clan_id_category['name']
                member_count = clan_id_category['members_count']

                embed.add_field(name=':trident: **Клан**', value=f'┕`{clan_name}`', inline=True)
                embed.add_field(name=':pencil: **Количество игроков**', value=f'┕`{member_count}`', inline=True)

                embed.set_footer(
                    text=f"Сервер: {server} | ID Blitz Account: {account_id} | Последний бой: {player_last_battle.strftime('%Y-%m-%d %H:%M:%S')}")

            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send(f"Пользователь `{player}` не найден.")

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.group(invoke_without_command = True, aliases=["фейк", "unreal", "tin"])
async def fake(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип чата не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help create`)")

@fake.command(aliases=["персонаж", "persona"])
async def personality(ctx):
    fake = Faker('ru_RU')
    embed = discord.Embed(title="Рандомная личность 🕵️‍♀️", color=bot_color)
    embed.add_field(name="Имя:", value=f"{fake.name()}", inline=False)
    embed.add_field(name="Профессия:", value=f"{fake.job()}", inline=False)
    embed.add_field(name="Номер телефона:", value=f"{fake.phone_number()}", inline=False)
    embed.add_field(name="Электронный адрес: ", value=f"{fake.free_email()}", inline=False)
    embed.add_field(name="Адрес:", value=f"{fake.address()}", inline=False)
    embed.add_field(name="День рождения:", value=f"{fake.date_of_birth()}", inline=False)
    embed.add_field(name="Цвет волос:", value=f"{fake.color_name()}", inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@fake.command(aliases=["карта"])
async def card(ctx):
    fake = Faker('ru_RU')
    fake_balance = random.randint(1, 48000)
    embed = discord.Embed(title="Рандомная банковская карта 💳", color=bot_color)
    embed.add_field(name="Владелец:", value=f"{fake.name()}", inline=False)
    embed.add_field(name="Баланс:", value=f"{fake_balance}$")
    embed.add_field(name="Дата:", value=f"{fake.credit_card_expire()}", inline=True)
    embed.add_field(name="Номер:", value=f"{fake.credit_card_number()}", inline=False)
    embed.add_field(name="Банк: ", value=f"{fake.bank()}")
    embed.add_field(name="Платёжная система:", value=f"{fake.credit_card_provider()}")
    embed.set_thumbnail(url="https://img.icons8.com/plasticine/400/sim-card-chip.png")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@fake.command(aliases=["нитро"])
async def nitro(ctx):
    link = ["https://discord.gift/svdKDpakdma", "https://discord.gift/ApdmlOnSia", "https://discord.gift/daUmepWE", "https://discord.gift/LdopEparw", "https://discord.gift/wERPdafgu", "https://discord.gift/giEpdatda", "https://discord.gift/LsnIanpa", "https://discord.gift/PkakcYXsi"]
    links = random.choice(link)
    embed = discord.Embed(title="Подарок нитро!", description=f"{links}", color=discord.Color.from_rgb(244,127,255))
    embed.set_image(url="https://images-ext-2.discordapp.net/external/gZ5wyrZMyP_UpEPpR-o7tdkSkNnlukgCerl8ihjYOME/https/images-ext-2.discordapp.net/external/fsLiBhigfy4QCCbL0ggphzfPyeaIll0nmNvcE5zlXec/https/media.discordapp.net/attachments/862030971305328643/865320983086628905/xedy9ugkqo621.png")
    await ctx.message.delete()
    await ctx.send(embed=embed)

@fake.command(aliases=["буст"])
async def boost(ctx):
    embed = discord.Embed(title=f"<a:boost:965238386409500692> Ура! {ctx.author.name} Бустит наш сервер!", color=discord.Color.from_rgb(255,114,250))
    embed.set_image(url="https://images-ext-1.discordapp.net/external/qg5eaY5TezymGxulK6BjGBgbsCoBWV2nLrKlAa_-n88/https/images-ext-2.discordapp.net/external/r48TtXE-ZgPEHtp04IEXXflGAjVYYkA-950-glMywIc/https/images-ext-1.discordapp.net/external/dlWfg-4OjgObnG_H4ARXMAM0w5S_1IrvIxsjYQMTN1M/https/media.discordapp.net/attachments/897123699914838106/900705333893275718/6gdSqO8.gif")
    await ctx.message.delete()
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def emoji(ctx, emoji: discord.Emoji):
        embed = discord.Embed(title=f"Команда: Эмодзи", description=f"**Эмодзи инфо:**\n**Название эмодзи:** {emoji.name}\n**Id эмодзи:** {emoji.id}\n**Анимация:** {emoji.animated}\n**Эмодзи:** {emoji}\n**[Скачать 🔗]({emoji.url})**", color=bot_color)#{emoji.name}\nId эмодзи: {emoji.id}\nЭмодзи: {emoji}
        embed.set_image(url=emoji.url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed=embed)

@client.command()
async def deleteemoji(ctx, emoji: discord.Emoji):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.reply(f'Successfully deleted (or not): {emoji}')
		await emoji.delete()
       
#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------укусить--------------------------------------------------------

@client.command(pass_context=True)#команда для укуса
async def bite(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: кусь', description='{}, укусил {}. А если бы откусил 😱'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(255, 255, 255))
    bite=['https://i.pinimg.com/originals/db/e3/48/dbe348e338fc03973a5f4f4f14f92b9d.gif', 'https://c.tenor.com/4j3hMz-dUz0AAAAC/anime-love.gif']
    embed.set_image(url=random.choice(bite))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------ласкать--------------------------------------------------------

@client.command(pass_context=True)#команда для ласканий
async def caress(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: ласкать', description='{}, ласкает {}. Милота))'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 129, 160))
    caress=['https://c.tenor.com/DzmjDubvoi8AAAAd/anime-caress.gif', 
    'https://64.media.tumblr.com/6d4e50d3a62e5a90500eadc0537843b2/tumblr_mkiknpSJxF1rbtx3po1_500.gif']
    embed.set_image(url=random.choice(caress))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------засмущаться-----------------------------------------------------

@client.command(pass_context=True)#команда для засмущения
async def confuse(ctx):
    embed=discord.Embed(title='Реакция: смущение', description='{}, засмущался это так мило'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(98, 228, 250))
    confuse=['https://thumbs.gfycat.com/NauticalDeliciousFowl-size_restricted.gif'
    ]
    embed.set_image(url=random.choice(confuse))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------плакать--------------------------------------------------------


@client.command(pass_context=True)#команда для плаканья
async def cry(ctx):
    embed=discord.Embed(title='Реакция: плач', description='{}, палчет. Может чем нибудь помочь?'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(68, 250, 234))
    cry=['https://c.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif', 
    'http://static.tumblr.com/fmikcqz/7Allyi1ls/anime_cry_sad_rain.gif', 'https://c.tenor.com/k2SKe36YwIUAAAAC/crying-girl.gif', 
    'https://www.techjunkie.com/wp-content/uploads/2018/03/Anime-Gif-with-Sad-Face-1.gif', 'https://c.tenor.com/gDk49oAcW9QAAAAd/anime-cry-cry.gif']
    embed.set_image(url=random.choice(cry))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------танцевать-------------------------------------------------------

@client.command(pass_context=True)#команда для плаканья
async def dance(ctx):
    embed=discord.Embed(title='Реакция: танец', description='Посмотрите как красиво танцует {}'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(83, 224, 118))
    dance=['https://media2.giphy.com/media/euMGM3uD3NHva/200.gif', 
    'https://aniyuki.com/wp-content/uploads/2021/05/aniyuki-anime-dance-gif-28.gif']
    embed.set_image(url=random.choice(dance))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------Самоубийство------------------------------------------------------

@client.command(pass_context=True)#команда для суицид
async def suicide(ctx):
    embed=discord.Embed(title='Реакция: твоя мать шлюха', description='Нет {} почему ты это сделал(а)? 😭😭😭'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(0, 0, 0))
    suicide=['https://c.tenor.com/OdehztbrpecAAAAC/anime-falling.gif', 
    'https://i.gifer.com/F5Ai.gif']
    embed.set_image(url=random.choice(suicide))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------1000-7---------------------------------------------------------

@client.command(pass_context=True)#команда для 1000-7
async def dead_inside(ctx):
    embed=discord.Embed(title='Реакция: дед инсайд.......', description='{}, 1000-7'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(0, 0, 0))
    dead_inside=['https://c.tenor.com/CCE66BvfC38AAAAC/tokyo-ghoul-ken-watanabe.gif']
    embed.set_image(url=random.choice(dead_inside))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------------пить----------------------------------------------------------

@client.command(pass_context=True)#команда для запоя
async def drink(ctx):
    embed=discord.Embed(title='Реакция: пить', description='{}, спился от даун))'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(240, 238, 91))
    drink=['https://c.tenor.com/SEoWK3bFonUAAAAd/anime-beer.gif', 
    'https://i.pinimg.com/originals/c1/a2/da/c1a2daf389b14a2f14abfdb9bcda8b6a.gif']
    embed.set_image(url=random.choice(drink))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------куашть---------------------------------------------------------

@client.command(pass_context=True)#команда для еды
async def eat(ctx):
    embed=discord.Embed(title='Реакция: кушать', description='{}, совсем зажрался'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(240, 238, 91))
    eat=['https://i.gifer.com/5HsF.gif', 'https://animesher.com/orig/1/149/1495/14951/animesher.com_eat-gif-birthday-1495177.gif', 
    'https://64.media.tumblr.com/5858fdafbc60c682aa585d3937f7c816/tumblr_inline_p7l32k75ck1v3eowb_540.gifv', 'https://giffiles.alphacoders.com/196/196155.gif',
    'https://i.kym-cdn.com/photos/images/original/001/107/679/b59.gif']
    embed.set_image(url=random.choice(eat))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#--------------------------------------------ударить----------------------------------------------------------

@client.command(pass_context=True)#команда для удара
async def hit(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: въебать', description='{}, ударил {} 😱😱😱'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(0, 0, 0))
    hit=['https://c.tenor.com/FJsjk_9b_XgAAAAC/anime-hit.gif', 'https://i.gifer.com/9Ky5.gif', 'https://data.whicdn.com/images/267081888/original.gif']
    embed.set_image(url=random.choice(hit))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------обнять----------------------------------------------------------

@client.command(pass_context=True)#команда для обнимашек
async def hug(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: обнять', description='{}, обнял(а) {}. Как это мило'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 150, 57))
    hug=['https://i.imgur.com/mk1tSAH.gif', 'https://64.media.tumblr.com/988a4660509af669515a40fd2ee38ada/b6806f9e566d4b2e-1d/s1280x1920/e0827aed786d0eeed23689dc320940b108c4305a.gif', 
    'https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif']
    embed.set_image(url=random.choice(hug))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------радоваться--------------------------------------------------------

@client.command(pass_context=True)#команда для радости
async def joy(ctx):
    embed=discord.Embed(title='Реакция: радоваться', description='У {} всё заебись и ему(ей) на всех похуй'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(240, 232, 69))
    joy=['https://i.pinimg.com/originals/68/53/45/685345402b067d8ced595481f8aa23da.gif', 
    'https://c.tenor.com/nBWlYPbKxzwAAAAC/anime-happy.gif']
    embed.set_image(url=random.choice(joy))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------поцеловаться------------------------------------------------------

@client.command(pass_context=True)#команда для поцелуев
async def kiss(ctx,member:discord.Member):
    embed=discord.Embed(description='{}, кажется тебя поцеловал(а) {}. Что это могло бы значить!? ヽ(°□° )ノ'.format(member.mention,ctx.message.author.mention), colour = discord.Color.from_rgb(235, 104, 237))
    kisses=['https://i.pinimg.com/originals/aa/18/c7/aa18c72b11f908963b33f4dced6ec88f.gif'
    ,'https://images.gr-assets.com/hostedimages/1604779980ra/30348890.gif', 'https://data.whicdn.com/images/356434547/original.gif']
    embed.set_image(url=random.choice(kisses))
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------смех------------------------------------------------------------

@client.command(pass_context=True)#команда для смеха
async def laugh(ctx):
    embed=discord.Embed(title='Реакция: ебать вы лошары', description='{} смешно с вас'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(240, 232, 69))
    laugh=['https://c.tenor.com/o-q-kqaTzSsAAAAC/anime-laugh.gif', 
    'https://c.tenor.com/tspOBIHclv8AAAAd/nagatoro-anime-laugh.gif']
    embed.set_image(url=random.choice(laugh))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#--------------------------------------------облизать---------------------------------------------------------

@client.command(pass_context=True)#команда для облизываний члена
async def lick(ctx,member:discord.Member):
    embed=discord.Embed(title='Облизать', description='{} облизал(a) {} походу он(а) подумал(а) что это чле....'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 140, 149))
    lick=['https://c.tenor.com/Go7wnhOWjSkAAAAC/anime-lick-face.gif'
    ,'https://images-ext-2.discordapp.net/external/JQKVMz6BGC_onN9f1FE6CIy5uI9g4goUSzkEYcN6Q7g/https/i.imgur.com/SoNfzBt.gif']
    embed.set_image(url=random.choice(lick))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------признание-в-любви----------------------------------------------------

@client.command(pass_context=True)#команда для признаний в любви
async def lover(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: признаться в любви', description='{} признался(лася) в любви {}'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 140, 149))
    love=['https://giffiles.alphacoders.com/188/188468.gif'
    ,'https://c.tenor.com/rS045JX-WeoAAAAC/anime-love.gif']
    embed.set_image(url=random.choice(love))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------скучать---------------------------------------------------------

@client.command(pass_context=True)#команда для скучать
async def miss(ctx):
    embed=discord.Embed(title='Реакция: скучать', description='{} скучает может поиграем с ним(ней)?'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(66, 67, 69))
    miss=['https://animesher.com/orig/1/115/1156/11562/animesher.com_animes--anime-gif-1156289.gif', 'https://c.tenor.com/gaxGj7lADG8AAAAC/anime-girl-anime.gif']
    embed.set_image(url=random.choice(miss))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------погладить-------------------------------------------------------

@client.command(pass_context=True)#команда для погладить
async def pat(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: погладить', description='{} погладил(а) {} Это так мило UwU'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 140, 149))
    pat=['https://c.tenor.com/jEfC8cztigIAAAAC/anime-pat.gif'
    ,'https://i.pinimg.com/originals/d7/c3/26/d7c326bd43776f1e0df6f63956230eb4.gif']
    embed.set_image(url=random.choice(pat))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)


#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------------тыкнуть-------------------------------------------------------

@client.command(pass_context=True)#команда для тыкнуть
async def poke(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: тыкнуть', description='{} вставил(а) пальчик в анальчик {} '.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 140, 149))
    poke=['https://c.tenor.com/3dOqO4vVlr8AAAAC/poke-anime.gif'
    ,'https://i.pinimg.com/originals/f1/6d/16/f16d16a4ac88a59168916ddfd62b49dd.gif', 'https://c.tenor.com/NjIdfk7i3bsAAAAC/poke-poke-poke.gif', 'https://i.pinimg.com/originals/b4/95/fb/b495fb19f4b9a1b04f48297b676c497b.gif']
    embed.set_image(url=random.choice(poke))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#------------------------------------------------рэп-батл-----------------------------------------------------

@client.command(pass_context=True)#команда для тыкнуть
async def rap(ctx,member:discord.Member):
    embed=discord.Embed(title='Пруфы: мать твою ебал(а)', description='{} раскидал(а) {} по фактам'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(0,0,0))
    rap=['https://media.giphy.com/media/xpJibZRfyb8GchlkVL/giphy.gif']
    embed.set_image(url=random.choice(rap))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-----------------------------------------------воскреснуть---------------------------------------------------

@client.command(pass_context=True)#команда для воскреснуть
async def resurrected(ctx):
    embed=discord.Embed(title='Реакция: воскреснуть', description='{} воскрес(ла)... он(а) ангел или дед инсайд?'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(66, 67, 69))
    resurrected=['https://c.tenor.com/xAWRN4fLcoIAAAAC/resurrect-anime.gif']
    embed.set_image(url=random.choice(resurrected))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------бежать------------------------------------------------------

@client.command(pass_context=True)#команда бежать
async def run(ctx):
    embed=discord.Embed(title='Реакция: бежать', description='{} съебался'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(118, 209, 245))
    run=['https://media0.giphy.com/media/JRlqKEzTDKci5JPcaL/giphy.gif', 'https://media.discordapp.net/attachments/937397780287205383/944665283245797376/20220219_194146.gif']
    embed.set_image(url=random.choice(run))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------грустить----------------------------------------------------

@client.command(pass_context=True)#команда для грустить
async def sad(ctx):
    embed=discord.Embed(title='Реакция: грустить', description='{} грустит(. Может расскажем ему анекдот?'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(66, 67, 69))
    sad=['https://i.pinimg.com/originals/0e/93/51/0e9351b77fab4bf407f16a6d7e82168c.gif']
    embed.set_image(url=random.choice(sad))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)


#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------выебать---------------------------------------------------

@client.command(pass_context=True)#команда для выебать
async def sex(ctx, member:discord.Member):
    embed=discord.Embed(title='Реакция: секс', description='{} занялся сексом с {}'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(228, 209, 189))
    sex=['https://64.media.tumblr.com/3e373d2bf62191ed0418c8746c159258/tumblr_nmsjpbKMuX1u35cjio1_400.gif'
    ,'https://64.media.tumblr.com/745db81614f8c953463949e2abc543ef/tumblr_nnsja9hiHT1u35cjio1_500.gif']
    embed.set_image(url=random.choice(sex))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#--------------------------------------------------щелбан-----------------------------------------------------

@client.command(pass_context=True)#команда для выебать
async def slit(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: щелбан', description='{} дал щелбан {}'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(228, 209, 189))
    slit=['https://anime-chan.me/uploads/posts/2015-06/1434639333_tumblr_nq3tforHq61tga1sco1_540.gif', 'https://anime-chan.me/uploads/posts/2016-10/1475612990_tumblr_oegx5uSUV31s4qvrdo1_540.gif', 
    'https://anime-chan.me/uploads/posts/2017-09/1504922382_tumblr_otrc2pLfJk1u86t2qo1_500.gif']
    embed.set_image(url=random.choice(slit))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#--------------------------------------------------шок--------------------------------------------------------

@client.command(pass_context=True)#команда для шок
async def shock(ctx):
    embed=discord.Embed(title='Реакция: шок', description='{} в шоке!'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(255, 255, 255))
    shock=['https://c.tenor.com/YIkb2YT9xFwAAAAC/anime-hitoribocchi.gif'
    ,'https://media1.giphy.com/media/zgGrSqSi3SSqs/200.gif', 'https://c.tenor.com/xD13KGAQC_0AAAAC/noragami-anime.gif']
    embed.set_image(url=random.choice(shock))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#--------------------------------------------выстрельнуть-----------------------------------------------------

@client.command(pass_context=True)#команда для выстрельнуть
async def shot(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: выстрельнуть', description='{} выстрелил(а) в {}. Он(а) сдох(ла)!? 😱😭'.format(ctx.message.author.mention,member.mention), colour = discord.Color.red())
    shot=['https://i.imgur.com/VqJlRR8.gif'
    ,'https://c.tenor.com/9G79MZldUhMAAAAd/anime-gun.gif']
    embed.set_image(url=random.choice(shot))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#---------------------------------------------пощечина-------------------------------------------------------

@client.command(pass_context=True)#команда для пощечина
async def slap(ctx,member:discord.Member):
    embed=discord.Embed(title='Реакция: пощечина', description='{} дал пощечину {}. Тебе больно?'.format(ctx.message.author.mention,member.mention), colour = discord.Color.from_rgb(240, 140, 149))
    slap=['https://media4.giphy.com/media/Zau0yrl17uzdK/giphy.gif'
    ,'https://i.imgur.com/fm49srQ.gif?noredirect', 'https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif']
    embed.set_image(url=random.choice(slap))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------спать----------------------------------------------------------

@client.command(pass_context=True)#команда для спать
async def sleep(ctx):
    embed=discord.Embed(title='Реакция: спать', description='{} спит. Что ему(ей) снится? 🌙⭐'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(138, 195, 230))
    sleep=['https://acegif.com/wp-content/gif/anime-sleep-2.gif'
    ,'https://acegif.com/wp-content/gif/anime-sleep-37.gif']
    embed.set_image(url=random.choice(sleep))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#----------------------------------------------курить---------------------------------------------------------

@client.command(pass_context=True)#команда для курить
async def smoke(ctx):
    embed=discord.Embed(title='Реакция: курить', description='{} закурил... может не стоит?'.format(ctx.message.author.mention), colour = discord.Color.from_rgb(92, 46, 0))
    smoke=['https://media3.giphy.com/media/7ERB0iMcJLaAQFg06Z/giphy.gif']
    embed.set_image(url=random.choice(smoke))
    embed.set_author( name = ctx.message.author.name, icon_url = ctx.message.author.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.message.delete()
    await ctx.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def cube(ctx):
  d = random.randint(0, 5)
  if d == 0:
    embed_0 = discord.Embed(title=f"{ctx.author.name}, кинул кость", description="Ему выпал `1`", color = bot_color)
    embed_0.set_image(url="https://media.discordapp.net/attachments/929051187364392963/934154132670013530/Picsart_22-01-21_23-27-48-717.jpg")
    embed_0.timestamp = datetime.datetime.utcnow()
    embed_0.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed_0)
  if d == 1:
    embed_1 = discord.Embed(title=f"{ctx.author.name}, подкинул кость", description="Ему выпало `2`", color = bot_color)
    embed_1.set_image(url="https://media.discordapp.net/attachments/929051187364392963/934154132913274950/Picsart_22-01-21_23-28-46-761.jpg")
    embed_1.timestamp = datetime.datetime.utcnow()
    embed_1.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed_1)
  if d == 2:
    embed_2 = discord.Embed(title=f"{ctx.author.name}, кинул кость", description="Ему выпал `3`", color = bot_color)
    embed_2.set_image(url="https://media.discordapp.net/attachments/929051187364392963/934154133399826452/Picsart_22-01-21_23-30-48-924.jp")
    embed_2.timestamp = datetime.datetime.utcnow()
    embed_2.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed_2)
  if d == 3:
    embed_3 = discord.Embed(title=f"{ctx.author.name}, подкинул кость", description="Ему выпало `4`", color = bot_color)
    embed_3.set_image(url="https://media.discordapp.net/attachments/929051187364392963/934154133668253696/Picsart_22-01-21_23-31-28-515.jpg")
    embed_3.timestamp = datetime.datetime.utcnow()
    embed_3.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed_3)
  if d == 4:
    embed_4 = discord.Embed(title=f"{ctx.author.name}, кинул плотную зигу", description="Ему выпал `5`", color = bot_color)
    embed_4.set_image(url="https://media.discordapp.net/attachments/929051187364392963/934154133903138816/Picsart_22-01-21_23-33-42-872.jpg")
    embed_4.timestamp = datetime.datetime.utcnow()
    embed_4.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed_4)
  if d == 5:
    embed_5 = discord.Embed(title=f"{ctx.author.name}, подкинул кость", description="Ему выпало `6`", color = bot_color)
    embed_5.set_image(url="https://media.discordapp.net/attachments/929051187364392963/934154134150594591/Picsart_22-01-21_23-34-37-760.jpg")
    embed_5.timestamp = datetime.datetime.utcnow()
    embed_5.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed_5)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command(aliases=["песня"])
async def lyrics(ctx, *, zapros=None):
    if zapros is None:
        await ctx.reply("Введите фрагмент песни для поиска")
    else:
        reponse = requests.get(f"https://some-random-api.ml/lyrics?title={zapros}")
        otv = reponse.json()
        try:
            embed=discord.Embed(title="Текст", url=f"{otv['links']['genius']}", description=otv['lyrics'], color=bot_color)
            embed.set_author(name=f"{otv['author']} - {otv['title']}")
            embed.set_thumbnail(url=f"{otv['thumbnail']['genius']}")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{ctx.author.name} \u200b')
            await ctx.reply(embed=embed)
        except:
            await ctx.reply("Песня не найдена")

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def achievement(ctx, *, text):
    text1 = text
    if len(text1) >= 30:
        # выводим сообщение об ошибке
        await ctx.reply(embed = discord.Embed(description = f'Длина текста не должна превышать `30` символов', color = bot_color))
        # используем return, чтобы завершить функцию
        return
    else:
        achievement = Image.open("img/achievement.png")
        colors = ["white"]
        drawer = ImageDraw.Draw(achievement)
        font = ImageFont.truetype("fonts/MinecraftRegular-Bmg3.otf", 15)
        for color in colors:
            drawer.text((60, 35), text=text1, font=font, fill=color)

        achievement.save("img/exit_achievement.png")
        #achievement.show()

        file = discord.File("img/exit_achievement.png", filename="exit_achievement.png")
        #embed = discord.Embed(color = discord.Colour.gold())
        embed = discord.Embed(title = 'Достижение', description = 'Получено новое достижение!', color = bot_color)
        embed.set_image(url="attachment://exit_achievement.png")
        await ctx.reply(file = file, embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

obj = qr.QRCode(  
    version = 1,  
    error_correction = qr.constants.ERROR_CORRECT_L,  
    box_size = 10,  
    border = 4,  
)  

@client.command(aliases=["qr"])
async def qrcode(ctx, *, text):
        obj.add_data(text)
        img = obj.make_image(fill_color = "cyan", back_color = "black")  
        img.save("img/qrcode.png")
        embed = discord.Embed(title="QRcode", description = 'Вот ваш QRcode:', color = bot_color)
        qrcode = discord.File("img/qrcode.png", filename="qrcode.png")
        embed.set_image(url="attachment://qrcode.png")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        #qrcode = os.remove("img/qrcode.png")
        await ctx.reply(file = qrcode, embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.group(invoke_without_command = True, aliases=["кодер"])
async def coder(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип кодеровки не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help coder`)")

@coder.command()
async def base64(ctx, *, text):

        sample_string = text
        sample_string_bytes = sample_string.encode("ascii")
  
        base64_bytes = bas64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        embed = discord.Embed(title="Кодер Base64", description = f"> {base64_string}", color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed = embed)

@client.group(invoke_without_command = True, aliases=["декодер"])
async def decoder(ctx):
    await ctx.message.reply(f"{ctx.author.name}, тип декодеровки не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help decoder`)")

@decoder.command()
async def base64(ctx, *, text):

        sample_string = text
        sample_string_bytes = sample_string.encode("ascii")
  
        base64_bytes = bas64.b64decode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        embed = discord.Embed(title="Декодер Base64", description = f"> {base64_string}", color = bot_color)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'{ctx.author.name} \u200b')
        await ctx.reply(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def math_game(ctx):
    math = str(random.randint(1, 50)) + random.choice(list('+-*')) + str(random.randint(1, 50))
    embed = discord.Embed(title="Математическая игра", description=f"Сколько будет `{math}`? \n На ответ даётся 10 секунд", color=bot_color)
    await ctx.reply(embed=embed)
    msg = await client.wait_for('message', timeout = 10)
    if msg.content == str(eval(math)):
        embed = discord.Embed(title="Верно!", color=bot_color)
        await msg.reply(embed=embed)
    else:
        embed = discord.Embed(title=f"Не верно! Ответ: `{str(eval(math))}`", color=bot_color)
        await msg.reply(embed=embed)

@math_game.error
async def game_error(ctx, err):
    embed = discord.Embed(title=f"Время истекло!", color=bot_color)
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.group(invoke_without_command = True, aliases=["рисовать","рисование"])
async def draw(ctx):
    await ctx.message.reply(f"{ctx.author.name}, цвет рисунка не указан. Пожалуйста, вызовить команду помощи (`{bot_prefix}help draw`)")

@draw.command(aliases=["оранжевый"])
async def orange(ctx):
    embed = discord.Embed(title="Рисование 🎨 | Orange", description=
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n"
f"||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||||🟧||\n",
color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@draw.command(aliases=["красный"])
async def red(ctx):
    embed = discord.Embed(title="Рисование 🎨 | Red", description=
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n"
f"||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||||🟥||\n",
color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@draw.command(aliases=["синий"])
async def blue(ctx):
    embed = discord.Embed(title="Рисование 🎨 | Blue", description=
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n"
f"||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||||🟦||\n",
color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@draw.command(aliases=["зёленый"])
async def green(ctx):
    embed = discord.Embed(title="Рисование 🎨 | Green", description=
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n"
f"||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||||🟩||\n",
color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b')
    await ctx.reply(embed=embed)

@draw.command(aliases=["белый"])
async def white(ctx):
    embed = discord.Embed(title="Рисование 🎨 | White", description=
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n"
f"||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||||⬜||\n",
color=bot_color)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b') 
    await ctx.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def anime(ctx, *, anime_name):
    try:
        anime = animec.Anime(anime_name)
    except:
        await ctx.send(f"Аниме `{anime_name}` не найдено")
        return
    embed = discord.Embed(title=anime.title_english, description=f"{anime.description[200:]}...", color=bot_color )
    embed.add_field(name="Эпизодов:", value=str(anime.episodes))
    embed.add_field(name="Рейтинг:", value=str(anime.rating))
    embed.add_field(name="Трансляции", value=str(anime.broadcast))
    embed.add_field(name="Статус", value=str(anime.status))
    embed.add_field(name="Тип", value=str(anime.type))
    embed.set_thumbnail(url=anime.poster)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name} \u200b') 
    await ctx.message.reply(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def server_news(ctx, *, text):
    embed = discord.Embed(title="Новости", description=text, color=bot_color )
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Новости сервера \u200b') 
    await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def server_rules(ctx, *, text):
    embed = discord.Embed(title="**__Правила__**", description="```py\n"+text+"\n```", color=bot_color )
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Правила сервера \u200b') 
    await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def bot_news(ctx, *, text):
    embed = discord.Embed(title=f"Новости {bot_name}", description=text, color=bot_color )
    embed.set_thumbnail(url=client.user.avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Новости {bot_name} \u200b') 
    await ctx.message.delete()
    await ctx.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}
# Struct:
# {
#    "<author_id>": ["<msg_time", "<msg_time>", ...],
#    "<author_id>": ["<msg_time"],
# }

hello_list = "Привет","привет","Эй халоп","эй халоп","Hi","hi","Hello","hello"

@client.event
async def on_message(ctx):
    if ctx.content.startswith("<@831803116071944212>"):
        await ctx.channel.send(f'Мой префикс `{bot_prefix}`')
    if ctx.content.startswith(hello_list):
        if not ctx.author.bot:
            await ctx.channel.send(f'Привет {ctx.author.name}!')
    global author_msg_counts

    author_id = ctx.author.id
    # Get current epoch time in milliseconds
    curr_time = datetime.datetime.now().timestamp() * 1000

    # Make empty list for author id, if it does not exist
    if not author_msg_times.get(author_id, False):
        author_msg_times[author_id] = []

    # Append the time of this message to the users list of message times
    author_msg_times[author_id].append(curr_time)

    # Find the beginning of our time window.
    expr_time = curr_time - time_window_milliseconds

    # Find message times which occurred before the start of our window
    expired_msgs = [
        msg_time for msg_time in author_msg_times[author_id]
        if msg_time < expr_time
    ]

    # Remove all the expired messages times from our list
    for msg_time in expired_msgs:
        author_msg_times[author_id].remove(msg_time)
    # ^ note: we probably need to use a mutex here. Multiple threads
    # might be trying to update this at the same time. Not sure though.

    if len(author_msg_times[author_id]) > max_msg_per_window:
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="Спам!", description=f"<@{author_id}>, был забанен за спам!", color=bot_color)
        await ctx.author.ban(reason="спам")
        await ctx.channel.send(embed=embed)

    await client.process_commands(ctx)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.group(invoke_without_command = True)
async def ticket(ctx):
    await ctx.reply(f"{ctx.author.name}, вы не выбрали взаимодействие с тикетом. Пожалуйста, вызовить команду помощи (`{bot_prefix}help ticket`)")

@ticket.command(pass_context=True)
#@commands.has_role("ceo")
async def create(ctx):
        #ticket_channel = await guild.create_text_channel(name=f'Тикет・{ctx.author.name}')
        name = 'Тикеты'
        category = discord.utils.get(ctx.guild.categories, name=name)
        foundchan = discord.utils.get(ctx.guild.text_channels, name=f"тикет・{ctx.author.name}")
        if category is None:
            category_create = await ctx.guild.create_category(name)

        if foundchan is None:
            channel = await ctx.guild.create_text_channel(f'тикет・{ctx.author.name}', category=category)
            embed = discord.Embed(title=f"Тикет {ctx.author.name}", description=f"{ctx.author.mention}, вы созадали тикет, подождите не много и с вами свяжется администратор сервера\n\nЧто бы закрыть тикест напишите `{bot_prefix}ticket close`.", color=bot_color)
            await channel.send(embed=embed)
        if foundchan:
            await ctx.channel.reply("У вас уже есть открытый тикет, что бы создать новый закройте старый.")
        Role = discord.utils.get(ctx.guild.roles, name="Тикет")
        if Role is None:
            await ctx.guild.create_role(name="Тикет", color=discord.Color.from_rgb(255, 210, 0))
        else:
            await channel.set_permissions(ctx.author, read_messages=True, send_messages=True, view_channel=True)
            await channel.set_permissions(ctx.guild.default_role, view_channel=False)
            await channel.set_permissions(Role, view_channel=True, send_messages=True, add_reactions=True)
            await category_create.set_permissions(ctx.author, read_messages=True, send_messages=True, view_channel=True)
            await category_create.set_permissions(ctx.guild.default_role, view_channel=False)
            await category_create.set_permissions(Role, view_channel=True, send_messages=True, add_reactions=True)

@ticket.command()
async def close(ctx):
    foundchan = discord.utils.get(ctx.guild.text_channels, name=f"тикет・{ctx.author.name}")
    embed = discord.Embed(title=f"Вы закрыли тикет", description=f"{ctx.author.mention}, вы закрыли свой тикет.\n\nЧто бы открыть его сново напишите `{bot_prefix}ticket create`", color=bot_color)
    #await discord.Member.send(embed=embed)
    await ctx.author.send(embed=embed)
    await foundchan.delete()

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@client.command()
@commands.has_permissions(manage_guild=True)
async def giveaway(ctx, time: str, *, prize: str):
    time = convert(time)

    embed = discord.Embed(title=prize,
                          description=f"Проводит - {ctx.author.mention}\n Нажмите на реакцию 🎉 что бы участвовать!\n Закончится через: **{time}** секунд\n Приз - **{prize}**",
                          color=bot_color)#ctx.guild.me.top_role.color

    msg = await ctx.channel.send(content="<a:icon_giveaway:974973075823165450> **GIVEAWAY** <a:icon_giveaway:974973075823165450>", embed=embed)
    await msg.add_reaction("🎉")

    await asyncio.sleep(3)
    await asyncio.sleep(int(time))

    new_msg = await ctx.channel.fetch_message(msg.id)

    user_list = [user for user in await new_msg.reactions[0].users().flatten() if
                 user != client.user]  # Check the reactions/don't count the bot reaction

    if len(user_list) == 0:
        await ctx.send("Нету участвующих.")
    else:
        winner = random.choice(user_list)
        await ctx.send(f"{winner.mention} ты выйграл **{prize}**!")

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def ben(ctx, time: str, *, prize: str):
    time = convert(time)

    msg = embed = discord.Embed(title="Бен", description=f"Выбери пробирку для реакции", color=bot_color)#ctx.guild.me.top_role.color
    await ctx.send(embed=embed)
    await msg.add_reaction("")

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

api_key = setting['openweathermap_api_key']
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel

    if x["cod"] != "404":
        async with channel.typing():

            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Погода в {city_name}", color=bot_color)
            embed.add_field(name="Описание", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Температура(C)", value=f"**{current_temperature_celsiuis}°C** :thermometer:", inline=False)
            embed.add_field(name="Влажность(%)", value=f"**{current_humidity}%** :sweat_drops:", inline=False)
            embed.add_field(name="Атмосферное давление(hPa)", value=f"**{current_pressure}hPa** :cloud:", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")    
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{ctx.author.name} \u200b') 

            await channel.reply(embed=embed)
    else:
        await channel.reply(f"Город `{city}` не найден.")

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.event
async def on_message_delete(message):
    if not message.author.bot:
        if message.channel.guild.id == settings['server_logs']:
            channel = client.get_channel(settings['channel_logs'])
            msg = f"**{message.author.mention}** удалил сообщение."
            embed = discord.Embed(color = bot_color, description = msg)
            embed.add_field(name = f"**Сообщение:**", value = f"{message.content}" + "\u200b")
            embed.add_field(name = f'**Канал:**', value = f'{message.channel.mention}')
            embed.set_author(name = f"{message.author.name}", icon_url=message.author.avatar.url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{message.author.name} \u200b') 
            await channel.send(embed = embed)

@client.event
async def on_message_edit(message_before, message_after):
    if not message_before.author.bot:
        if message_before.channel.guild.id == settings['server_logs']:
            channel = client.get_channel(settings['channel_logs'])
            msg = f"**{message_before.author.mention}** отредактировал сообщение."
            embed = discord.Embed(color = bot_color, description = msg)
            embed.add_field(name = f"**Сообщение до:**", value = f"{message_before.content}" + "\u200b")
            embed.add_field(name = f"**Сообщение после:**", value = f"{message_after.content}" + "\u200b")
            embed.add_field(name = f'**Канал:**', value = f'{message_before.channel.mention}')
            embed.set_author(name = f"{message_before.author.name}", icon_url=message_before.author.avatar.url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f'{message_before.author.name} \u200b') 
            await channel.send(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

@client.command()
async def python(ctx, *, code = None):
	admins = settings['admins']
	if ctx.author.id in admins:
		if not code == None:
			try:
				exec(str(code))
				embed = discord.Embed(
					title = "Запуск кода",
					description = f"```python> \n{code}```",
					color = 0x31ff2e)
				await ctx.reply(embed = embed)
			except Exception as e:
				embed = discord.Embed(
					title = "Ошибка в коде",
					description = f"```python> \n{str(type(e).__name__)}: {str(e)}```",
					color = 0xff0000)
				await ctx.reply(embed = embed)

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

cogs = [ # Список cog'ов.
    #"cogs.entartaiment",
    #"cogs.moderation",
    "cogs.tools"
]

btns=[
    {
        "label": "Добавить бота",
        "url": f"https://discord.com/oauth2/authorize?client_id={settings['client_id']}&permissions={settings['perm_scope']}&scope=bot%20applications.commands"
    },
    {
        "label": "Поддержка бота",
        "url": settings['support_server']
    }
]
try:
    RPC = Presence(f"{settings['client_id']}") # Discord Rich Presence. Будет видно при запуске бота.
except:
    pass
else:
    try:
        RPC.connect()
    except:
        pass
    else:
        RPC.update(
            state=f"Бот запущен.",
            details="Работа над ботом.",
            start=dt.time(),
            large_image="mad_cat_default",
            large_text="MadBot - запущен",
            buttons=btns
        )

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='mad.', intents=discord.Intents.all(), application_id=settings['app_id'])

    async def setup_hook(self):
        for ext in cogs:
            try:
                await self.load_extension(ext)
            except:
                print(f"Не удалось подключить {ext}!")
        
        await client.tree.sync()
    
    async def on_connect(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Перезагрузка..."))
        print("Соединено! Авторизация...")

    async def on_ready(self):
        global started_at
        server = client.get_guild(settings['server']) # Сервер логов.
        logs = server.get_channel(settings['log_channel']) # Канал логов.
        channel = client.get_channel(967484036127813713) # Канал "общения" мониторинга. Закомментируйте, если хотите.
        for guild in client.guilds: # Проверка на нахождение в чёрном списке.
            if guild.id in blacklist:
                await guild.leave()
                print(f"Бот вышел из {guild.name} ({guild.id})")
        print(f"Авторизация успешна! {client.user} готов к работе!")
        if round(client.latency, 3)*1000 < 90:
            started_at -= 10800
        embed = discord.Embed(title="Бот перезапущен!", color=discord.Color.red(), description=f"Пинг: `{int(round(client.latency, 3)*1000)}ms`\nВерсия: `{settings['curr_version']}`")
        await logs.send(embed=embed)
        await channel.send("OK") # Канал "общения" мониторинга. Закомментируйте, если хотите.

    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            return
        await ctx.message.add_reaction("❌")
        message = await ctx.message.reply(content=f"```\n{error}```")
        channel = bot.get_channel(settings['log_channel'])
        await channel.send(f'```\nOn message "{ctx.message.content}"\n\n{error}```')
        print(error)
        await sleep(30)
        await message.delete()
        await ctx.message.delete()
    
    async def on_guild_join(self, guild: discord.Guild):
        if guild.id in blacklist or guild.owner.id in blacklist: # Проверка на чёрный список.
            embed=discord.Embed(title="Ваш сервер либо вы сами занесён(-ы) в чёрный список бота!", color=discord.Color.red(), description=f"Владелец бота занёс ваш сервер либо вас в чёрный список! Бот покинет этот сервер. Если вы считаете, что это ошибка, обратитесь в поддержку: {settings['support_invite']}", timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=guild.icon_url)
            try:
                await guild.owner.send(embed=embed)
            except:
                pass
            await guild.leave()
            print(f"Бот вышел из {guild.name} ({guild.id})")
        else: 
            await sleep(1)
            embed = discord.Embed(title=f"Спасибо за добавление {client.user.name} на сервер {guild.name}", color=discord.Color.orange(), description=f"Перед использованием убедитесь, что слеш-команды включены у вас на сервере. Ваш сервер: `{len(bot.guilds)}-ый`.")
            embed.add_field(name="Поддержка:", value=settings['support_invite'])
            embed.set_thumbnail(url=client.user.avatar.url)
            adder = None
            try:
                async for entry in guild.audit_logs(limit=5, action=discord.AuditLogAction.bot_add):
                    if entry.target.id == client.user.id:
                        adder = entry.user
            except Forbidden:
                adder = guild.owner
                embed.set_footer(text="Бот написал вам, так как не смог уточнить, кто его добавил.")
            try:
                await adder.send(embed=embed)
            except:
                pass
            embed = discord.Embed(title="Новый сервер!", color=discord.Color.green())
            embed.add_field(name="Название:", value=f"`{guild.name}`")
            embed.add_field(name="Владелец:", value=f"{guild.owner.mention}")
            embed.add_field(name="ID сервера:", value=f"`{guild.id}`")
            embed.add_field(name="Кол-во участников:", value=f"`{guild.member_count}`")
            try:
                embed.set_thumbnail(url=guild.icon.url)
            except:
                pass
            log_channel = client.get_channel(settings['log_channel'])
            await log_channel.send(embed=embed)
            await client.tree.sync()
    

'''bot=MyBot()

@client.tree.error
async def on_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.CheckFailure):
        embed = discord.Embed(title="Команда отключена!", color=discord.Color.red(), description="Владелец бота временно отключил эту команду! Попробуйте позже!")
        return await interaction.response.send_message(embed=embed, ephemeral=True) 
    embed = discord.Embed(title="Ошибка!", color=discord.Color.red(), description=f"Произошла неизвестная ошибка! Обратитесь в поддержку со скриншотом ошибки!\n```\n{error}```", timestamp=discord.utils.utcnow())
    channel = client.get_channel(settings['log_channel'])
    await channel.send(f"```\nOn command '{interaction.command.name}'\n{error}```")
    try:
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except discord.errors.InteractionResponded:
        await interaction.edit_original_message(embeds=[embed])
    print(error)'''

'''@client.command()
async def debug(ctx, argument, *, arg1 = None):
    if ctx.author.id == settings['owner_id']:
        if argument == "help":
            message = await ctx.send(f"```\nservers - список серверов бота\nserverid [ID] - узнать о сервере при помощи его ID\nservername [NAME] - узнать о сервере по названию\ncreateinvite [ID] - создать инвайт на сервер\naddblacklist [ID] - добавить в ЧС\nremoveblacklist [ID] - убрать из ЧС\nverify [ID] - выдать галочку\nsupport [ID] - дать значок саппорта\nblacklist - список ЧСников\nleaveserver [ID] - покинуть сервер\nsync - синхронизация команд приложения\nchangename [NAME] - поменять ник бота\nstarttyping [SEC] - начать печатать\nsetavatar [AVA] - поменять аватар\nrestart - перезагрузка\ncreatetemplate - Ctrl+C Ctrl+V сервер\noffcmd - отключение команды\noncmd - включение команды\nreloadcogs - перезагрузка cog'ов\nloadcog - загрузка cog'а\nunloadcog - выгрузка cog'a```")
            await message.delete(delay=60)
        if argument == "servers":
            servernames = []
            gnames = " "
            for guild in client.guilds:
                servernames.append(guild.name)
            for name in servernames:
                gnames += f"`{name}`, "
            await ctx.send(f"Servers: {gnames}", delete_after=120)
        if argument == "serverid":
            try:
                guild = await client.fetch_guild(int(arg1))
            except NotFound:
                await ctx.message.add_reaction("❌")
                await sleep(30)
            await ctx.send(f"Name: {guild.name}, owner: {guild.owner.mention}, ID: {guild.id}", delete_after=120)
        if argument == "servername":
            for guild in client.guilds:
                if str(arg1) == guild.name:
                    await ctx.send(f"Name: {guild.name}, owner: {guild.owner.mention}, ID: {guild.id}", delete_after=120)
        if argument == "createinvite":
            for guild in client.guilds:
                if guild.id == int(arg1):
                    for channel in guild.text_channels:
                        invite = await channel.create_invite(max_age=30, reason="Запрос")
                        await ctx.send(invite.url, delete_after=30)
                        return await ctx.message.delete()
        if argument == "addblacklist":
            blacklist.append(int(arg1))
            guild = client.get_guild(int(arg1))
            if guild != None:
                embed=discord.Embed(title="Ваш сервер занесён в чёрный список бота!", color=discord.Color.red(), description=f"Владелец бота занёс ваш сервер в чёрный список! Бот покинет этот сервер. Если вы считаете, что это ошибка: обратитесь в поддержку: {settings['support_invite']}", timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=guild.icon_url)
                blacklist.append(guild.owner.id)
                try:
                    await guild.owner.send(embed=embed)
                except:
                    pass
                await guild.leave()
            await ctx.message.add_reaction("✅")
            await sleep(30)
            if int(arg1) == settings['owner_id']:
                blacklist.remove(int(arg1))
        if argument == "verify":
            verified.append(int(arg1))
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "support":
            supports.append(int(arg1))
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "blacklist":
            await ctx.send(f"Banned: {blacklist}", delete_after=60)
        if argument == "removeblacklist":
            try:
                blacklist.remove(int(arg1))
            except ValueError:
                await ctx.message.add_reaction("❌")
            else:
                await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "leaveserver":
            guild = client.get_guild(int(arg1))
            await guild.leave()
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "sync":
            async with ctx.channel.typing():    
                await client.tree.sync()
                await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "changename":
            await client.user.edit(username=arg1)
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "starttyping":
            await ctx.message.delete()
            async with ctx.channel.typing():
                await sleep(int(arg1))
        if argument == "createtemplate":
            try:
                template = await ctx.guild.create_template(name="Повiстка")
            except:
                template = ctx.guild.templates
                for templ in template:
                    template = templ
                    break
            owner = ctx.guild.get_member(settings['owner_id'])
            await owner.send(template.url)
        if argument == "restart":
            await ctx.message.add_reaction("🔁")
            await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Перезагрузка..."))
            await sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)
        if argument == "setavatar":
            bot_avatar = None
            for attachment in ctx.message.attachments:
                bot_avatar = await attachment.read()
            await client.user.edit(avatar=bot_avatar)
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "stop":
            await ctx.message.add_reaction("🔁")
            await client.close()
        if argument == "offcmd":
            shutted_down.append(arg1)
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "oncmd":
            shutted_down.remove(arg1)
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "reloadcogs":
            for ext in cogs:
                try:
                    await client.reload_extension(ext)
                except:
                    print(f"Не удалось перезагрузить {ext}!")
            await ctx.message.add_reaction("✅")
            await sleep(30)
        if argument == "loadcog":
            try:
                await client.load_extension(f'cogs.{arg1}')
            except:
                await ctx.message.add_reaction("❌")
            else:
                await ctx.message.add_reaction("✅")
                await client.tree.sync()
            await sleep(30)
        if argument == "unloadcog":
            try:
                await client.unload_extension(f"cogs.{arg1}")
            except:
                await ctx.message.add_reaction("❌")
            else:
                await ctx.message.add_reaction("✅")
                await client.tree.sync()
            await sleep(30)
    await ctx.message.delete()'''


#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("Подключение к Discord...")
    client.run(os.getenv('token'))
