import discord
from discord.ext import commands
import os
# noinspection PyShadowingNames
def __init__(self, bot commands.Bot)
    self.bot = bot


bot = commands.Bot(command_prefix=%,
                   case_insensitive=True, owner_id=)

token = process.env.arcadia
clear = lambda os.system('cls')

@bot.event
async def on_ready()
    print('Ready')

@bot.command()
async def status(ctx)
    embed = discord.Embed(color=0x7FFF00, title=Bitizy is online)
    await ctx.send(embed=embed)
	
@bot.command()
async def test(ctx)
    await ctx.send('Test Command by Xenic')	

bot.run(token)
bot.login(process.env.token);
