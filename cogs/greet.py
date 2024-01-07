import discord
from discord import Member
from discord.ext import commands
from discord.utils import get
import mariadb

class greet(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Ready")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply("OOPS! That command doesn't exist!", delete_after=10)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"Hey {ctx.author.mention}!! You don't have the permissions to do that command!", delete_after=10)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Hey {ctx.author.mention}!! Check `.help`, you're missing some parameters for this command.", delete_after=10)
        else:
            await ctx.reply(f"Well... this is awkward... there's an error and I can't do that command! {error}", delete_after=10)
    
    @commands.Cog.listener()
    async def on_member_join(self, member:Member):
        if member.guild.system_channel:
            channel = member.guild.system_channel
        if member.avatar:
            pic = member.avatar.url
        else:
            pic = member.default_avatar.url
        
        greeter = discord.Embed(
            colour=discord.Color.dark_green()
        )
        greeter.set_thumbnail(url=pic)
        greeter.add_field(name="**WELCOME**", value=f"**Hello {member.mention}!!** Welcome to {member.guild.name}!", inline=False)
        greeter.add_field(name= "***RULES***", value=None, inline=False)
        greeter.add_field(name= "**1. Be respectful**", value="Respect all users! Treat them the way you want to be treated.", inline=False)
        greeter.add_field(name= "**2. No NSFW Content**", value='No P-word, No H-word, and NO GORE. You will be banned from this server. However, mild nsfw jokes are allowed! No stepping over the line!', inline=False)
        greeter.add_field(name= "**3. DON'T PING EVERYONE**", value="Don't ping everyone. Don't mention someone too much.", inline=False)
        greeter.add_field(name= "**4. DON'T SPAM**", value="DON'T! JUST. DON'T!", inline=False)
        greeter.set_footer(text="Hope you enjoy your stay!")
        await channel.send(embed=greeter)
    
async def setup(client):
    await client.add_cog(greet(client))
