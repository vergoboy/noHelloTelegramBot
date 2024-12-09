from telethon import TelegramClient, events

api_id = ''
api_hash = ''
bot_token = ''

client = TelegramClient('session_name', api_id, api_hash)

users_who_liked = set()

message_text = f"""
سلام! 👋

برای ادامه‌ی گفتگو با من، لطفاً این پیام را لایک کنید:
👉 [پست کانال](https://t.me/noHello_info/8)

بعد از اینکه لایک کردید، برگردید و دوباره پیام بدید تا بتونیم چت کنیم! 😊
"""

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    user_id = event.sender_id

    if user_id in users_who_liked:
        await event.reply('سلام! چطور می‌تونم کمکت کنم؟ 😊')
    else:
        await event.reply(message_text)


async def check_if_user_liked(user_id):
    """
    """
    try:
        message = await client.get_messages(channel_username, ids=post_id)
        for reaction in message.reactions.results:
            if user_id in reaction.users:
                return True
    except Exception as e:
        print(f"خطا در بررسی لایک‌ها: {e}")
    return False


@client.on(events.NewMessage)
async def check_likes_periodically(event):
    user_id = event.sender_id

    if user_id not in users_who_liked:
        liked = await check_if_user_liked(user_id)
        if liked:
            users_who_liked.add(user_id)
            await event.reply('ممنون که پست رو لایک کردی! حالا می‌تونیم گپ بزنیم 😊')


print("✨ ربات در حال اجراست... ✨")
client.start()
client.run_until_disconnected()
