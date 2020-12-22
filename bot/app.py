from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
from datetime import datetime, date, time
import os


data = {}

SETTING, SET_TIMER, LIVE, SPEND, EARN = range(5)

def start(update, context):
    # update.message.reply_text('Send me the sum on month: /set <sum>')
    update.message.reply_text('Привет! Давай начнём работу.\nОтправь мне сколько ты готов тратить в этот месяц ')

    return SETTING

def do_echo(update):
    update.message.reply_text(update.message.text)

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = os.getenv("TOKEN")
    updater = Updater(token=TOKEN, use_context=True, base_url="https://telegg.ru/orig/bot")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))


    message_handler = MessageHandler(Filters.text, do_echo)
    dp.add_handler(message_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()