import discord
from discord.ext import commands

import os
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def mem(ctx):
    images = os.listdir('memas')

    img_name = random.choice(images)

    with open(f'memas/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    



bot.run("MTEwNDY3NDAyMjc5NDQ2NTM4MA.GDprFL.PuB5t7WelRm0tunlagebJIUspfgmxPusf8MPxk")