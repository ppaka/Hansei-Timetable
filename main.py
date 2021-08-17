import datetime
import json
import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice

client = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(client, sync_commands=True)


dataDictionary = {'컴그': ['컴그', '351 971 4354'], '국어': ['국어', '531 696 3430'], '영어': ['영어', '974 976 2480'], '사회': ['사회', '458 265 2826'], '국사': ['국사', '418 692 2475'], '수학': ['수학', '260 836 1619'],
                  '프로': ['프로', '274 223 4806'], '과학': ['과학', '314 911 3899'], '진로': ['진로', '341 183 8871'], '음악': ['음악', '373 769 7752'], '디자': ['디자', '351 971 4354'], '체육': ['체육', '517 857 7141'],
                  '자율': ['', ''], '정처': ['', ''], '파이썬': ['파이썬', '997 912 0043'], '컴시': ['컴시', '279 718 8506'], '소양': ['소양', '458 265 2826']}


daylist = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

zoomLink = 'https://zoom.us/j/'

studyTime = ['08:40 - 09:30', '09:40 - 10:30',
             '10:40 - 11:30', '11:30 - 12:20', '12:20 - 13:10',
             '13:20 - 14:10', '14:20 - 15:10', '15:20 - 16:10']


@client.event
async def on_ready():
    print(f'다음으로 로그인 합니다\n{client.user.name}')
    print(client.user.id)
    print('--------')
    await client.change_presence(activity=discord.Game(name='/시간표'))


@slash.slash(name="시간표",
             description="시간표를 표시합니다",
             options=[
                 create_option(
                     name="optone",
                     description="처리할 명령을 선택해주세요",
                     option_type=3,
                     required=True,
                     choices=[
                         create_choice(
                             name="게임",
                             value="게임"
                         ),
                         create_choice(
                             name="해킹1",
                             value="해킹1"
                         ),
                         create_choice(
                             name="해킹2",
                             value="해킹2"
                         ),
                         create_choice(
                             name="해킹3",
                             value="해킹3"
                         ),
                         create_choice(
                             name="수업시간",
                             value="수업시간"
                         )
                     ]
                 ),
                 create_option(
                     name="day",
                     description="다른 요일의 시간표를 볼때 사용합니다",
                     option_type=3,
                     required=False,
                     choices=[
                         create_choice(
                             name="월요일",
                             value="월요일"
                         ),
                         create_choice(
                             name="화요일",
                             value="화요일"
                         ),
                         create_choice(
                             name="수요일",
                             value="수요일"
                         ),
                         create_choice(
                             name="목요일",
                             value="목요일"
                         ),
                         create_choice(
                             name="금요일",
                             value="금요일"
                         )
                     ]
                 )
             ])
async def show(ctx, optone: str, day: str = ""):
    r = datetime.datetime.today().weekday()
    if day == "월요일":
        r = 0
    elif day == "화요일":
        r = 1
    elif day == "수요일":
        r = 2
    elif day == "목요일":
        r = 3
    elif day == "금요일":
        r = 4
    elif day == "토요일":
        r = 5
    elif day == "일요일":
        r = 6

    if optone == "게임":
        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classGame"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='게임과 1-1', description=f'{daylist[r]} 게임 1반 시간표 입니다!', color=0xFFB2D9)
                embed.add_field(
                    name=f'아침조회', value=f'{dataDictionary["과학"][1]}\n{zoomLink + (dataDictionary["과학"][1].replace(" ", ""))}')
                for i in sj:
                    embed.add_field(name=f'{dataDictionary[i][0]}', value=f'{dataDictionary[i][1]}\n{zoomLink + (dataDictionary[i][1].replace(" ", ""))}',
                                    inline=False)
            embed.set_footer(text='by paka#8285')
            await ctx.send(embed=embed)
    elif optone == "해킹1":
        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classHac1"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='해킹보안 1-1', description=f'{daylist[r]} 해킹보안 1반 시간표 입니다!', color=0xB5B2FF)
                for i in sj:
                    embed.add_field(name=f'{dataDictionary[i][0]}', value=f'{dataDictionary[i][1]}\n{zoomLink + (dataDictionary[i][1].replace(" ", ""))}',
                                    inline=False)
            embed.set_footer(text='by paka#8285')
            await ctx.send(embed=embed)
    elif optone == "해킹2":
        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classHac2"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='해킹보안 1-2', description=f'{daylist[r]} 해킹보안 2반 시간표 입니다!', color=0xCEF279)
                for i in sj:
                    embed.add_field(name=f'{dataDictionary[i][0]}', value=f'{dataDictionary[i][1]}\n{zoomLink + (dataDictionary[i][1].replace(" ", ""))}',
                                    inline=False)
            embed.set_footer(text='by paka#8285')
            await ctx.send(embed=embed)
    elif optone == "해킹3":
        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classHac3"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='해킹보안 1-3', description=f'{daylist[r]} 해킹보안 3반 시간표 입니다!', color=0xFFC19E)
                embed.add_field(
                    name=f'아침조회', value=f'{dataDictionary["국사"][1]}\n{zoomLink + (dataDictionary["국사"][1].replace(" ", ""))}')
                for i in sj:
                    embed.add_field(name=f'{dataDictionary[i][0]}', value=f'{dataDictionary[i][1]}\n{zoomLink + (dataDictionary[i][1].replace(" ", ""))}',
                                    inline=False)
            embed.set_footer(text='by paka#8285')
            await ctx.send(embed=embed)
    elif optone == "수업시간":
        embed = discord.Embed(
            title='수업시간', description='『조종례는 알잘딱』', color=0xFFA7A7)
        embed.add_field(name='1교시', value=studyTime[0], inline=False)
        embed.add_field(name='2교시', value=studyTime[1], inline=False)
        embed.add_field(name='3교시', value=studyTime[2], inline=False)
        embed.add_field(name='점심시간', value=studyTime[3], inline=False)
        embed.add_field(name='4교시', value=studyTime[4], inline=False)
        embed.add_field(name='5교시', value=studyTime[5], inline=False)
        embed.add_field(name='6교시', value=studyTime[6], inline=False)
        embed.add_field(name='7교시', value=studyTime[7], inline=False)
        embed.set_footer(text='by paka#8285')
        await ctx.send(embed=embed)


client.run('ODE4ODAwNTgxMzkxOTQxNjQ5.YEdVdw.hoIfa3xTPa-SOIh-lqFvfFrB9I0')
# client.run("NzM1MTA2NjA1NDM1MDYwMjI1.XxbbYA.qpDbsDm-8vxI5Gy7bvKGrfDg7Ac")
