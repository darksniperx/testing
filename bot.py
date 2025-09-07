from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")   # Render env var me set karo
app = Flask(__name__)

# Telegram Application (async)
application = Application.builder().token(TOKEN).build()


# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is live ✅")


application.add_handler(CommandHandler("start", start))


# --- Flask route for webhook ---
@app.route("/" + TOKEN, methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "ok"


@app.route("/")
def home():
    return "Bot running ✅"


if __name__ == "__main__":
    # Flask ko Render pe run karwana h
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
