import discord
import logging
import os
from discord.ext import commands

intents = discord.Intents.default()
#intents.message_content = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.info(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        logging.info(f"Sync'd {len(synced)} commands.")
    except Exception as e:
        logging.error(e)

@bot.tree.command(name='hello')
async def say_hello(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Hello!")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

if __name__ == "__main__":
    bot_token = os.getenv('DISCORD_TOKEN')
    logging.warn("=== RUNNING BOT ===")
    bot.run(bot_token)