import discord
import asyncio
from discord import Member, app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions, bot_has_permissions


class adminCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def sync(self, ctx):
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"Synced {len(fmt)} commands.")
 
    @commands.hybrid_command(name='kick',with_app_command=True, description='Kicks people off the server!')
    @has_permissions(kick_members=True)
    @bot_has_permissions(kick_members=True)
    # @app_commands.guilds(1114623410950115508)
    async def kick(self, ctx, member:Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send("Apple Pie has Successfuly **Kicked** {} for: {}".format(member, reason), ephemeral=True)
   
    @commands.hybrid_command(name='ban',with_app_command=True, description='Bans people from the server!')
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    # @app_commands.guilds(1114623410950115508)
    async def ban(self, ctx, member:Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send("Apple Pie has Successfully Banned {} for: {}".format(member, reason))

    @commands.hybrid_command(name='clear',with_app_command=True, description='Clears Messages! (default 5)')
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    # @app_commands.guilds(1114623410950115508)
    async def clear(self, ctx, amount:int=5):
        await ctx.defer(ephemeral=True)
        # async with ctx.typing():
        await ctx.channel.purge(limit=amount+1)
            # await ctx.defer(f"cleared {amount} messages!",ephemeral=True)
            # await asyncio.sleep(5)
        await ctx.send(f"cleared {amount} messages!")

async def setup(client):
    await client.add_cog(adminCommand(client))
    
