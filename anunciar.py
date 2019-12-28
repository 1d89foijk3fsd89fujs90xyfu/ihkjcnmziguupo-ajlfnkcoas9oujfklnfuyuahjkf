import discord
import random
from discord.ext import commands
import asyncio

channel_id = "UCJnYvI7s9PwirJSU0okv8JA"
api_key = os.environ["API_KEY"]
lol = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}")
d = json.loads(lol)
oi = d["items"]["subscriberCount"]

class anunciar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.group(pass_context=True)
    async def subs(self,ctx):
        embed=discord.Embed(title="Subs", description=f"O zFayser tem neste momento **{oi}**", color=0xf22b1d)
        await ctx.send(embed=embed)
        
    @commands.guild_only()
    @commands.group(pass_context=True)
    async def anunciar(self,ctx):
        if not ctx.author.guild_permissions.manage_guild:
            if ctx.invoked_subcommand is None:
                embed=discord.Embed(title="🚫Sem permissoes🚫", description="**Sabia que - só as pessoas que tem permissoes `manage_guild` tem asseso ao comando?\nE você não tem essa permzinha aí**")
                await ctx.send(embed=embed)
        if ctx.author.guild_permissions.manage_guild:
            if ctx.invoked_subcommand is None:
                embed=discord.Embed(title="Anunciar", description="Anuncie qualquer coisa", color=0xffff00)
                embed.add_field(name=f"{ctx.prefix}anunciar pv [sua messagem]", value="envie uma messagem para todos os usuarios", inline=False)
                embed.add_field(name=f"{ctx.prefix}anunciar canal [#canal] [sua messagem]", value="envie uma messagem para um devido canal", inline=True)
                return await ctx.send(embed=embed)

    @commands.guild_only()
    @anunciar.command(pass_context=True)
    async def pv(self,ctx, *, msg=None):
        if not ctx.author.guild_permissions.manage_guild:
            embed=discord.Embed(title="🚫Sem permissoes🚫", description="**Sabia que - só as pessoas que tem permissoes `manage_guild` tem asseso ao comando?\nE você não tem essa permzinha aí**")
            return await ctx.send(embed=embed)
        if ctx.author.guild_permissions.manage_guild:
            if msg is None:
                return await ctx.send("Desculpa mas voce precisa de ter pelo menos uma messagem")
            if msg is not None:
                a = []
                r = []
                pessoas = ctx.author.name
                guild = ctx.guild.name
                x = ctx.guild.members
                fucl = await ctx.send("Processando usuarios...")
                await asyncio.sleep(1.5)
                await fucl.delete()
                ldksla = await ctx.send("Enviando messagens")
                await asyncio.sleep(1.5)
                await ldksla.delete()
                for member in x:
                    a.append(member.id)
                    b = random.choice(a)
                    user = self.bot.get_user(b)
                    rerettr = print(user)
                    if user.bot is True:
                        a.remove(b)
                    if user.bot is False:
                        try:
                            await user.send(f"`🎉Anuncio de {pessoas}🎉`\n\n{msg}\n")
                            kkk = f"Foi enviada messagem para {user.name}"
                            lixo = await ctx.send(kkk)
                            await asyncio.sleep(1)
                            await lixo.delete()
                            r.append(b)
                            a.remove(b)
                        except Exception as e:
                            a.remove(b)
                await ctx.send("Foi tudo enviado!!")

    @anunciar.command(pass_context=True)
    @commands.guild_only()
    async def canal(self,ctx,ch:discord.TextChannel=None,*,msg=None):
        if not ctx.author.guild_permissions.manage_guild:
            embed=discord.Embed(title="🚫Sem permissoes🚫", description="**Sabia que - só as pessoas que tem permissoes `manage_guild` tem asseso ao comando?\nE você não tem essa permzinha aí**")
            return await ctx.send(embed=embed)
        if ctx.author.guild_permissions.manage_guild:
            try:
                if ch is None:
                    return await ctx.send("Por favor mencione o canal")
                if msg is None:
                    return await ctx.send("Por favor digite uma messagem")
                if ch and msg is not None:
                    await ch.send(f"{msg}")
                    await ctx.send("Messagem enviada")
            except Exception as e:
                await ctx.send('Mencione um canal valido ou um canal em que EU tenha permissoes')

def setup(bot):
    bot.add_cog(anunciar(bot))
