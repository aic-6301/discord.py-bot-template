import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('DISCORD_BOT_TOKEN')
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f"Logging as {bot.user}")

  
@bot.command()
async def neko(ctx):
  await ctx.send("にゃーん")

  
bot.run(token)
