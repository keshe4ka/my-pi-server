from server_info import get_info
from weather import get_weather
from aiogram import Bot, Dispatcher, executor
import aioschedule
import asyncio

from config import BOT_TOKEN, CHAT_ID

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["server_info"])
async def server_info_command(message):
    await bot.send_message(message.chat.id, get_info())


# @dp.message_handler(commands=["weather"])
# async def weather_command(message):
#     await bot.send_message(message.chat.id, f"{message.chat.id}")


async def send_weather():
    await bot.send_message(CHAT_ID, "Мужики, вот сводки по погоде")
    await bot.send_message(CHAT_ID, get_weather())


async def send_good_morning_message():
    await bot.send_message(CHAT_ID, "Ребятули, всем доброго утра и хорошего настроения! :)")
    await bot.send_photo(CHAT_ID, f"/photos/1.jpg")


async def test():
    await bot.send_message(CHAT_ID, "test")


async def scheduler():
    aioschedule.every().day.at("18:08").do(test)
    aioschedule.every().day.at("06:00").do(send_weather)
    aioschedule.every().day.at("06:00").do(send_weather)
    aioschedule.every().day.at("08:00").do(send_weather)
    aioschedule.every().day.at("10:00").do(send_weather)
    aioschedule.every().day.at("11:00").do(send_good_morning_message)
    aioschedule.every().day.at("12:00").do(send_weather)
    aioschedule.every().day.at("14:00").do(send_weather)
    aioschedule.every().day.at("16:00").do(send_weather)
    aioschedule.every().day.at("18:00").do(send_weather)
    aioschedule.every().day.at("20:00").do(send_weather)
    aioschedule.every().day.at("22:00").do(send_weather)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
