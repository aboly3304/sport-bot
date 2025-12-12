from telegram import Update
from telegram.ext import ContextTypes

class CommonHandlers:

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("✅ ربات با موفقیت اجرا شد")

    @staticmethod
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("ℹ️ راهنمای ربات")

    @staticmethod
    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("❌ عملیات لغو شد")
