import discord
from discord.ext import commands
import os
import requests
import urllib.request
import json
import asyncio
import pymongo
from pymongo import MongoClient

prefixo = "?"
bot = commands.Bot(case_insensitive=True, command_prefix=prefixo, status=discord.Status.idle, activity=discord.Game("Recarregando o bot"))
bot.remove_command("help")

channel_id = "UCJnYvI7s9PwirJSU0okv8JA"
key = os.environ["API_KEY"]
data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+channel_id+"&key="+key).read()
oi = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

startup_extensions = ["anunciar"]
TOKEN = os.environ["ACCESS_TOKEN"]

@bot.event
async def on_ready():
    print("----------------")
    print("Logado como:")
    print("Nome: {}".format(str(bot.user.name)))
    print("Id : {}".format(str(bot.user.id)))
    print("Discord.py versao : " + str(discord.__version__))
    print("----------------")
    while True:
        await bot.change_presence(status=None, activity=discord.Game("Increvam-se no canal do meu dono -> zFayser <-"))
        await asyncio.sleep(30)
        await bot.change_presence(status=None, activity=discord.Game(f"Oi agora o meu dono tem {oi} inscritos!!"))
        await asyncio.sleep(30)
                  
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Falha ao carregar a extenção {}  \n{}'.format(extension, exc))

    bot.run(TOKEN)
