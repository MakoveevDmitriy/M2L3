import discord
import random
import os
import requests


from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import get_duck_image_url



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

@bot.command()
async def dogs(ctx):
    images = os.listdir('dogs')

    img_name = random.choice(images)

    with open(f'dogs/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def prostokvahino(ctx):
    images = os.listdir('prostokvahino')

    img_name = random.choice(images)

    with open(f'prostokvahino/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)




@bot.command()
async def passvord(ctx):
    
    await ctx.send(gen_pass(10))
    
@bot.command()
async def money(ctx):
    a = random.randint(1, 2)
    if a == 1:
        await ctx.send('решка')
    else:
        await ctx.send('орёл')


@bot.command()
async def ekologia(ctx):
    images = os.listdir('ekologia')

    img_name = random.choice(images)

    with open(f'ekologia/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)



@bot.command()
async def musor(ctx):
    await ctx.send("Привет!!!Ты хочешь помочь планете в плане экологии? Молодец! Ты можешь помочь утилизируя отходы, не покупая лишнее, переходя на естественную энергию, экономя воду.")

    images = os.listdir('ekologia')

    img_name = random.choice(images)

    with open(f'ekologia/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)








@bot.command()
async def command(ctx):
    await ctx.send('есть функции: hello, heh, passvord, money, command, duck, dogs, mem, prostokvahino, musor, ekologia')


bot.run("MTEwNDY3NDAyMjc5NDQ2NTM4MA.GDprFL.PuB5t7WelRm0tunlagebJIUspfgmxPusf8MPxk")