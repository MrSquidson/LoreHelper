import discord
from discord import app_commands
from discord.ext import commands
from discord import Member
import datetime
from discord.ext.commands import has_permissions, MissingPermissions


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True



class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print('Loaded??') 
    
    # Simple test command
    @app_commands.command(
        name="commandname",
        description="My first application Command",
)
    async def first_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

async def setup(bot) -> None:
    await bot.add_cog(Moderation(bot))
    # await bot.add_cog('treeCMD') # only to remove class