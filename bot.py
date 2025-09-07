from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler
import os

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>✅ Flask + Telegram Bot is running on Render!</h2>"

# Telegram Bot
def start(update, context):
    update.message.reply_text("🤖 Bot is alive and working on Render!")

def run_bot():
    TOKEN = os.getenv("BOT_TOKEN")  # BOT_TOKEN ko Render dashboard me Environment Variable me set karo
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

# Thread me bot run karna (Flask ke sath parallel me)
Thread(target=run_bot).start()
