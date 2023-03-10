import os
import discord
import platform
import settings
from discord.ext import commands


def run():

    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents)

    release = platform.release()[:5]

    @bot.event
    async def on_ready():
        print("-" * 45)
        print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
        print(f"discord.py API Version: {discord.__version__}")
        print(f"Python Version: {platform.python_version()}")
        print(f"Running on {platform.system()} {release} ({os.name})")
        print("-" * 45)

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()
