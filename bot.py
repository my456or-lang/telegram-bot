import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# הגדרות לוגים
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# הטוקן יילקח ממשתנה סביבה ב-Render
TOKEN = os.environ.get('BOT_TOKEN', 'הכנס_כאן_את_הטוקן_שלך_אם_מריץ_מקומי')

# פונקציית התחלה - תפריט ראשי
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎵 דיסקים", callback_data='disks')],
        [InlineKeyboardButton("🎭 הצגות", callback_data='shows')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'שלום! ברוך הבא לבוט שלי 👋\n'
        'בחר אחת מהאופציות:',
        reply_markup=reply_markup
    )

# טיפול בלחיצות על כפתורים
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # תפריט דיסקים
    if query.data == 'disks':
        keyboard = [
            [InlineKeyboardButton("💿 דיסק 1 - מוזיקה ישראלית", callback_data='disk_1')],
            [InlineKeyboardButton("💿 דיסק 2 - מוזיקה עולמית", callback_data='disk_2')],
            [InlineKeyboardButton("💿 דיסק 3 - מוזיקה קלאסית", callback_data='disk_3')],
            [InlineKeyboardButton("🔙 חזרה לתפריט הראשי", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            'בחר דיסק:',
            reply_markup=reply_markup
        )
    
    # תפריט הצגות
    elif query.data == 'shows':
        keyboard = [
            [InlineKeyboardButton("🎭 הצגה 1 - קומדיה", callback_data='show_1')],
            [InlineKeyboardButton("🎭 הצגה 2 - דרמה", callback_data='show_2')],
            [InlineKeyboardButton("🎭 הצגה 3 - מחזמר", callback_data='show_3')],
            [InlineKeyboardButton("🔙 חזרה לתפריט הראשי", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            'בחר הצגה:',
            reply_markup=reply_markup
        )
    
    # בחירת דיסק ספציפי
    elif query.data.startswith('disk_'):
        disk_num = query.data.split('_')[1]
        keyboard = [[InlineKeyboardButton("🔙 חזרה לדיסקים", callback_data='disks')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            f'בחרת דיסק {disk_num}!\n\n'
            f'כאן אפשר להוסיף מידע על הדיסק, קישורים להאזנה וכו...',
            reply_markup=reply_markup
        )
    
    # בחירת הצגה ספציפית
    elif query.data.startswith('show_'):
        show_num = query.data.split('_')[1]
        keyboard = [[InlineKeyboardButton("🔙 חזרה להצגות", callback_data='shows')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            f'בחרת הצגה {show_num}!\n\n'
            f'כאן אפשר להוסיף מידע על ההצגה, מועדים, כרטיסים וכו...',
            reply_markup=reply_markup
        )
    
    # חזרה לתפריט ראשי
    elif query.data == 'main_menu':
        keyboard = [
            [InlineKeyboardButton("🎵 דיסקים", callback_data='disks')],
            [InlineKeyboardButton("🎭 הצגות", callback_data='shows')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            'ברוך הבא לבוט שלי 👋\n'
            'בחר אחת מהאופציות:',
            reply_markup=reply_markup
        )

# פונקציה ראשית להרצת הבוט
def main():
    # יצירת האפליקציה
    application = Application.builder().token(TOKEN).build()
    
    # הוספת handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # הרצת הבוט
    logger.info("הבוט מתחיל לעבוד...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
