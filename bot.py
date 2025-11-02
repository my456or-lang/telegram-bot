from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הבוט פעיל ועובד!")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"שגיאה התרחשה: {context.error}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # מוסיף פקודת /start
    application.add_handler(CommandHandler("start", start))
    
    # מוסיף טיפול בשגיאות
    application.add_error_handler(error_handler)

    # מריץ את הבוט עם ניקוי עדכונים ישנים
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
