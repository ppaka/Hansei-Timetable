import datetime
import json

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!시간표 ')
daylist = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
subjectlist = ['컴그', '국어', '영어', '사회', '국사',    # 0컴그 1국어 2영어 3사회 4국사
                '수학', '프로', '과학', '진로', '음악',   # 5수학 6프로 7과학 8진로 9음악
                '디자', '체육', '자율', '정처', '파이썬'] # 10디자 11체육 12자율 13정처 14파이썬
sjzoomid = ['3519714354', '5316963430', '9749762480', '4582652826', '4186922475',
             '2608361619', '2742234806', '3149113899', '3411838871', '3737697752',
             '3519714354', '5178577141', '줌 아이디가 없습니다', '2797188506', '7271742487']
sjzoomlink = 'https://zoom.us/j/'
studyTime = ['08:40 - 09:30', '09:40 - 10:30',
 '10:40 - 11:30', '11:30 - 12:20', '12:20 - 13:10', 
 '13:20 - 14:10', '14:20 - 15:10', '15:20 - 16:10']


@client.event
async def on_ready():
    print(f'다음으로 로그인 합니다\n{client.user.name}')
    print(client.user.id)
    print('--------')
    await client.change_presence(activity=discord.Game(name='!시간표 도움말'))


@client.command(name='게임', pass_context=True)
async def showGame(ctx, day):
    r = ""
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

    with open('data.json') as jsonFile:
        data = json.load(jsonFile)
        sj = data["classGame"][r]["subjects"]
        if sj == "":
            embed = discord.Embed(
                title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
        else:
            embed = discord.Embed(
                title='게임과 1-1', description=f'{daylist[r]} 게임 1반 시간표 입니다!', color=0xffff00)
            embed.add_field(name=f'아침조회: {subjectlist[7]}', value=f'{sjzoomid[7]}\n{sjzoomlink+sjzoomid[7]}')
            for i in sj:
                embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
    await ctx.send(embed=embed)


@client.command(name='해킹1', pass_context=True)
async def showHac1(ctx, day):
    r = ""
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

    with open('data.json') as jsonFile:
        data = json.load(jsonFile)
        sj = data["classHac1"][r]["subjects"]
        if sj == "":
            embed = discord.Embed(
                title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
        else:
            embed = discord.Embed(
                title='해킹보안 1-1', description=f'{daylist[r]} 해킹보안 1반 시간표 입니다!', color=0xffff00)
            for i in sj:
                embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
    await ctx.send(embed=embed)


@client.command(name='해킹2', pass_context=True)
async def showHac2(ctx, day):
    r = ""
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

    with open('data.json') as jsonFile:
        data = json.load(jsonFile)
        sj = data["classHac2"][r]["subjects"]
        if sj == "":
            embed = discord.Embed(
                title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
        else:
            embed = discord.Embed(
                title='해킹보안 1-2', description=f'{daylist[r]} 해킹보안 2반 시간표 입니다!', color=0xffff00)
            for i in sj:
                if i == 14:
                    embed.add_field(name=f'{subjectlist[i]}',value=f'9979120043\n{sjzoomlink}9979120043', inline=False)
                else: embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
    await ctx.send(embed=embed)


@client.command(name='해킹3', pass_context=True)
async def showHac3(ctx, day):
    r = ""
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

    with open('data.json') as jsonFile:
        data = json.load(jsonFile)
        sj = data["classHac3"][r]["subjects"]
        if sj == "":
            embed = discord.Embed(
                title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
        else:
            embed = discord.Embed(
                title='해킹보안 1-3', description=f'{daylist[r]} 해킹보안 3반 시간표 입니다!', color=0xffff00)
            embed.add_field(name=f'아침조회: {subjectlist[4]}', value=f'{sjzoomid[4]}\n{sjzoomlink+sjzoomid[4]}')
            for i in sj:
                if i == 14:
                    embed.add_field(name=f'{subjectlist[i]}',value=f'9979120043\n{sjzoomlink}9979120043', inline=False)
                else: embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
    await ctx.send(embed=embed)


@showGame.error
async def showGame_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = datetime.datetime.today().weekday()

        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classGame"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='게임과 1-1', description=f'{daylist[r]} 게임 1반 시간표 입니다!', color=0xffff00)
                embed.add_field(name=f'아침조회: {subjectlist[7]}', value=f'{sjzoomid[7]}\n{sjzoomlink+sjzoomid[7]}')
                for i in sj:
                    embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
        await ctx.send(embed=embed)


@showHac1.error
async def showHac1_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = datetime.datetime.today().weekday()

        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classHac1"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='해킹보안 1-1', description=f'{daylist[r]} 해킹보안 1반 시간표 입니다!', color=0xffff00)
                for i in sj:
                    embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
        await ctx.send(embed=embed)


@showHac2.error
async def showHac2_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = datetime.datetime.today().weekday()

        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classHac2"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='해킹보안 1-2', description=f'{daylist[r]} 해킹보안 2반 시간표 입니다!', color=0xffff00)
                for i in sj:
                    if i == 14:
                        embed.add_field(name=f'{subjectlist[i]}',value=f'9979120043\n{sjzoomlink}9979120043', inline=False)
                    else: embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
        await ctx.send(embed=embed)


@showHac3.error
async def showHac3_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = datetime.datetime.today().weekday()

        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
            sj = data["classHac3"][r]["subjects"]
            if sj == "":
                embed = discord.Embed(
                    title='오류', description='시간표 데이터가 존재하지 않습니다', color=0xff0000)
            else:
                embed = discord.Embed(
                    title='해킹보안 1-3', description=f'{daylist[r]} 해킹보안 3반 시간표 입니다!', color=0xffff00)
                embed.add_field(name=f'아침조회: {subjectlist[4]}', value=f'{sjzoomid[4]}\n{sjzoomlink+sjzoomid[4]}')
                for i in sj:
                    if i == 14:
                        embed.add_field(name=f'{subjectlist[i]}',value=f'9979120043\n{sjzoomlink}9979120043', inline=False)
                    else: embed.add_field(name=f'{subjectlist[i]}',value=f'{sjzoomid[i]}\n{sjzoomlink+sjzoomid[i]}', inline=False)
        await ctx.send(embed=embed)


@client.command(name='수업시간')
async def stuTime(ctx):
    embed = discord.Embed(title='수업시간', description='조종례 까먹으면 안돼!!', color=0x86e57f)
    embed.add_field(name='1교시', value=studyTime[0], inline=False)
    embed.add_field(name='2교시', value=studyTime[1], inline=False)
    embed.add_field(name='3교시', value=studyTime[2], inline=False)
    embed.add_field(name='점심시간', value=studyTime[3], inline=False)
    embed.add_field(name='4교시', value=studyTime[4], inline=False)
    embed.add_field(name='5교시', value=studyTime[5], inline=False)
    embed.add_field(name='6교시', value=studyTime[6], inline=False)
    embed.add_field(name='7교시', value=studyTime[7], inline=False)
    await ctx.send(embed=embed)


@client.command(name='도움말', pass_context=True)
async def help(ctx):
    embedhelp = discord.Embed(
        title='도움말', description='명령어 모음', color=0xffb2f5)
    embedhelp.add_field(
        name='!시간표 게임', value='게임 1반 시간표', inline=False)
    embedhelp.add_field(
        name='!시간표 해킹1', value='해킹보안 1반 시간표', inline=False)
    embedhelp.add_field(
        name='!시간표 해킹2', value='해킹보안 2반 시간표', inline=False)
    embedhelp.add_field(
        name='!시간표 해킹3', value='해킹보안 3반 시간표', inline=False)
    embedhelp.add_field(
        name='!시간표 수업시간', value='수업시간을 보여주는 명령어야!', inline=False)
    embedhelp.add_field(
        name='요일 시간표 보는법', value='!시간표 (반) (월요일)와 같이 치면 해당 요일의 시간표가 나와!', inline=False)
    await ctx.send(embed=embedhelp)


client.run('ODE4ODAwNTgxMzkxOTQxNjQ5.YEdVdw.hoIfa3xTPa-SOIh-lqFvfFrB9I0')
