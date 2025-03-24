import sys
import os
import asyncio
from pyrogram.errors import *
from database.users_db import db
from pyrogram import Client, filters
from info import ADMINS

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

@Client.on_message(filters.private & filters.command("users") & filters.user(ADMINS))
async def users(bot, update):
    total_users = await db.total_users_count()
    text = "Bot Status\n"
    text += f"\nTotal Users: {total_users}"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(ADMINS))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying To Restarting.....</i>",
        quote=True
    )
    await asyncio.sleep(2)
    await msg.edit("<i>Server Restarted Successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2
