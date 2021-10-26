# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import mimetypes

def detect_type(m: Message):
    if m.document:
        return m.document
    elif m.video:
        return m.video
    elif m.audio:
        return m.audio
    else:
        return
    

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def media_receive_handler(_, m: Message):
    file = detect_type(m)
    file_name = ''
    if file:
        if file.file_name:
            file_name = file.file_name
        else:
            if file.mime_type.startswith("video/"):
                file_name = "video" + str(m.date) + ".mp4"
            elif file.mime_type.startswith("audio/"):
                file_name = "audio" + str(m.date) + ".mp3"
            else:
                file_name = str(m.date)
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + str(log_msg.message_id) + '/' +quote_plus(file_name) if file_name else ''
    await m.reply_text(
        text="`{}`".format(stream_link),
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Open', url=stream_link)]])
    )
