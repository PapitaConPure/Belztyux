import discord
from discord.ext import commands

'''Almacenar puerta io de Discord'''
client = commands.Bot(command_prefix = 'zx.')

'''Inicio de weá del bot'''
@client.event
async def on_ready():
    print('Bot conectado y funcionando como "{0.user}"'.format(client))

'''Comandos'''
''''''

'''Ping'''
@client.command(aliases=['ping','bot.ping','b.ping'])
async def COMMAND_PING(message):
    numeros = ''
    async for m_id in message.channel.history().filter(lambda m: m.content.startswith('Prueba')).map(lambda m: m.id):
        numeros += '{0}\n'.format(m_id)

    await message.channel.send(f'Wena po como estai [{round(client.latency * 1000)}ms]')


'''Información del servidor'''
@client.command(aliases=['serverinfo','sv.info','s.info'])
async def COMMAND_SERVERINFO(message):
    numeros = ''
    async for m_id in message.channel.history().filter(lambda m: m.content.startswith('Prueba')).map(lambda m: m.id):
        numeros += '{0}\n'.format(m_id)

    embed = discord.Embed(
        title = 'Información del servidor',
        description = 'Prueba',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='Prueba de pie de embed')
    embed.set_image(url = message.author.avatar_url)
    embed.set_thumbnail(url='https://img2.gelbooru.com/images/99/c2/99c29fb2d86d53394d223bbdec6f9c44.jpg')
    embed.set_author(name = message.author.name, icon_url = message.author.avatar_url)
    embed.add_field(name = 'Numeritos uwu', value = numeros, inline = False)
    embed.add_field(name = 'Wenas', value = 'Wena po como estai', inline = True)
    embed.add_field(name = 'Tobien', value = '¿Todo bien po\'?', inline = True)

    await message.channel.send(embed=embed)

@client.command(errors='CommandNotFound')
async def COMMAND_NOTFOUND(message):
    await message.channel.send(':warning: este comando no existe.')

'''Presencia del bot'''
client.run('NzA2OTY5MDcwOTY0MzEwMTA4.XrB_Mw.-vcA42Y9OMCiuWRSwe9Ukd-09Ic')