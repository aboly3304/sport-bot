from telegram import Update
from telegram.ext import ContextTypes

class SOSHandlers:

    @staticmethod
    async def sos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🚨 درخواست اضطراری ثبت شد")
