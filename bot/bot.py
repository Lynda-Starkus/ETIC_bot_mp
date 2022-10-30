import discord
import os
import search_runpee # search class we will impelement later
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

df = read_csv("../Scraper/startupnation_articles.csv")
'''
# If you are coding the bot on a local machine, use the python-dotenv pakcage to get variables stored in .env file of your project
from dotenv import load_dotenv
load_dotenv()
'''

# instantiate discord client 
client = discord.Client()

# discord event to check when the bot is online 
@client.event
async def on_ready():
  print(f'{client.user} is now online!')

@client.event
async def on_message(message): 
  # make sure bot doesn't respond to it's own messages to avoid infinite loop
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  
  
  if message.content.startswith(f'$hello'):
    await message.channel.send('''Hello there! I\'m the fidgeting bot from RunPee. 
    Sorry but I really need to go to the bathroom... Please read my manual by typing $help or $commands while I'm away.''')

  if f'$search' in message_content:
        await message.channel.send(df['url'][0])


# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))