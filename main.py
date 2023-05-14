import os
from discord import *
from discord import Intents
from discord.ext import commands
from discord import Game
from discord import Status

APP_ID = '818800581391941649'
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

intents = Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=Intents.all(),
            sync_command=True,
            application_id=APP_ID
        )
        self.initial_extension = [
            'Cogs.get_timetable_day'
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()

    async def on_ready(self):
        print('login as')
        print(self.user.name)
        print(self.user.id)
        print('===============')
        game = Game('/시간표 를 쳐보라고 말')
        await self.change_presence(status=Status.online, activity=game)


bot = MyBot()
bot.run(token=DISCORD_TOKEN)
