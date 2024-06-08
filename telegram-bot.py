import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Your bot token
TOKEN = '7390031408:AAHJ2ESzbZT_LbazD91NswGZiihN8cJBDhM'

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome Abdul Rauof!')

def main() -> None:
    # Create the application and pass it your bot's token
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler('start', start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
