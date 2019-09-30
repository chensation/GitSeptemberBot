import discord
from discord.ext import commands

# TODO Change Ping and name to your cog name
class Cu(commands.Cog, name='Cu'):
    """Classic Ping->Pong example"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Unloads and then loads an extension"""
        # Send when the user says !ping
        await ctx.send("Pong")

    @commands.command()
    async def heho(self, ctx):
        await ctx.message.channel.send(f"{ctx.author} heed a ho in {ctx.channel.name}.")


def setup(bot):
    # Tell the bot about our cog
    # TODO Change Ping to your class name
    bot.add_cog(Cu(bot))
