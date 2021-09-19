from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

bot_token = os.environ.get("BOT_TOKEN")
yandex_api_key = os.environ.get("YANDEX_API_KEY")

# интервалы времени для функции uptime
intervals = (
    ('w', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),  # 60 * 60 * 24
    ('h', 3600),  # 60 * 60
    ('m', 60),
    ('s', 1),
)

# api яндекс погоды
weather_url = "https://api.weather.yandex.ru/v2/informers/"

# локации мест для погоды
murino_pos = ["60.059189", "30.429451"]
kupchino_pos = ["59.851452", "30.323209"]
kononva_pos = ["64.502058", "40.694358"]
locations = [murino_pos, kupchino_pos, kononva_pos]

# словарь состояния погоды
condition_dict = {
    "clear": "☀️Ясно",
    "partly-cloudy": "⛅️Малооблачно",
    "cloudy": "⛅️Облачно с прояснениями",
    "overcast": "☁️Пасмурно",
    "drizzle": "☂️Морось",
    "light-rain": "☂️Небольшой дождь",
    "rain": "☔️Дождь",
    "moderate-rain": "☔️Умеренно сильный дождь",
    "heavy-rain": "☔️☔️Сильный дождь",
    "continuous-heavy-rain": "☔️☔️Длительный сильный дождь",
    "showers": "☔️☔️☔️Ливень",
    "wet-snow": "Дождь со снегом",
    "light-snow": "❄️Небольшой снег",
    "snow": "❄️❄️Снег",
    "snow-showers": "❄️❄️❄️Снегопад",
    "hail": "☄️Град",
    "thunderstorm": "🌩Гроза",
    "thunderstorm-with-rain": "🌩Дождь с грозой",
    "thunderstorm-with-hail": "🌩Гроза с градом"
}
