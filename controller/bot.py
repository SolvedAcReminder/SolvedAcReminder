from discord.ext import commands
from discord import Intents
import requests
from bs4 import BeautifulSoup
import re

bot = commands.Bot(command_prefix='$', intents=Intents.all())
prefix = '$'

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("HELLO")

    if message.content.startswith("$user"):
        args = message.content.split()
        response = requests.get(f"https://solved.ac/api/v3/user/grass?handle={args[1]}&topic=default")
        print(response.json())
        userInfo = requests.get("https://solved.ac/api/v3/user/show?handle=" + args[1])
        await message.channel.send(response.json()["currentStreak"])

async def start(token):
    await bot.start(token)

async def stop():
    await bot.close()
