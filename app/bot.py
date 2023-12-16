import discord
import os
from discord.ext import commands

# Set command prefix for the bot
bot = commands.Bot(command_prefix='!')

# Event listener for when the bot has switched from offline to online.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command to respond to "!hello"
@bot.command(name='hello', help='Responds with Hello World!')
async def hello(ctx):
    await ctx.send('Hello World!')

# Run the bot with the token from environment variable
bot_token = os.getenv('DISCORD_TOKEN')
bot.run(bot_token)