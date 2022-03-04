import os
import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

bot = discord.Bot()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello guys')
    await bot.process_commands(message)

@bot.command()
async def startgame(ctx):
    embedvar = discord.Embed(title="Starting the BUSec game", description="Click on the StartGame button to "
                                                                          "start the game", color=0x00ff00)
    button = Button(label='StartGame', style=discord.ButtonStyle.green,emoji="✔")
    view = View()
    view.add_item(button)
    await ctx.send(embed = embedvar, view = view)


load_dotenv()
bot.run(os.getenv('TOKEN'))
