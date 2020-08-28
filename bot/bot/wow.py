import random
import discord
from discord.ext import commands

class Wow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll",help="Roll from 1 to a specified number (default 100)")
    async def roll(self, ctx, max=100):
        await ctx.send(random.randrange(max))

def setup(bot):
    bot.add_cog(Wow(bot))