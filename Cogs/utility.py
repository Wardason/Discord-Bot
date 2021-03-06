from discord.ext import commands
from aiohttp import request
import wikipedia
import discord
import random


class Fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx, animal: str):
        if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):

            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

            async with request('GET', image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]
                else:
                    image_link = None

            async with request('GET', fact_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    embed = discord.Embed(title=f"{animal.title()} fact",
                                          description=data["fact"],
                                          color=random.randint(0, 0xffffff))
                    if image_link is not None:
                        embed.set_image(url=image_link)

                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"API returned a {response.status} status.")
        else:
            await ctx.send("No facts are available for that animal")

    @commands.command(name="wiki")
    async def wikipedia(self, ctx, question1: str, question2=None):
        if question2 is None:
            output = wikipedia.summary(question1, sentences=2)
            await ctx.send(output)
        else:
            question = question1 + question2
            output2 = wikipedia.summary(question, sentences=2)
            await ctx.send(output2)


def setup(bot):
    bot.add_cog(Fact(bot))
