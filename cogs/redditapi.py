import os
import random
import discord
import asyncpraw
from discord.ext import commands

reddit = asyncpraw.Reddit(client_id = os.getenv('REDDIT_USE_SCRIPT'),
                        client_secret = os.getenv('REDDIT_TOKEN'),
                        user_agent = 'Windows (by u/Nguyen_Bot)')
                        # username = os.getenv('REDDIT_USER'),
                        # password = os.getenv('REDDIT_PASS'))

class RedditAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        subreddit = await reddit.subreddit('memes')
        posts = []
        async for post in subreddit.hot(limit = 200):
            posts.append(post)
        randomPost = random.choice(posts)
        embed = discord.Embed(title = f'__{randomPost.title}__', color = 11027200, url = randomPost.url)
        embed.set_image(url = randomPost.url)
        await ctx.send(embed = embed)
        return

async def setup(bot):
    await bot.add_cog(RedditAPI(bot))
    print('RedditAPI has been loaded!')