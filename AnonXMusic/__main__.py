import asyncio
import importlib

from pyrogram import idle, Client, filters
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from AnonXMusic.utils.gban_approval import send_gban_request, handle_gban_approval  # GBan approval ka functionality import


# SUDO_USERS ko config se load karna
SUDO_USERS = [123456789, 987654321]  # Yahan apne sudo user IDs daal do

# Global ban request command ko handle karna
@app.on_message(filters.command("gban") & filters.user(SUDO_USERS))
async def gban_command(client, message):
    # Request ko admin ke pass bhejna
    await send_gban_request(client, message)
    await message.reply_text("Gban request sent to admins for approval!")

# Callback query handle karna (approve/decline)
@app.on_callback_query(filters.regex(r"^(approve_gban|decline_gban)_\d+$"))
async def handle_callback_query(client, callback_query):
    await handle_gban_approval(client, callback_query)

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("✦ Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("✦ Successfully Imported Modules...💞")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AnonXMusic").error(
            "✦ Please turn on the videochat of your log group/channel.\n\n✦ Stopping Bot...💣"
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("AnonXMusic").info(
        "✦ EDIT BY ➥ ROY EDITX...🐝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AnonXMusic").info("❖ Stopping AVISHA Music Bot...💌")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())