from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, InlineQueryHandler

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

async def start(update, context):
    """ شروع کار ربات با ارسال پیام خوش‌آمدگویی """
    await update.message.reply_text('سلام! این یه ربات اینلاین هست. برای استفاده، آیدی من رو تایپ کن و یه فاصله بذار!')

async def inlinequery(update, context):
    """ هندلر برای کوئری اینلاین """
    query = update.inline_query.query
    if not query: 
        return

    result = InlineQueryResultArticle(
        id='1',
        title="Send for this",
        input_message_content=InputTextMessageContent('در حال ارسال پیام‌ها...'),
        description="روی این کلیک کن تا چند پیام و عکس ارسال بشه"
    )

    await update.inline_query.answer([result])  # اینجا await اضافه شد

async def send_content(update, context):
    """ ارسال چند پیام و عکس به کاربر """
    chat_id = update.effective_chat.id
    
    messages = [
        "فکر کن به یکی زنگ بزنی بگی سلام بعد تماس بزاری روی انتظار... 🤦‍♂",
        "",
    ]

    images = [
        'https://raw.githubusercontent.com/vergoboy/noHelloTelegramBot/refs/heads/main/photo1.jpg',
        'https://raw.githubusercontent.com/vergoboy/noHelloTelegramBot/refs/heads/main/photo2.jpg',
    ]

    for message in messages:
        await context.bot.send_message(chat_id=chat_id, text=message)  # اضافه شدن await
    
    for image_url in images:
        await context.bot.send_photo(chat_id=chat_id, photo=image_url)  # اضافه شدن await

def main():
    """ ساخت و اجرای ربات """
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(InlineQueryHandler(inlinequery))
    application.add_handler(CommandHandler("send_content", send_content))

    application.run_polling()

if __name__ == '__main__':
    main()
