import discord

class DiscordAgent:
    def __init__(self):
        self.webhook = None
        self.user = None

    async def setup(self, channel:discord.TextChannel, name:str='Agente ZYX'):
        channel_webhooks = await channel.webhooks()
        for webhook in channel_webhooks:
            if(webhook.channel_id == channel.id):
                self.webhook = webhook
        if not self.webhook:
            self.webhook = await channel.create_webhook(name=name)
        return self

    def set_user(self, user:discord.User):
        self.user = user

    async def send_as_user(self, content:str|None=None, embeds:list[discord.Embed]|None=None, user:discord.User|None=None):
        if not user:
            user = self.user
        try:
            return await self.webhook.send(
                content = content,
                embeds = embeds,
                username = user.name,
                avatar_url = user.avatar_url,
            )
        except Exception as e:
            print(f'Error al enviar como usuario por medio de Agente: {e}')
            return None