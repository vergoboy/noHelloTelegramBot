from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, InlineQueryHandler

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

def start(update, context):
    update.message.reply_text('سلام! این یه ربات اینلاین هست. برای استفاده، آیدی من رو تایپ کن و یه فاصله بذار!')

def inlinequery(update, context):
    query = update.inline_query.query
    if not query: 
        return

    result = InlineQueryResultArticle(
        id='1',
        title="Send for this",
        input_message_content=InputTextMessageContent('در حال ارسال پیام‌ها...'),
        description="روی این کلیک کن تا چند پیام و عکس ارسال بشه"
    )

    update.inline_query.answer([result])

async def send_content(update, context):
    chat_id = update.effective_chat.id
    
    messages = [
        "پیام اول: سلام دوست عزیز! 😊",
        "پیام دوم: این یه آموزش ساخت ربات اینلاین هست!",
        "پیام سوم: امیدوارم که برات مفید باشه!",
    ]

    images = [
        'https://example.com/image1.jpg',
        'https://example.com/image2.jpg',
    ]

    for message in messages:
        await context.bot.send_message(chat_id=chat_id, text=message)
    
    for image_url in images:
        await context.bot.send_photo(chat_id=chat_id, photo=image_url)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(InlineQueryHandler(inlinequery))
    application.add_handler(CommandHandler("send_content", send_content))

    application.run_polling()

if __name__ == '__main__':
    main()
