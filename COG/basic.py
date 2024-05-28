import discord
from discord import app_commands
from discord.ext import commands
import datetime
import time
import math
import typing

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
interaction = discord.Interaction

startDate = 1711929600  # April 1, 2024

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded??')

    @app_commands.command(
        name="loredate",
        description="Calculate a loredate from a Date",
    )
    @app_commands.describe(
        day="Day of the month",
        month="Month using 1,2,3...",
        year="Full year i.e. 1984 or 2024"
    )
    async def loredate(self, interaction: discord.Interaction, day: typing.Optional[int], month: typing.Optional[str], year: typing.Optional[int]):
        try:
            if month.isdigit():
                month = int(month)
        except:
            if month in months:
                month = months.index(month) + 1
        if month is None:
            month = datetime.datetime.today().month
        if day is None:
            day = datetime.datetime.today().day
        if year is None:
            year = 2024
        try:
            if isinstance(month, str):
                month = datetime.datetime.strptime(month, '%B').month
            date = datetime.datetime(year, month, day)
            unix_time = time.mktime(date.timetuple())
        except ValueError as e:
            await interaction.response.send_message(f"Error: {e}")
            return

        if unix_time < startDate:
            await interaction.response.send_message("Dates before April 1st 2024 fall outside the scope of AU")
            return

        days_since_start = int((unix_time - startDate) / 86400)+1  # Number of days since start date
        loreYear = (days_since_start // 4) + 50  # Each lore year has 4 days, start at 64 AU
        cur_season = days_since_start % 4  # Get the current season index

        seasons = ['Winter', 'Spring', 'Summer', 'Fall']
        
        print(f'The Date {date} becomes \nUnix: {unix_time}\nLoreyear: {loreYear} with Season: {seasons[cur_season]}')
        await interaction.response.send_message(f"cur_season = {cur_season}")
        await interaction.followup.send(f'{seasons[cur_season]} of {loreYear} AU')

async def setup(bot) -> None:
    await bot.add_cog(Moderation(bot))
