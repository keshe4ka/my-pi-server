import requests
from config import weather_url, YANDEX_API_KEY, locations, condition_dict


def get_weather_for_city(location):
    auth = {
        "X-Yandex-API-Key": YANDEX_API_KEY
    }

    query_params = {
        "lat": location.get_position()[0],
        "lon": location.get_position()[1],
        "lang": "ru_RU"
    }

    response = requests.get(
        weather_url,
        params=query_params,
        headers=auth
    )

    answer = response.json()["fact"]

    # добавляет знак плюса
    def temp_editor(value):
        if value > 0:
            return f"+{value}"
        else:
            return value

    weather = [
        temp_editor(answer["temp"]),
        temp_editor(answer["feels_like"]),
        answer["wind_speed"],
        condition_dict[answer["condition"]],
        answer["humidity"]
    ]
    return weather


def get_weather():
    try:
        weather_data = []
        info = ""
        for index, location in enumerate(locations):
            weather_data.append(get_weather_for_city(location))
            info += f"{location.get_name()} \n" \
                    f"{weather_data[index][3]} \n" \
                    f"🌡Температура: {weather_data[index][0]} ℃ \n" \
                    f"🚶🏻Ощущается как: {weather_data[index][1]} ℃ \n" \
                    f"💨Скорость ветра: {weather_data[index][2]} м/с \n" \
                    f"💧Влажность воздуха: {weather_data[index][4]} % \n\n"
        return info
    except Exception as ex:
        return f"Превышен лимит запросов \n{ex}"
