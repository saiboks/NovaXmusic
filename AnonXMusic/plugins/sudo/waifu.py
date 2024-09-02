from pyrogram import Client, filters
import requests
from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Arthey_bot?startgroup=true"),
    ],
]


waifu_api_url = 'https://api.waifu.im/search'

# IAM_DAXX

def get_waifu_data(tags):
    params = {
        'included_tags': tags,
        'height': '>=2000'
    }

    response = requests.get(waifu_api_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.on_message(filters.command("waifu"))
def waifu_command(client, message):
    try:
        tags = ['maid']  # You can customize the tags as needed
        waifu_data = get_waifu_data(tags)

        if waifu_data and 'images' in waifu_data:
            first_image = waifu_data['images'][0]
            image_url = first_image['url']
            message.reply_photo(image_url, caption=f"𖣐 ᴡᴀɪғᴜ ɪᴍɢ ʙʏ ➥ ʟ ᴜ ᴄ ʏ • / ‹𝟹", reply_markup=InlineKeyboardMarkup(EVAA),)
        else:
            message.reply_text("No waifu found with the specified tags.")

    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")
      
