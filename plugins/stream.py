import os, asyncio, requests, string, random
from asyncio import TimeoutError
from web.bot import Webxav
from utils import humanbytes
from info import *
from urllib.parse import quote_plus
from pyrogram import Client, filters
from Script import script
from pyrogram.errors import *
from pyrogram.types import *

from web.utils.file_properties import get_name, get_hash, get_media_file_size

@Client.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(c: Client, m: Message):
    try:  # This is the outer try block
        msg = await m.copy(chat_id=BIN_CHANNEL)
        online = f"{URL}watch/{str(msg.id)}?hash={get_hash(msg)}"
        download = f"{URL}{str(msg.id)}?hash={get_hash(msg)}"

        a = await log_msg.reply_text(
            text=f"ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ : [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nUꜱᴇʀ ɪᴅ : {m.from_user.id}\nStream ʟɪɴᴋ : {online}",
            disable_web_page_preview=True, quote=True
        )
        k = await m.reply_text(
            text=script.CAPTION_TXT.format(get_name(msg), humanbytes(get_media_file_size(m))),
            quote=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ᴡᴀᴛᴄʜ •", url=online),
                InlineKeyboardButton("• ᴅᴏᴡɴʟᴏᴀᴅ •", url=download)
        ],[
               InlineKeyboardButton('• ᴡᴀᴛᴄʜ ɪɴ ᴡᴇʙ ᴀᴘᴘ •', web_app=WebAppInfo(url=online))]
            ])
        )
        await m.delete()  # Delete the original message after processing

        # Wait for 6 hours (21600 seconds)
        await asyncio.sleep(21600)  # Sleep for 6 hours

        # After 6 hours, delete `msg`, `a`, and `k`
        try:
            await log_msg.delete()
            await a.delete()
            await k.delete()
        except Exception as e:
            print(f"Error during deletion: {e}")

    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True)

@Client.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    try:  # This is the outer try block
        msg = await broadcast.forward(chat_id=BIN_CHANNEL)
        online = f"{URL}watch/{str(msg.id)}?hash={get_hash(msg)}"
        download = f"{URL}{str(msg.id)}?hash={get_hash(msg)}"

        await msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {online}",
            quote=True
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• ᴡᴀᴛᴄʜ •", url=online),
                    InlineKeyboardButton('• ᴅᴏᴡɴʟᴏᴀᴅ •', url=download)] 
            ])
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=BIN_CHANNEL,
                            text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
                            disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=BIN_CHANNEL, text=f"**#ERROR_TRACKEBACK:** `{e}`", disable_web_page_preview=True)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel!{e}**")


    
    
  
