import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
#intents.message_content = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Sync'd {len(synced)} commands.")
    except Exception as e:
        print(e)

@bot.tree.command()
async def hello(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Hello!")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

bot_token = os.getenv('DISCORD_TOKEN')
bot.run(bot_token)