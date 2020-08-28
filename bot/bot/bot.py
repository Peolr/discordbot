# bot.py
import os
import random
import data


database = data.BotDB()

import discord
from discord.ext import commands
from dotenv import load_dotenv

extensions = ["wow","poll"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def is_command(m, cmd):
    if m.find(cmd, 0, len(cmd)) > -1:
        return True
    return False


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


    for guild in bot.guilds:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )
        database.checkserver(guild)



@bot.command(name="fat",hidden=True)
async def fat(ctx):

    response = f"We know, {ctx.author.name}."
    await ctx.send(response)

#https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f"loaded extension: {extension}")
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(TOKEN)
    print("running")
