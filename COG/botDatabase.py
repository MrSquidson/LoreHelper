import os
import discord
from discord.ext import commands
import csv
from csv import DictWriter


class Database(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    async def filepathExists(filepath):
        print(f'filepathExists recieved {filepath}')
        if os.path.exists(filepath) != True:
            os.makedirs(filepath)

    async def loreEvent(guildID:int, date:int, loreevent:str):

        field_names = ['date', 'loreevent']
        current_dir = os.getcwd()
        filepath = os.path.expanduser(os.path.join(current_dir, 'DB', str(guildID)))
        await Database.filepathExists(filepath=filepath)


        if os.path.exists(filepath + '/punishments.csv') != True: # If './DB/GuildID/punishments.csv' doesn't exist 
            Database.filepathExists(filepath=filepath)
            open(filepath+'\punishments.csv','x')
            with open((os.path.join(filepath, 'punishments.csv')),'w', newline='') as csvfile: # Make a new csv fil
                writer = csv.DictWriter(csvfile, fieldnames=field_names) # With field_names in the header (also creates header)
                writer.writeheader()
                writer.writerow({f'date': date}) # Write case 1/loreevent 1
                print(f'Made new .csv file for Guild {discord.Guild.name(guildID)} 
                      \nWith GuildID: {guildID}')
                return 'New Guild'

        else: # ... 'punishments.csv' exists!
            with open(filepath + '/punishments.csv','a', newline='') as f_object: # open file in append mode!
                dictwriter_object = DictWriter(f_object, fieldnames=field_names) # with the same fieldnames as before
                dictwriter_object.writerow({date}) # Write the new event to file
                print('Appended most recent case')
                return 'Success'

async def setup(bot) -> None:
     await bot.add_cog(Database(bot))