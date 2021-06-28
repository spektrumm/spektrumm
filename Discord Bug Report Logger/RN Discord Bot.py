# import gspread required libraries
import gspread
#import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


# import discord API functions for use with this bot
import discord
from discord.ext import commands, tasks
from itertools import cycle

# define the bot's command prefix for use in discord
bot = commands.Bot(command_prefix = '.')
status = cycle(['Bug Squashing!', 'Crafting...', 'Mining...', 'rats.', 'Those pesky bugs...',"Google API's are hard"])


#------------------------------------------------------------------------------------

# DISCORD.PY GENERAL SETUP
# define an event for the bot to print to the console when the bot is 'ready'
@bot.event
async def on_ready():
    change_status.start()
    await bot.change_presence(status = discord.Status.do_not_disturb,activity = discord.Game('Hello there!'))
    print("Bot is ready!")

# create a looping task to update the bot's status on discord
@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

#------------------------------------------------------------------------------------

# GSPREAD SHEET DATA GENERAL
# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('placeholder', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)


# get the instance of the Spreadsheet
sheet = client.open('Rasa Novum Bug Report (Responses)')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# Define the extracted values as a list
lstSheetData = sheet_instance.get_all_records()

rawRowCount = len(sheet_instance.get_all_values())


#------------------------------------------------------------------------------------
# DISCORD.PY BOT FUNCTIONS BEGIN

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency *1000)}ms')
    print(f'pong! {round(bot.latency *1000)}ms') # Display the latency console side, to ensure the command is funcitoning properly.

### --- WIP --- ###

#serverID = 'placeholder'

#@tasks.loop(seconds=15)
#async def sheet_check(ctx):
    #channel = discord.utils.get(bot.get_all_channels(), guild__name='Eye of the Spider', name='bot-test')
    #server = discord.Guild(str())
    #channel = discord.TextChannel(, guild="Eye Of The Spider")
    #await bug_report_new(channel)
        

@bot.command()
async def check(ctx):

    updatedRowCount = len(sheet_instance.get_all_values())

    timestampChk = sheet_instance.cell(col=1,row=updatedRowCount)
    categoryChk = sheet_instance.cell(col=2,row=updatedRowCount)
    usernameChk = sheet_instance.cell(col=3,row=updatedRowCount)
    
    convertTime = str(timestampChk)
    convertCat = str(categoryChk)
    convertUser = str(usernameChk)

    
    
    if updatedRowCount > rawRowCount:
        await ctx.send(f'New bug report! **Timestamp:** {convertTime[13:-2]}, **Category:** {convertCat[12:-2]}, **Submitted by:** {convertUser[12:-2]} **Link:** https://docs.google.com/forms/d/1tU7OR2U0LOkB6cuC-JppTNyxjcLBsewWpBp2Meg8LwE/edit#responses')
        print('New bug report!')
    else:
        await ctx.send('No new bug reports.')
        print('No new bug reports.')
    

    #await ctx.send(f'New bug report! **Timestamp:** {convertTime[13:-2]}, **Category:** {convertCat[12:-2]}, **Submitted by:** @{convertUser[12:-2]}')
    
    #updatedRowCount = rawRowCount + 1


bot.run('placeholder')