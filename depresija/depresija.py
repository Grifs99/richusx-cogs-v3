import json
import os
import re
from redbot.core import commands
import discord
# import urllib.request

BaseCog = getattr(commands, "Cog", object)

class Depresija(BaseCog):
    """Reply with today's name-days"""

    def __init__(self, bot):
        self.bot = bot
        self.emoji = None

        for i in bot.emojis:
            if "depresija" in i.name:
                self.emoji = i
                break

    @commands.Cog.listener()
    async def on_message(self, msg) -> None:
        if msg.author.id == 141242913958002688:
            if "depresija" in msg.content:
                await msg.channel.send(content=f"{msg.author.mention} {self.emoji}")
