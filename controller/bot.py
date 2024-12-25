from discord.ext import commands
from discord import Intents

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

async def start(token):
    await bot.start(token)

async def stop():
    await bot.close()