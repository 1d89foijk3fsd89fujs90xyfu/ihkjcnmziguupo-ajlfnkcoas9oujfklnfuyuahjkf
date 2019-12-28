import discord
from discord.ext import commands
import os
import requests
import urllib.request
import json
import asyncio
import pymongo
from pymongo import MongoClient

bot = commands.Bot(command_prefix='?', status=discord.Status.idle, activity=discord.Game("Ligando o bot"))

admin = 457914780876013569
COR = 0x34363c
url = os.environ["LOL"]
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
        await bot.change_presence(status=None, activity=discord.Game("Canal: zFayser"))
        await asyncio.sleep(30)
        await bot.change_presence(status=None, activity=discord.Game(f"Somos agora {oi} inscritos!!"))
        await asyncio.sleep(30)

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def recarregar(ctx,cog=None):
    if cog is None:
        return await ctx.send("Mencione umas das extençoes ai em baixo\n\n```yml\nanunciar\n```")
    if cog is not None:
        try:
            bot.load_extension(f'{cog}')
            bot.unload_extension(f'{cog}')
            bot.load_extension(f'{cog}')
            embed=discord.Embed(title="Extenção recarregada", color=COR)
            embed.description = f"A extenção {cog}.py foi recarregada"
        except Exception as e:
            embed=discord.Embed(title="Erro", color=COR)
            embed.description= f"A extenção {cog} não foi carregada devido ao erro \n\n```yml\n{e}\n```"
        await ctx.send(embed=embed)
               
        
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Falha ao carregar a extenção {}  \n{}'.format(extension, exc))

    bot.run(TOKEN)
