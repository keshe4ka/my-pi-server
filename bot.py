import values
import telebot

from telebot import types

from config import bot_token

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['show'])
def start_command(message):
    bot.send_message(values.info)


if __name__ == '__main__':
    bot.polling(none_stop=True)
