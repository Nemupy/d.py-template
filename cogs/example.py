import discord
from discord.ext import commands
from discord import app_commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="example", description="This is an example command.")
    async def server(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello! This is an example command response.")


async def setup(bot: commands.Bot):
    await bot.add_cog(ExampleCog(bot))
