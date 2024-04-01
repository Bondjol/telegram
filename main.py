from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from time import sleep
import json
import asyncio
from function import clearLog, asciiIntro, forward, giveaway
with open('config.json', 'r') as file:
    data_json = json.loads(file.read())



# RUN : 
async def run():
    with open('config.json', 'r') as file:
        data_json = json.loads(file.read())
    # client = TelegramClient('session_name', api_id, api_hash)
    print('tunggu sebentar..')
    # await client.start()
    clearLog()
    print(asciiIntro)
    print('[-] 1. Auto give away')
    print('[-] 2. Auto forward')
    print('[-] 3. Cooming Soon')
    menu = int(input('Pilih menu : '))
    if menu == 1:
        giveaway()
    elif menu == 2:
        await forward(data_json)
    elif menu == 3:
        print('Cooming soon..')
        print('Kirim permintaan ke @si_bondjol')
        exit(code=0)
    else:
        pass
asyncio.run(run())