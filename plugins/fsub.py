from pyrogram.errors import *
from pyrogram.types import *
from info import *
from Script import script

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2

async def get_fsub(bot, message):
    target_channel_id = AUTH_CHANNEL  # Your channel ID
    user_id = message.from_user.id
    try:
        await bot.get_chat_member(target_channel_id, user_id)
    except UserNotParticipant:
        channel_link = (await bot.get_chat(target_channel_id)).invite_link
        keyboard = [[InlineKeyboardButton(" ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=channel_link)],[InlineKeyboardButton("↻ ᴛʀʏ ᴀɢᴀɪɴ", url=f"https://t.me/{BOT_USERNAME}?start=start")]]
        await message.reply_photo(
            photo=(AUTH_PICS),
            caption=script.AUTH_TXT.format(message.from_user.mention),
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return False
    else:
        return True

#Dont Remove My Credit @Tech_Shreyansh
#This Repo Is By @SmartEdith_Bot 
# For Any Kind Of Error Ask Us In Support Group @Tech_Shreyansh2