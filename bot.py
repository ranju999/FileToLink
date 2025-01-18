from web import WebTime, __version__
from info import API_ID, API_HASH, BOT_TOKEN, PORT, ADMINS
from aiohttp import web
from web.server import web_server
from pyrogram import Client, idle
import pyromod.listen
import os
from typing import Union, Optional, AsyncGenerator
from pyrogram import types

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="postforwarder",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
            max_concurrent_transmissions=100,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        app = await web_server()
        app['bot'] = self  # Pass bot instance to the app
        runner = web.AppRunner(app)
        await runner.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(runner, bind_address, PORT).start()     
        print(f"| ❤ |==> Iꜱ Sᴛᴀʀᴛᴇᴅ ɪɴɪᴛɪᴀᴛᴇᴅ {me.first_name} <==| 🍿 |")
        await idle()
        await self.send_message(ADMINS, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️😅😅😅__**")
        
    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
       

bot=Bot()
bot.run()
