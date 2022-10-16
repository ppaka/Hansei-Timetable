from typing import Optional
from discord import app_commands
import discord
from discord.ext import commands
from discord import Interaction
import datetime
import pytz
import re
import dotenv
import os
from urllib import parse
import requests
import random

dotenv.load_dotenv()
neis_key = os.getenv('NEIS_KEY')
daylist = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

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
        app_commands.Choice(name='월요일', value=0),
        app_commands.Choice(name='화요일', value=1),
        app_commands.Choice(name='수요일', value=2),
        app_commands.Choice(name='목요일', value=3),
        app_commands.Choice(name='금요일', value=4),
    ])
    @app_commands.describe(date='원하는 날짜의 시간표를 볼때 사용합니다 (입력예시: 20220505)')
    async def request_get(self, interaction: Interaction, sch_class: app_commands.Choice[str], weekday: Optional[app_commands.Choice[int]] = None, date: Optional[int] = None):        
        cur_date = datetime.datetime.now(pytz.timezone('Asia/Seoul'))

        ymd = cur_date.strftime('%Y%m%d')
        if weekday != None:
            if cur_date.weekday() == 6:
                cur_date += datetime.timedelta(weeks=1)
            cur_date -= datetime.timedelta(days=cur_date.weekday() - weekday.value)
            ymd = cur_date.strftime('%Y%m%d')
        if date != None:
            cur_date = datetime.datetime.strptime(str(date), '%Y%m%d')
            ymd = cur_date.strftime('%Y%m%d')
        
        dddep = re.sub(r'[0-9]+', '', sch_class.value)
        class_num = sch_class.value.replace(dddep, '')

        APTP_OFCDC_SC_CODE = 'B10';
        SD_SCHUL_CODE = '7010911';
        ALL_TI_YMD = ymd
        DDDEP_NM = dddep
        GRADE = 2
        CLASS_NM = class_num
        req_url = f'https://open.neis.go.kr/hub/hisTimetable?KEY={neis_key}&Type=json&ATPT_OFCDC_SC_CODE={APTP_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&ALL_TI_YMD={ALL_TI_YMD}&DDDEP_NM={parse.quote(DDDEP_NM)}&GRADE={GRADE}&CLASS_NM={CLASS_NM}'

        await interaction.response.defer(ephemeral=False)

        try:
            req = requests.get(req_url)

        except requests.exceptions.Timeout as errd:
            print("Timeout Error : ", errd)
            await interaction.response.edit_message(content='에러 발생! [Timeout Error]')
            return
            
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting : ", errc)
            await interaction.response.edit_message(content='에러 발생! [Connection Error]')
            return
            
        except requests.exceptions.HTTPError as errb:
            print("Http Error : ", errb)
            await interaction.response.edit_message(content='에러 발생! [Http Error]')
            return

        # Any Error except upper exception
        except requests.exceptions.RequestException as erra:
            print("AnyException : ", erra)
            await interaction.response.edit_message(content='으... 에러가...')
            return

        json_data = dict(req.json())
        if 'hisTimetable' not in json_data.keys():
            if json_data['RESULT']['CODE'] == 'INFO-200':
                error_embed = discord.Embed(title='오류 발생!', color=0xFF0000, description='나이스에서 데이터를 불러올 수 없습니다').add_field(name='에러코드', value='INFO-200').set_footer(text=f'YMD:{ymd} / paka#8285')
                await interaction.edit_original_response(embed=error_embed)
            return
        
        if json_data['hisTimetable'][0]['head'][1]['RESULT']['CODE'] != 'INFO-000':
            error_embed = discord.Embed(title='오류 발생!', color=0xFF0000, description='나이스에서 데이터를 불러올 수 없습니다').add_field(name='에러코드', value=f"{json_data['hisTimetable'][0]['head'][1]['RESULT']['CODE']}").set_footer(text=f'YMD:{ymd} / paka#8285')
            await interaction.edit_original_response(embed=error_embed)
            return

        if 'row' not in dict(json_data['hisTimetable'][1]).keys():
            error_embed = discord.Embed(title='오류 발생!', color=0xFF0000, description='시간표 데이터를 불러올 수 없습니다').set_footer(text=f'YMD:{ymd} / paka#8285')
            await interaction.edit_original_response(embed=error_embed)
            return
        
        letters = '0123456789ABCDEF'
        color = '0x'
        for i in range(0, 6):
            color += letters[random.randrange(0, 16)]
        embed = discord.Embed(title=f'{DDDEP_NM} {GRADE}-{CLASS_NM}', color=int(color, 0), description=f'{daylist[cur_date.weekday()]} {DDDEP_NM} {CLASS_NM}반 시간표를 보여드릴게요!').set_footer(text=f'YMD:{ymd} / paka#8285')
        for e in json_data['hisTimetable'][1]['row']:
            embed.add_field(name=f"{e['PERIO']}교시", value=f"{e['ITRT_CNTNT']}", inline=False)
        await interaction.edit_original_response(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        get_timetable_day(bot)
    )
