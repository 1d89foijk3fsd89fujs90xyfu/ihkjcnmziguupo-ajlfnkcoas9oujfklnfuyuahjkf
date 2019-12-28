import discord
from discord.ext import commands
import os
import json
import asyncio

bot = commands.Bot(command_prefix='?', status=discord.Status.idle, activity=discord.Game("Ligando o bot"))

startup_extensions = ["anunciar", "subs"]
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
        await asyncio.sleep(10)
        await bot.change_presence(status=None, activity=discord.Game(f"Somos agora {subs} | "))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Falha ao carregar a extenção {}  \n{}'.format(extension, exc))

    bot.run(TOKEN)
