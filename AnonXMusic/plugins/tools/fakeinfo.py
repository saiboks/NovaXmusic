import requests
from pyrogram import Client
from pyrogram import filters
from AnonXMusic import app


random_user_api_url = 'https://randomuser.me/api/'


@app.on_message(filters.command("fake", prefixes="/"))
def generate_fake_user_by_country(client, message):
    country_name = message.text.split("/fake ", maxsplit=1)[1]
    
    # Call the RandomUser API to get fake user information for the specified country
    response = requests.get(f'{random_user_api_url}?nat={country_name}')
    
    if response.status_code == 200:
        user_info = response.json()['results'][0]
        # Extract user details
        first_name = user_info['name']['first']
        last_name = user_info['name']['last']
        email = user_info['email']
        country = user_info['location']['country']
        state = user_info['location']['state']
        city = user_info['location']['city']
        street = user_info['location']['street']['name']
        zip_code = user_info['location']['postcode']
        # Reply with the generated fake user information for the specified country
        message.reply_text(f"๏ ɴᴀᴍᴇ ➠ {first_name} {last_name}\n\n๏ ᴇᴍᴀɪʟ ➠ {email}\n\n๏ ᴄᴏᴜɴᴛʀʏ ➠ {country}\n\n๏ sᴛᴀᴛᴇ ➠ {state}\n\n๏ ᴄɪᴛʏ ➠ {city}\n\n๏ ᴀᴅᴅʀᴇss ➠ {street}\n\n๏ ᴢɪᴘ ᴄᴏᴅᴇ ➠ {zip_code}\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ ʟ ᴜ ᴄ ʏ • / ‹𝟹 ")
    else:
        message.reply_text(f"✦ ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ғᴀᴋᴇ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ {country_name}.")

