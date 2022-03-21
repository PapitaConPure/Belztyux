from dotenv import load_dotenv
load_dotenv()
import discord
from discord.ext import commands
import pixiv
import os
import re

#Puerta IO de Discord
discord_client = commands.Bot(command_prefix = 'zx ')

#Inicio de weá del bot
@discord_client.event
async def on_ready():
    '''Ejecutado al iniciar sesión con el cliente'''
    print('Bot conectado y funcionando como "{0.user}"'.format(discord_client))

#Recibir mensajes
pixiv_re = re.compile('((http:\/\/|https:\/\/)(www\.)?)(pixiv.net(\/en)?)\/artworks\/([0-9]{6,9})')

@discord_client.event
async def on_message(message):
    '''Ejecutado al recibir un mensaje'''
    if message.author == discord_client.user: return
    if not message.content: return

    if pixiv_re.search(message.content):
        pixiv_pages =  pixiv_re.finditer(message.content)
        for page in pixiv_pages:
            page_id = int(page.groups()[-1])
            illust =  pixiv.get_illust(page_id)
            image_name = f'pixiv_temp_{page_id}'
            image = pixiv.upload_image_to_imgur(illust.image_urls['large'], image_name)
            
            embed = discord.Embed(
                title = illust.title,
                colour = discord.Colour.from_rgb(0, 151, 250),
            )

            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.set_image(url=image['link'])
            embed.add_field(
                name=f'💬 {illust.total_comments} ❤ {illust.total_bookmarks} 👁 {illust.total_view}',
                value=f'[Haz click aquí]({page.group(0)})',
            )

            new_content = pixiv_re.sub('', message.content)

            await message.channel.send(
                content = new_content if new_content else None,
                embed = embed,
            )
        await message.delete()

#Comandos
#Ping
@discord_client.command(aliases = ['ping','bot.ping','b.ping','bot.p','b.p'])
async def COMMAND_PING(ctx):
    numeros = ''
    async for m_id in ctx.history().filter(lambda m: m.content.startswith('Prueba')).map(lambda m: m.id):
        numeros += '{0}\n'.format(m_id)

    await ctx.send(f'Wena po como estai `[{round(discord_client.latency * 1000)}ms]`')

#Enlace de invitación
@discord_client.command(name = 'invitar', aliases = ['invite','bot.invitar','b.invitar','bot.i','b.i'])
async def COMMAND_INVITE(ctx):
    embed = discord.Embed(
        title = 'Invita a Belztyux a un servidor',
        description = 'Añade a Belztyux a tu servidor por medio de alguno de los siguientes enlaces de invitación.',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text='Prueba de pie de embed')
    '''embed.set_thumbnail(url='https://img2.gelbooru.com/images/99/c2/99c29fb2d86d53394d223bbdec6f9c44.jpg')'''
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(
        name = 'Invitar con permisos solicitados',
        value = 'Para invitarme a otro server, sigue el [proceso de autorización](https://discord.com/oauth2/authorize?client_id=706969070964310108&scope=bot&permissions=433255147584)',
        inline = False
    )

    await ctx.send(embed = embed)

#Información del servidor
@discord_client.command(aliases = ['serverinfo','sv.info','s.info','sv.i','s.i'])
async def COMMAND_SERVERINFO(ctx):
    numeros = ''
    async for m_id in ctx.history().filter(lambda m: m.content.startswith('Prueba')).map(lambda m: m.id):
        numeros += '{0}\n'.format(m_id)

    embed = discord.Embed(
        title = 'Información del servidor',
        description = 'Prueba',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='Prueba de pie de embed')
    embed.set_image(url = ctx.guild.icon_url)
    embed.set_thumbnail(url='https://img2.gelbooru.com/images/99/c2/99c29fb2d86d53394d223bbdec6f9c44.jpg')
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name = 'Numeritos uwu', value = numeros, inline = False)

    await ctx.send(embed = embed)

'''
@discord_client.on_command_error()
async def COMMAND_ERROR(ctx, error):
    switcher = {
        'CommandError': 'ha ocurrido un error al ejecutar un comando.',
        'MissingRequiredArgument': 'falta un argumento.',
        'BadArgument': 'argumentos inválidos.',
        'UserInputError': 'argumentos inválidos.',
        'CommandOnCooldown': 'comando en enfriamiento.',
        'CommandNotFound': 'este comando no existe. Prueba enviando `zx.ayuda`.'
    }
    ctx.send(f':warning: {switcher.get(error, "ha ocurrido un error inesperado.")}')
'''

#Presencia del bot
discord_client.run(os.getenv('DISCORD_TOKEN'))