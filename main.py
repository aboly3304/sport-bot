import logging
from telegram.ext import Application, CommandHandler

from config import BOT_TOKEN
from handlers.common import CommonHandlers
from handlers.admin import AdminHandlers
from handlers.registration import RegistrationHandlers
from handlers.sos import SOSHandlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    common = CommonHandlers()
    admin = AdminHandlers()
    registration = RegistrationHandlers()
    sos = SOSHandlers()

    application.add_handler(CommandHandler("start", common.start))
    application.add_handler(CommandHandler("help", common.help))
    application.add_handler(CommandHandler("register", registration.register))
    application.add_handler(CommandHandler("sos", sos.sos))
    application.add_handler(CommandHandler("admin", admin.admin_panel))

    application.run_polling()

if __name__ == "__main__":
    main()
