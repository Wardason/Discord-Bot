import random
from discord.ext import commands

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Gives random number between 1 and 100")
    async def random(self, ctx):
        n = random.randrange(1, 101)
        await ctx.send(n)

    @commands.command(brief="Random number between 1 and 10")
    async def dice(self, ctx):
        n = random.randrange(1, 10)
        await ctx.send(n)

    @commands.command(brief="Either Heads or Tails")
    async def coin(self, ctx):
        n = random.randint(0, 1)
        await ctx.send("Heads" if n == 1 else "Tails")



def setup(bot):
    bot.add_cog(Gamble(bot))