from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎭 הצגות", callback_data="plays_menu")],
        [InlineKeyboardButton("🎤 הופעות", callback_data="concerts_menu")],
        [InlineKeyboardButton("💿 אלבומים", callback_data="albums_menu")],
        [InlineKeyboardButton("📀 דיסקים", callback_data="discs_menu")]
    ]
    await update.message.reply_text("בחר קטגוריה:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # תתי קטגוריות להצגות
    if query.data == "plays_menu":
        keyboard = [
            [InlineKeyboardButton("הצגה 1 🎬", callback_data="play1")],
            [InlineKeyboardButton("הצגה 2 🎭", callback_data="play2")],
            [InlineKeyboardButton("⬅️ חזרה לתפריט הראשי", callback_data="main_menu")]
        ]
        await query.edit_message_text("בחר הצגה:", reply_markup=InlineKeyboardMarkup(keyboard))

    # תתי קטגוריות להופעות
    elif query.data == "concerts_menu":
        keyboard = [
            [InlineKeyboardButton("הופעה בתל אביב", callback_data="concert_tlv")],
            [InlineKeyboardButton("הופעה בירושלים", callback_data="concert_jlm")],
            [InlineKeyboardButton("⬅️ חזרה לתפריט הראשי", callback_data="main_menu")]
        ]
        await query.edit_message_text("בחר הופעה:", reply_markup=InlineKeyboardMarkup(keyboard))

    # תתי קטגוריות לאלבומים
    elif query.data == "albums_menu":
        keyboard = [
            [InlineKeyboardButton("אלבום הבכורה", callback_data="album1")],
            [InlineKeyboardButton("המסע", callback_data="album2")],
            [InlineKeyboardButton("⬅️ חזרה לתפריט הראשי", callback_data="main_menu")]
        ]
        await query.edit_message_text("בחר אלבום:", reply_markup=InlineKeyboardMarkup(keyboard))

    # תתי קטגוריות לדיסקים
    elif query.data == "discs_menu":
        keyboard = [
            [InlineKeyboardButton("דיסק 1", callback_data="disc1")],
            [InlineKeyboardButton("דיסק 2", callback_data="disc2")],
            [InlineKeyboardButton("⬅️ חזרה לתפריט הראשי", callback_data="main_menu")]
        ]
        await query.edit_message_text("בחר דיסק:", reply_markup=InlineKeyboardMarkup(keyboard))

    # הצגה של וידאו לדוגמה
    elif query.data == "play1":
        await context.bot.send_video(chat_id=query.message.chat_id, video="https://your-link.com/play1.mp4", caption="הצגה 1 🎬")
    elif query.data == "play2":
        await context.bot.send_video(chat_id=query.message.chat_id, video="https://your-link.com/play2.mp4", caption="הצגה 2 🎭")

    # דוגמאות לקטגוריות אחרות
    elif query.data == "concert_tlv":
        await context.bot.send_video(chat_id=query.message.chat_id, video="https://your-link.com/concert_tlv.mp4", caption="הופעה בתל אביב 🎤")
    elif query.data == "album1":
        await context.bot.send_video(chat_id=query.message.chat_id, video="https://your-link.com/album1.mp4", caption="אלבום הבכורה 💿")

    elif query.data == "main_menu":
        await start(update, context)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
