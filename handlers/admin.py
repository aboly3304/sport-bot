from telegram import Update
from telegram.ext import ContextTypes

class AdminHandlers:

    @staticmethod
    async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🛠 پنل ادمین")
