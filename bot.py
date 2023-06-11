import discord
from discord import guild
from discord.abc import GuildChannel
from discord.ext import commands
from discord.member import Member
import os
import asyncio

#from key import token

with open("key", "r") as f:
    key = f.readline()

intents = discord.Intents.default()
intents.members = True

cogs = []
for f in os.listdir('./cogs'):
    if f.endswith('.py'):
        cogs.append("cogs."+f[:-3])

bot = commands.Bot(command_prefix=["."], intents=intents)

async def load():
    
    for f in os.listdir('./cogs'):
        if f.endswith('.py'):
            await bot.load_extension(f'cogs.{f[:-3]}')
            print("cog loaded")

async def main():
    await load()
    await bot.start(key)        

asyncio.run(main())