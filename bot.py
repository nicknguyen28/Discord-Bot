# bot.py
import os
import discord
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

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.channel.send(f"Shutting down!")
    exit()

bot.run(TOKEN)