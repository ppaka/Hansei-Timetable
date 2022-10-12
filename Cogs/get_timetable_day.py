from typing import Optional
import discord
from discord import app_commands
from discord.ext import commands
from discord import Interaction


class get_timetable_day(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='시간표', description='나이스에서 시간표 데이터를 찾아드립니다!')
    @app_commands.rename(sch_class='class')
    @app_commands.describe(sch_class='원하는 반을 선택해주세요')
    @app_commands.choices(sch_class=[
        app_commands.Choice(name='게임', value='게임과1'),
        app_commands.Choice(name='네보1', value='네트워크보안과1'),
        app_commands.Choice(name='해킹1', value='해킹보안과1'),
        app_commands.Choice(name='해킹2', value='해킹보안과2'),
    ])
    @app_commands.describe(weekday='원하는 요일의 시간표를 볼때 사용합니다')
    @app_commands.choices(weekday=[
        app_commands.Choice(name='월요일', value=1),
        app_commands.Choice(name='화요일', value=2),
        app_commands.Choice(name='수요일', value=3),
        app_commands.Choice(name='목요일', value=4),
        app_commands.Choice(name='금요일', value=5),
    ])
    @app_commands.describe(date='원하는 날짜의 시간표를 볼때 사용합니다 (입력예시: 20220505)')
    async def request_get(self, interaction: Interaction, sch_class: app_commands.Choice[str], weekday: Optional[app_commands.Choice[int]] = None, date: Optional[int] = None):
        await interaction.response.send_message('~')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        get_timetable_day(bot)
    )
