from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot_token = os.environ.get("BOT_TOKEN")

# интервалы времени для функции uptime
intervals = (
    ('w', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),  # 60 * 60 * 24
    ('h', 3600),  # 60 * 60
    ('m', 60),
    ('s', 1),
)
