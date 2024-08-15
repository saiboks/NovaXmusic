from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config import BOT_USERNAME

start_txt = """
𖣐 ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʟ ᴜ ᴄ ʏ • / ‹𝟹, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n𖣐 ᴘᴏᴡᴇʀᴇᴅ ʙʏ 𝐀𝐫𝐭𝐡𝐞𝐲 ♡゙ ᴍ ᴜ s ɪ ᴄ"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/PhoenixXsupport"),
          InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/nova_updats")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ec5d7ec6899af85241cd9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
