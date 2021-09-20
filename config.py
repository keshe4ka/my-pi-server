from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY")
CHAT_ID = os.environ.get("CHAT_ID")

# интервалы времени для функции uptime в server_info.py
intervals = (
    ('w', 604800),  # 60 * 60 * 24 * 7
    ('d', 86400),  # 60 * 60 * 24
    ('h', 3600),  # 60 * 60
    ('m', 60),
    ('s', 1),
)

# api яндекс погоды
weather_url = "https://api.weather.yandex.ru/v2/informers/"


# используется для получения погоды для конкретной локации
class Location:
    name = ""
    pos = [0, 0]

    def __init__(self, name, pos):
        self.name = name  # устанавливаем имя
        self.pos = pos

    def get_name(self):
        return self.name

    def get_position(self):
        return self.pos


# инициализация мест
kononova = Location("😎КОНОНОВА😎", ["64.502058", "40.694358"])
murino = Location("🤒ШУВАЛОВА🤒", ["60.059189", "30.429451"])
kupchino = Location("🤡КУПЧИНО🤡", ["59.851452", "30.323209"])

# список всех мест
locations = [kononova, murino, kupchino]

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
