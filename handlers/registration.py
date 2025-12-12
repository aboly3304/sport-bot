from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

class RegistrationHandlers:

    END = ConversationHandler.END

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("📝 شروع ثبت‌نام")
        return RegistrationHandlers.END
