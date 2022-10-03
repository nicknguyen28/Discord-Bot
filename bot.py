# bot.py
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
bot = commands.Bot(command_prefix = '$', intents = intent)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.reload_extension(f'cogs.{filename[:-3]}')
    embed = discord.Embed(description = '**Reloaded!**')
    await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    embed = discord.Embed(description = '**Shutdown!**')
    await ctx.send(embed = embed)
    exit()

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())