import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and context.
async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Get your free followers here: http://freefollowers.ct.ws')

async def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle any message received."""
    text = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Received: {text}")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7280592829:AAEDF6KYufs2nicVtjabrdCvKOfmILGI348").build()  # <-- Replace with your Bot Token

    # Register the command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    application.run_polling()

if __name__ == '__main__':
    main()
