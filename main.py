import discord
import time
client = discord.Client()

async def on_ready():
    print('目前登入身份：', client.user)

async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # #如果包含 ping，機器人回傳 pong
    # if message.content == 'ping':
    #     await message.channel.send('pong')

async def level_up(message):
    if message.author == client.user:
        return
    while message.content == 'level up':
        await message.channel.send('up')
        time.sleep(2)
        if message.content == 'stop':
            return False




TOKEN = 'OTkyNzYyODgyNzYyNzQzODM5.GoKIQZ.V-92rIOvrCF_8ZpsB_06HhT6unz4lsKQFTbmyE'
client.run(TOKEN)