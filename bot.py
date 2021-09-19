from server_info import get_info
from weather import get_weather
from aiogram import Bot, Dispatcher, executor

from config import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["show"])
async def start_command(message):
    await bot.send_message(message.chat.id, get_info())


@dp.message_handler(commands=["weather"])
async def start_command(message):
    await bot.send_message(message.chat.id, get_weather())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
