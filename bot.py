from server_info import get_info
from weather import get_weather
from statistic import collect_statistic
from anecdote import get_joke

from aiogram import Bot, Dispatcher, executor
import aioschedule
import asyncio

from config import BOT_TOKEN, CHAT_ID

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["server_info"])
async def server_info_command(message):
    await bot.send_message(message.chat.id, get_info())


@dp.message_handler(commands=["joke"])
async def server_info_command(message):
    await bot.send_message(message.chat.id, "Вот юморесочка такая вот держи")
    await bot.send_message(message.chat.id, get_joke())


# к сожалению, мужики удалили бота из конфы
#
# async def send_weather():
#     await bot.send_message(CHAT_ID, "Мужики, вот сводки по погоде")
#     await bot.send_message(CHAT_ID, get_weather())
#
#
# async def send_good_morning_message():
#     await bot.send_animation(CHAT_ID, "https://c.tenor.com/R_q5ErjROlIAAAAC/smile-big-smile.gif")


async def scheduler():
    aioschedule.every(300).seconds.do(collect_statistic)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
