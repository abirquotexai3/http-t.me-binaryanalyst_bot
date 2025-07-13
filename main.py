import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import time
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

TOKEN = "7940316241:AAEb4TCc_iZpWTloCkrRY1XFTT4YjqL8HLY আপনার বট টোকেন
CHAT_ID = 7865578608  # আপনার চ্যাট আইডি (int টাইপে)

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 স্বাগতম! স্ক্রিনশট পাঠান, Prediction পাবেন।")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    time.sleep(2)

    photo_file = await update.message.photo[-1].get_file()
    photo_bytes = await photo_file.download_as_bytearray()
    image = Image.open(BytesIO(photo_bytes))

    # ছবিতে অ্যানোটেশন (ডেমো)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), "UP 78%", fill="green", font=font)
    image.save("annotated.png")

    # Prediction রেজাল্ট
    msg = "Prediction Result:\n👉 Next Candle: UP\n👉 Probability: 78%\n\nDisclaimer: Trading involves risk. Invest wisely."
    keyboard = [[InlineKeyboardButton("Join Telegram", url="http://t.me/abirquotexai3_bot")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    with open("annotated.png", "rb") as img_file:
        await update.message.reply_photo(img_file, caption=msg, reply_markup=reply_markup)

def main():
    app = Application.builder().token(7940316241:AAEb4TCc_iZpWTloCkrRY1XFTT4YjqL8HLY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()

if __name__ == "__main__":
    main()