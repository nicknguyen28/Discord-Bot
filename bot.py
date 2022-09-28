# bot.py
import os
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

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.reload_extension(f'cogs.{filename[:-3]}')
    await ctx.send('`Reloaded!`')

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('`Shutdown!`')
    exit()

bot.run(TOKEN)