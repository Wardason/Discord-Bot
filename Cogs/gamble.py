import random
from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Gives random number between 1 and 100")
    async def random(self, ctx):
        no = random.randrange(1, 101)
        await ctx.send(no)

    @commands.command(brief="Random number between 1 and 10")
    async def dice(self, ctx):
        no = random.randrange(1, 6)
        await ctx.send(no)
def setup(bot):
    bot.add_cog(Gamble(bot))
