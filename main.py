import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hola'):
        await message.channel.send('Wena po')

'''Presencia del bot'''
client.run('NzA2OTY5MDcwOTY0MzEwMTA4.XrB_Mw.-vcA42Y9OMCiuWRSwe9Ukd-09Ic')