from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Function to send Global Unban Request
async def send_gban_request(client, message):
    # Define your request message here
    request_text = f"""🛑 #New_Global_Unban_Request 🛑
    User: {message.from_user.mention}
    User ID: {message.from_user.id}
    Reason: {message.text}
    Requested by: {message.from_user.mention}
    """

    # Define the inline keyboard for approval or decline
    buttons = [
        [
            InlineKeyboardButton("Approve", callback_data=f"approve_gban_{message.from_user.id}"),
            InlineKeyboardButton("Decline", callback_data=f"decline_gban_{message.from_user.id}")
        ]
    ]
    
    # Send the message to the admin group/channel with buttons
    await client.send_message(
        chat_id=ADMIN_CHAT_ID,  # Replace with your admin group ID
        text=request_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# Callback query handler to manage approval or decline
@Client.on_callback_query(filters.regex(r"^(approve_gban|decline_gban)_\d+$"))
async def handle_gban_approval(client, callback_query):
    action, user_id = callback_query.data.split('_')[0], int(callback_query.data.split('_')[2])
    
    if action == "approve_gban":
        # Logic to ban the user globally
        await client.ban_chat_member(chat_id=GBAN_GROUP_ID, user_id=user_id)  # Example command to ban
        await callback_query.answer("User globally banned!", show_alert=True)
    else:
        await callback_query.answer("Ban request declined!", show_alert=True)

    # Optionally delete the original request message
    await callback_query.message.delete()