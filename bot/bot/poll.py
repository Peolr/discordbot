import random
import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll",help="setup a poll")
    async def poll(self, ctx):

        end_creation = False

        def check(m):
            if m.author==ctx.author and m.channel == ctx.channel:
                return True

        while (not end_creation):
            msg = await self.bot.wait_for('message', check=check)
            if msg.content == "end":
                end_creation = True

        print("ended poll")
def setup(bot):
    bot.add_cog(Poll(bot))