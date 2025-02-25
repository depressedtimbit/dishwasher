import discord
from discord.ext.commands import Cog
import json
import re
import config
import datetime
from helpers.checks import check_if_staff
from helpers.configs import get_misc_config, get_staff_config


class Reply(Cog):
    """
    A cog that stops people from ping replying people who don't want to be.
    """

    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None

    async def handle_message_with_reference(self, message):
        reference_author = message.reference.resolved.author
        if (
            message.author.bot
            or not message.guild
            or not message.guild.get_member(reference_author.id)
            or reference_author.id == message.author.id
            or not get_misc_config(message.guild.id, "noreply_role")
            or reference_author.get_role(
                get_misc_config(message.guild.id, "noreply_role")
            )
            is None
        ):
            return

        staff_role = get_staff_config(message.guild.id, "staff_role")
        if staff_role and message.author.get_role(staff_role):
            return

        if reference_author in message.mentions:
            await message.add_reaction("🗞️")
            await message.reply(
                file=discord.File("assets/noreply.png"),
                delete_after=15,
                mention_author=True,
            )

    @Cog.listener()
    async def on_message(self, message):
        await self.bot.wait_until_ready()

        if message.reference and message.type == discord.MessageType.reply:
            await self.handle_message_with_reference(message)


async def setup(bot):
    await bot.add_cog(Reply(bot))
