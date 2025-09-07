from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")  # Render ke Dashboard > Environment Variables me BOT_TOKEN add karna

def start(update, context):
    update.message.reply_text("✅ Bot is alive and responding!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
