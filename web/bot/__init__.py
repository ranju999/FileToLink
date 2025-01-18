from pyrogram import Client
from info import *
from os import getcwd

Webxav= Client(
    name='Web Streamer',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=SLEEP_THRESHOLD,
    workers=WORKERS
)

multi_clients = {}
work_loads = {}
