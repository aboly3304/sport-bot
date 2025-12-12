from telegram import Update
from telegram.ext import ContextTypes

class RegistrationHandlers:

    @staticmethod
    async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("📝 ثبت‌نام شما انجام شد")
