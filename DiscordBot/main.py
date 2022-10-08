import discord
from discord.ext import commands            # >>> python -m pip install -U discord.py
from config import settings
from weathercommand import *
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)
#print('JarvisBot in da house!')
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send('Pong!')

@bot.command()
async def matha(ctx: commands.Context):
    await ctx.send('fucka!')


@bot.command()
async def weather(ctx: commands.Context):
    result = request_current_weather(1496747)
    await ctx.send(result)

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def roll(ctx, *arg):
    await ctx.reply(random.randint(0, 100))

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
