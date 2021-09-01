import values
import telebot


from config import bot_token

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['show'])
def start_command(message):
    bot.send_message(message.chat.id, values.info.string)


if __name__ == '__main__':
    bot.polling(none_stop=True)
