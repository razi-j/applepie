import discord
from discord import Member, app_commands
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sync(self, ctx):
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(fmt)} commands.")
    
    
    @commands.hybrid_command()
    async def ping(self, ctx):
        first = await ctx.send("Pong")
        await first.edit(content=f"Pong\n\n\n{round(self.client.latency * 1000)}ms")
    
    @commands.hybrid_command(name='test',description='Test Command')
    @app_commands.guilds(1114623410950115508)
    async def test(self,ctx: commands.Context):
        await ctx.send("Hybrid Command", ephemeral=True)
    #@commands.tree.command()
    #async def ping(self, interaction: discord.Interaction):
    #    await interaction.response.send_message(f"Pong {interaction.user.mention}", ephemeral=True)

    
async def setup(client):
    await client.add_cog(fun(client))