import discord
from discord.ext import commands
import os
import asyncio
import mariadb

with open("key", "r") as f:
    key = f.readline()

intents = discord.Intents.all()
intents.members = True

cogs = []
for f in os.listdir('./cogs'):
    if f.endswith('.py'):
        cogs.append("cogs."+f[:-3])

bot = commands.Bot(command_prefix=["."], intents=intents, application_id='1114548342396047451')
bot.remove_command('help')

async def load():
    
    for f in os.listdir('./cogs'):
        if f.endswith('.py'):
            print(f[:-3])
            await bot.load_extension(f'cogs.' + f[:-3])
            print("cog loaded")

async def main():
    await load()
    await bot.start(key)

asyncio.run(main())
