import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
from random import randrange

import pandas as pd


csv = pd.read_csv('./startupnation_articles.csv')

df = pd.DataFrame(csv, columns=['title','url','tag'])
#print(df['title'][0])


load_dotenv()
  
#client = discord.Client(intents=discord.Intents.all())
token = os.getenv('TOKEN')

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$')

@bot.event
async def on_ready():
	print("Logged in as a bot")


@bot.command()
async def startup(ctx, *args):
	arguments = ', '.join(args)
	embed = discord.Embed(title="startup nation", url=str(df['url'][0]), description='test article')
	embed.set_image(url="https://c0.wallpaperflare.com/preview/299/790/569/business-laptop-office-computer.jpg")
	#embed.description = (url=df['url'][0])
	await ctx.send(df['title'][0], embed=embed)
	'''
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)


	print('message = ',user_message, '')
	if message.author == client.user:
		return

		if user_message.strip() == "eticoncept" :
      #await message.channel.send(f'Hello {username}')
			await channel.send(df['title'][0])
			return
		elif user_message.strip() == "bye":
			await channel.send(f'Bye {username}')
		elif user_message.lower() == "tell me a joke":
			jokes = [" Can someone please shed more\
			light on how my lamp got stolen?",
					"Why is she called llene? She\
					stands on equal legs.",
					"What do you call a gazelle in a \
					lions territory? Denzel."]
			await message.channel.send(random.choice(jokes))

'''
	
bot.run(token)