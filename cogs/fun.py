import discord
from discord import Member, app_commands
from discord.ext import commands
import time

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(with_app_command=True)
    async def ping(self, ctx):
        first = await ctx.send("Pong")
        await first.edit(content=f"Pong\n\n\n{round(self.client.latency * 1000)}ms")
    
    @commands.hybrid_command(with_app_command=True)
    #@app_commands.guilds(1114623410950115508)
    async def test(self,ctx: commands.Context):
        await ctx.send("Hybrid Command", ephemeral=True)
    #@commands.tree.command()
    #async def ping(self, interaction: discord.Interaction):
    #    await interaction.response.send_message(f"Pong {interaction.user.mention}", ephemeral=True)
    @commands.hybrid_command(with_app_command=True)
    async def hack(self,ctx,target:discord.Member = None):
        if target == None:
            target = ctx.author
        virus = "NGGYU"
        initial_message = await ctx.send(f"``[▓                    ] / {virus}-virus.exe Packing files.``")
        list = (
            f"``[▓▓▓▓                   ] - {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓                  ] - {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓                 ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓                ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓               ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓              ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓             ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓            ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓          ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] | {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            "``Injecting virus... \``",
            f"``Successfully Injected {virus}-virus.exe into {target.name}``",
            )
        for i in list:
            time.sleep(0.15)
            await initial_message.edit(content=i)
        embed = discord.Embed()
        embed.set_image(url="https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")
        await target.send(embed=embed)
    
async def setup(client):
    await client.add_cog(fun(client))
