import download
import json
from collections import defaultdict
import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = ''
CHANNEK_ID = ''
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!count"):
        download.download()
        json_open = open('COVID-19_data.json', 'r', encoding="utf-8_sig")
        json_load = json.load(json_open)
        jsn = json_load

        properties = defaultdict(int)
        for f in jsn['features']:
            property = f['properties']['居住都道府県']
            if property == '中華人民共和国' or property == '調査中' or property == '不明' or property == 'スペイン' or property == 'アイルランド':
                continue
            if property not in properties:
                properties[property] = 0
            properties[property] += 1

        say = ''
        for p in properties:
            say += p + ' ' + str(properties[p]) + '\n'
        await message.channel.send(say)

client.run(TOKEN)
