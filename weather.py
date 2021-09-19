import requests
from config import weather_url, yandex_api_key, locations, condition_dict


def get_weather_for_city(coordinates):
    auth = {
        "X-Yandex-API-Key": yandex_api_key
    }

    query_params = {
        "lat": coordinates[0],
        "lon": coordinates[1],
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
        for location in locations:
            weather_data.append(get_weather_for_city(location))

        info = f"😎КОНОНОВА😎 \n" \
               f"{weather_data[2][3]} \n" \
               f"🌡Температура: {weather_data[2][0]} ℃ \n" \
               f"🚶🏻Ощущается как: {weather_data[2][1]} ℃ \n" \
               f"💨Скорость ветра: {weather_data[2][2]} м/с \n" \
               f"💧Влажность воздуха: {weather_data[2][4]} %  \n\n" \
               f"🤒ШУВАЛОВА🤒 \n" \
               f"{weather_data[0][3]} \n" \
               f"🌡Температура: {weather_data[0][0]} ℃ \n" \
               f"🚶🏻Ощущается как: {weather_data[0][1]} ℃ \n" \
               f"💨Скорость ветра: {weather_data[0][2]} м/с \n" \
               f"💧Влажность воздуха: {weather_data[0][4]} %  \n\n" \
               f"🤡КУПЧИНО🤡 \n" \
               f"{weather_data[1][3]} \n" \
               f"🌡Температура: {weather_data[1][0]} ℃ \n" \
               f"🚶🏻Ощущается как: {weather_data[1][1]} ℃ \n" \
               f"💨Скорость ветра: {weather_data[1][2]} м/с \n" \
               f"💧Влажность воздуха: {weather_data[1][4]} %"
        return info
    except Exception as ex:
        return f"Превышен лимит запросов \n{ex}"
