import discord
from keep_alive import keep_alive
from discord.ext import commands
import random

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 363536676582326282  # Change to your discord id!!!

member = ['현준', '은비', '수빈', '민욱', '광배', '수현']
lst = []
temp_lst = []


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title="조교님의 능력", color=0xa29cf2)
    embed.add_field(name="!안녕", value="조교님에게 인사를 해보아요", inline=False)
    embed.add_field(name="!룰렛", value="조교님께서 코드리뷰 순서를 정해줍니다", inline=False)
    embed.add_field(name="!문제", value="추가한 문제들과 링크를 보여줍니다", inline=False)
    embed.add_field(name="!문제추가 {문제번호}",
                    value="해당 문제를 추가하고 문제링크와 백준 문제집 링크를 보여줍니다",
                    inline=False)
    embed.add_field(name="!문제삭제 {문제번호}", value="해당 문제를 삭제합니다", inline=False)
    embed.add_field(name="!문제초기화", value="문제 목록을 초기화합니다", inline=False)
    embed.add_field(name="!문제복원",
                    value="실수로 초기화를 하셨나요? 걱정 마세요, 우리의 조교님은 언제나 준비되어 있답니다",
                    inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 안녕(ctx):
    embed = discord.Embed(title="안녕하세요😄", color=0xa29cf2)
    await ctx.send(embed=embed)


@bot.command()
async def 룰렛(ctx):
    random.shuffle(member)
    embed = discord.Embed(title="오늘 코드리뷰의 발표 순서입니다", color=0xa29cf2)
    embed.add_field(name="1.\t" + member[0], value="", inline=False)
    embed.add_field(name="2.\t" + member[1], value="", inline=False)
    embed.add_field(name="3.\t" + member[2], value="", inline=False)
    embed.add_field(name="4.\t" + member[3], value="", inline=False)
    embed.add_field(name="5.\t" + member[4], value="", inline=False)
    embed.add_field(name="6.\t" + member[5], value="", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 문제(ctx):
    if len(lst) == 0:
        embed = discord.Embed(title="추가된 문제가 없습니다", color=0xe64500)
        await ctx.send(embed=embed)
    if len(lst) == 1:
        embed = discord.Embed(title="문제 리스트", color=0xa29cf2)
        embed.add_field(name=lst[0],
                        value="https://www.acmicpc.net/problem/" + str(lst[0]),
                        inline=False)
        await ctx.send(embed=embed)
    if len(lst) == 2:
        embed = discord.Embed(title="문제 리스트", color=0xa29cf2)
        embed.add_field(name=lst[0],
                        value="https://www.acmicpc.net/problem/" + str(lst[0]),
                        inline=False)
        embed.add_field(name=lst[1],
                        value="https://www.acmicpc.net/problem/" + str(lst[1]),
                        inline=False)
        await ctx.send(embed=embed)
    if len(lst) == 3:
        embed = discord.Embed(title="문제 리스트", color=0xa29cf2)
        embed.add_field(name=lst[0],
                        value="https://www.acmicpc.net/problem/" + str(lst[0]),
                        inline=False)
        embed.add_field(name=lst[1],
                        value="https://www.acmicpc.net/problem/" + str(lst[1]),
                        inline=False)
        embed.add_field(name=lst[2],
                        value="https://www.acmicpc.net/problem/" + str(lst[2]),
                        inline=False)
        await ctx.send(embed=embed)
    if len(lst) == 4:
        embed = discord.Embed(title="문제 리스트", color=0xa29cf2)
        embed.add_field(name=lst[0],
                        value="https://www.acmicpc.net/problem/" + str(lst[0]),
                        inline=False)
        embed.add_field(name=lst[1],
                        value="https://www.acmicpc.net/problem/" + str(lst[1]),
                        inline=False)
        embed.add_field(name=lst[2],
                        value="https://www.acmicpc.net/problem/" + str(lst[2]),
                        inline=False)
        embed.add_field(name=lst[3],
                        value="https://www.acmicpc.net/problem/" + str(lst[3]),
                        inline=False)
        await ctx.send(embed=embed)
    if len(lst) == 5:
        embed = discord.Embed(title="문제 리스트", color=0xa29cf2)
        embed.add_field(name=lst[0],
                        value="https://www.acmicpc.net/problem/" + str(lst[0]),
                        inline=False)
        embed.add_field(name=lst[1],
                        value="https://www.acmicpc.net/problem/" + str(lst[1]),
                        inline=False)
        embed.add_field(name=lst[2],
                        value="https://www.acmicpc.net/problem/" + str(lst[2]),
                        inline=False)
        embed.add_field(name=lst[3],
                        value="https://www.acmicpc.net/problem/" + str(lst[3]),
                        inline=False)
        embed.add_field(name=lst[4],
                        value="https://www.acmicpc.net/problem/" + str(lst[4]),
                        inline=False)
        await ctx.send(embed=embed)
    if len(lst) == 6:
        embed = discord.Embed(title="문제 리스트", color=0xa29cf2)
        embed.add_field(name=lst[0],
                        value="https://www.acmicpc.net/problem/" + str(lst[0]),
                        inline=False)
        embed.add_field(name=lst[1],
                        value="https://www.acmicpc.net/problem/" + str(lst[1]),
                        inline=False)
        embed.add_field(name=lst[2],
                        value="https://www.acmicpc.net/problem/" + str(lst[2]),
                        inline=False)
        embed.add_field(name=lst[3],
                        value="https://www.acmicpc.net/problem/" + str(lst[3]),
                        inline=False)
        embed.add_field(name=lst[4],
                        value="https://www.acmicpc.net/problem/" + str(lst[4]),
                        inline=False)
        embed.add_field(name=lst[5],
                        value="https://www.acmicpc.net/problem/" + str(lst[5]),
                        inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def 문제추가(ctx, num):
    if num in lst:
        embed = discord.Embed(title=num + '번은 이미 있습니다', color=0xe64500)
        await ctx.send(embed=embed)
    else:
        lst.append(num)
        embed = discord.Embed(title="문제 풀러 가기",
                              url="https://www.acmicpc.net/problem/" +
                              str(num),
                              color=0xa29cf2)
        embed.set_author(name=str(num) + "번 문제 추가")
        await ctx.send(embed=embed)


@bot.command()
async def 문제삭제(ctx, num):
    if num in lst:
        lst.remove(num)
        embed = discord.Embed(title=num + "번 삭제 완료", color=0x0fa10c)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=num + '번은 리스트에 없습니다', color=0xe64500)
        await ctx.send(embed=embed)


@bot.command()
async def 문제초기화(ctx):
    global lst
    global temp_lst
    temp_lst = lst
    lst = []
    embed = discord.Embed(title="문제 초기화 완료", color=0x0fa10c)
    await ctx.send(embed=embed)


@bot.command()
async def 문제복원(ctx):
    global lst
    global temp_lst
    lst = temp_lst
    temp_lst = []
    embed = discord.Embed(title="문제 복원 완료", color=0x0fa10c)
    await ctx.send(embed=embed)


extensions = [
    'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = 'MTA3NDM2MDc3NDk1NDM0MDM4Mg.GFu0KL.7hgH7K2oZH14ZaxQUfHse-cwSNFFxRfC-qbfdQ'
bot.run(token)  # Starts the bot
