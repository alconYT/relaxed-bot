import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Type|| .Help for command help'))
    await client.send_message(member, 'Hello welcome to alcon's server read the rules plz')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')
    if message.content == '.relax bot':
        await client.send_message(message.channel,'Hi {user} this is alconYT bot how r u?')
    if message.content == '.pikalove':
        em = discord.Embed(description='PIKA LOVE TO THE TO <33')
        em.set_image(url='https://cdn.discordapp.com/emojis/649673695006031913.png?v=1')
        await client.send_message(message.channel, embed=em)
    if ('fuck ') in message.content:
       await client.delete_message(message)
    if ('shit') in message.content:
       await client.delete_message(message)
    if ('ass') in message.content:
       await client.delete_message(message)
    if ('wlf') in message.content:
       await client.delete_message(message)
    if ('wlh') in message.content:
       await client.delete_message(message)
    if message.content == '.meme':
        em = discord.Embed(description='Only a spoon full')
        em.set_image(url='https://cdn.discordapp.com/attachments/410117018432438272/812191778366554132/image0-1.png')
        await client.send_message(message.channel, embed=em)
client.run('ODEzNTYxNTc0NTg4NTQ3MDky.YDRGQg.p5DahVuWJVkaD0gNpPYqfQdzb2s')

