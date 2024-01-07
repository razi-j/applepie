import discord
import aiomysql 
import random
from discord.utils import get
from discord.ext import commands
from discord import Member, app_commands

class afk(commands.Cog):
    def __init__(self,client):
        self.client = client 
          
    @commands.Cog.listener()
    async def on_ready(self):
        try:
            setattr(self.client, 'db', await aiomysql.connect(
            user = 'root', password = 'root', host='localhost',
            port = 3306, db='afk'))
            print('Connected')
            async with self.client.db.cursor() as cur:
                await cur.execute("CREATE TABLE IF NOT EXISTS afk(user VARCHAR(255), display_name VARCHAR(255), guild VARCHAR(255), reason TEXT)")

        except Exception as e:
            print(f"Failed to Connect to Mariadb: {e}") 

    @commands.hybrid_command(with_app_command=True)
    async def afk(self, ctx, *, reason=None):
        if reason==None:
            reason = "No Reason! Just went AFK!" 
        async with self.client.db.cursor() as cur:
            await cur.execute("SELECT reason from afk WHERE user=%s AND guild=%s", (ctx.author.id, ctx.guild.id))
            data = await cur.fetchone()
            print(data)
            if data:
                if data[0] == reason:
                    print(data[0])
                    await ctx.send("You are already afk for the same reason!")
                else:
                    await cur.execute('UPDATE afk SET reason=%s WHERE user=%s AND guild=%s',(reason, ctx.author.id, ctx.guild.id))
                    await ctx.send(f"{ctx.author.mention} is now afk!\nReason: `{reason}`")
            else:
                await cur.execute("INSERT INTO afk (user,display_name,guild,reason) VALUES (%s, %s, %s, %s)",(ctx.author.id, ctx.author.display_name, ctx.guild.id, reason))
                if ctx.author.id != ctx.guild.owner_id:
                    await ctx.author.edit(nick = f"[AFK] {ctx.author.display_name}")
                await ctx.send(f"{ctx.author.mention} is now afk!\nReason: `{reason}`")
                role = get(ctx.guild.roles, name="AFK")
                await ctx.author.add_roles(role)

        await self.client.db.commit()

async def setup(client):
    await client.add_cog(afk(client))
