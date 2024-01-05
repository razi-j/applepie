import discord
from discord import app_commands
from discord.ext import commands

class HELP(commands.Cog):
    def __init__(self,client) -> None:
        self.client = client
    

    @commands.hybrid_command(name='help', description="Sends Help!")
    @app_commands.guilds(1114623410950115508, )
    async def help(self,ctx):
        helpembed = discord.Embed(
                title="**Apple Pie Commands**",
                colour=discord.Colour.dark_green()
            )
        helpembed.set_footer(text="Kindly use these commands in servers where Apple Pie exists! Thank You!")
        helpembed.set_thumbnail(url="https://kristineskitchenblog.com/wp-content/uploads/2021/04/apple-pie-1200-square-592-2.jpg")
        helpembed.add_field(name="Basic Information", value="Hi! I'm a bot created by <@741364782581416007>. Ask me to do stuff by using `.` as a prefix!")
        await ctx.send(embed=helpembed)

async def setup(client):
    await client.add_cog(HELP(client))