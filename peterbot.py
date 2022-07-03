import discord
from discord.ext import commands
import time
# import keep_alive

bot = commands.Bot(command_prefix='p.')
@bot.event
async def on_ready():
    print(' P_Bot is online')

# @bot.event
# async def on_member_join(member):
#     print(f'{member} hello !')
#
# @bot.event
# async def on_member_remove(member):
#     print(f'{member} bye !')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'hint':
        await message.channel.send('男生 虛構 電影角色 人形')
    while message.content == 'level up':
        await message.channel.send('up')
        time.sleep(2)
        if message.content == 'stop':
            return False
    if message.content == '耶':
        await message.channel.send('?')
@bot.event
async def on_message(message):
    channel = bot.get_channel(991388317977424013)
    if message.channel == channel:
        if message.content == '耶':
            await channel.send('?')

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)



if __name__ == "__main__":
    TOKEN = 'OTkzMTMzMjYwMTA2MzcxMDcy.GdVbuL.s4oIyjJDNBjvbKWvf0fBPmkNodFw_wQ73Ln4EY'

    bot.run(TOKEN)
    test = 0