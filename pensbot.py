#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import configparser

import discord
import asyncio

from discord.ext import commands


config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.discord/credentials.ini'))

'''client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!f '):
        await client.send_message(message.channel, 'Fuck {}!'.format(message.content.replace('!f ', '')))
        await client.send_message(message.author, 'Did I make you happy, oWo?')
        await client.delete_message(message)
    elif message.content.startswith('!emoji'):
        print('\U0001F32D')
        await client.add_reaction(message, '\U0001F32D')
    elif 'kessel' in message.content.lower():
        await client.add_reaction(message, '\U0001F32D')

client.run(config['DEFAULT']['token'])
'''

bot = commands.Bot(command_prefix='!', description='Yaas')

@bot.event
async def on_ready():
    print('Fuck yeah!')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left: int, right: int):
    await bot.say(left + right)

@bot.command()
async def fuck(target: str):
    await bot.say('Fuck {}!'.format(target))

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run(config['DEFAULT']['token'])
