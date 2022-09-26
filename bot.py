# bot.py
import os
import discord
import random
from discord.ext import commands
from googlesearch import search
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix='$', intents = intent)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def lookup(ctx, *query):
    queryWhole=' '.join(query)
    author = ctx.author.mention
    await ctx.channel.send(f"Here is the top google search for {queryWhole} {author} !")
    async with ctx.typing():
        for j in search(queryWhole, tld="co.in", num=1, stop=1, pause=2): 
            await ctx.send(f"\n:arrow_right: {j}")
            return

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.channel.send(f"Shutting down!")
    exit()

@bot.command()
async def randnum(ctx, range1=int(0), range2=int(0)):
    if (range2 != 0 and range2 <= range1):
        await ctx.channel.send(f"Input a valid range!")
        return
    
    if (range1 == 0 and range2 == 0):
        await ctx.channel.send(f"{random.randint[1,10]}!")
        return

    await ctx.channel.send(f"{random.randint[range1, range2]}!")
    return

bot.run(TOKEN)