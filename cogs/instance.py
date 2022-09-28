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
        author = ctx.author.name
        numSearches = 5
        description = f'**Here are the top {numSearches} google searches for {queryWhole} @{author}!**\n'
        async with ctx.typing():
            try:
                for j in search(queryWhole, tld = 'co.in', num = numSearches, stop = numSearches, pause = 2):
                    description += f'\n:arrow_right: {j}\n'
                embed = discord.Embed(description = description, color = 2123412)
                await ctx.send(embed=embed)
            except:
                return
    
    @commands.command()
    async def randnum(self, ctx, range1 = int(0), range2 = int(0)):
        if (range2 != 0 and range2 <= range1):
            await ctx.channel.send(f'Input a valid range!')
            return
        
        if (range1 == 0 and range2 == 0):
            await ctx.channel.send(f'{random.randint(1, 10)}!')
            return

        await ctx.channel.send(f'{random.randint(range1, range2)}!')

async def setup(bot):
    await bot.add_cog(Instance(bot))