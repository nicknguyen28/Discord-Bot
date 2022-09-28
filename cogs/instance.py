import random
import discord
from discord.ext import commands
from googlesearch import search

class Instance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Instance has been loaded!')

    @commands.command()
    async def lookup(self, ctx, *query):
        queryWhole=' '.join(query)
        author = ctx.author.mention
        await ctx.send(f"Here is the top 3 google searches for {queryWhole} {author} !")
        async with ctx.typing():
            try:
                for j in search(queryWhole, tld="co.in", num=3, stop=3, pause=2): 
                    await ctx.send(f"\n:arrow_right: {j}")
            except:
                return
    
    @commands.command()
    async def randnum(self, ctx, range1=int(0), range2=int(0)):
        if (range2 != 0 and range2 <= range1):
            await ctx.channel.send(f"Input a valid range!")
            return
        
        if (range1 == 0 and range2 == 0):
            await ctx.channel.send(f"{random.randint(1,10)}!")
            return

        await ctx.channel.send(f"{random.randint(range1, range2)}!")

async def setup(bot):
    await bot.add_cog(Instance(bot))