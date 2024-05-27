import discord
from discord import app_commands
from discord.ext import commands
from discord import Member
import datetime
import time
from discord.ext.commands import has_permissions, MissingPermissions
import math
import typing


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
interaction = discord.Interaction

startDate = 1711929600

months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

async def floorToQuarter(number):
    return math.floor((number) * 100 / 25) 

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print('Loaded??') 
    
#     # Simple test command
#     @app_commands.command(
#         name="commandname",
#         description="My first application Command",
# )
#     async def first_command(self, interaction: discord.Interaction):
#         await interaction.response.send_message("Hello!")

    @app_commands.command(
        name="loredate",
        description="Calculate a loredate from a Date",
)
    @app_commands.describe(
        day="Day of the month"
    )
    @app_commands.describe(
        month='Month using 1,2,3...'
    )
    @app_commands.describe(
        year='Full year i.e. 1984 or 2024'
    )
    async def loredate(self, interaction: discord.Interaction, day: typing.Optional[int], month:typing.Optional[str], year: typing.Optional[int]):
        try:
            if month.isdigit():
                month = int(month)
        except:
            if month in months:
                month = months.index(month) + 1
        if month == None:
            month = datetime.datetime.today().month
        if day == None:
            day = datetime.datetime.today().day

        if year == None:
            year = 2024
        try:
        # If month is a string, convert it to a number
            if isinstance(month, str):
                month = datetime.datetime.strptime(month, '%B').month
        
        # Create a datetime object from the provided day, month, and year
            date = datetime.datetime(year, month, day)
            print(date)
        
        # Convert the datetime object to a Unix timestamp
            unix_time = time.mktime(date.timetuple())
        except  ValueError as e:
            return f"Error: {e}"

        if unix_time < (startDate - (24*60*60)):
            await interaction.response.send_message("Dates before April 1st 2024 Fall outside the scope of AU")

        cur_time = (((unix_time - startDate) / 86400) / 4)
        loreYear = math.floor(cur_time)+1
        seasons = ['Winter','Spring', 'Summer','Fall']
        cur_season = await floorToQuarter(cur_time - loreYear) +1
        
        await interaction.response.send_message(f'{seasons[cur_season]} of {loreYear + 50} AU') 

async def setup(bot) -> None:
    await bot.add_cog(Moderation(bot))
    # await bot.add_cog('treeCMD') # only to remove class