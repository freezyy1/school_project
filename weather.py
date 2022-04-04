import requests
import telebot
from tokens import url, api_weather, api_telegram, city, admin
bot = telebot.TeleBot(api_telegram)
import logging
import time


def weather(message):
    try:
        # здесь можно было бы ввести вместо Тюмень message.text, чтобы отслеживать сообщения и по ним передавать
        # данные о погоде
        city_name = city

        params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)
        weather = result.json()

        # условие для температуры воздуха для выявление актировки
        if weather["main"]['temp'] > 29:
            temp = "Сейчас прохладно"
        elif weather["main"]['temp'] < 29:
            temp = "Сегодня холодно"
        elif weather["main"]['temp'] < 32:
            temp = "сегодня актировка у 1-9 классов"
        elif weather["main"]['temp'] < 36:
            temp = "Также у 10 и 11 классов"

        # условие для скорости ветра
        if weather["wind"]['speed'] == 0:
            wind = "По шкале Бофорта сейчас Штиль"
        elif 1.5 >= weather["wind"]['speed'] >= 0.5:
            wind = "По шкале Бофорта сейчас тихий ветер "
        elif 1.6 <= weather["wind"]['speed'] <= 3.3:
            wind = "По шкале Бофорта сейчас легкий ветер"
        elif 3.4 <= weather["wind"]['speed'] <= 5.4:
            wind = "По шкале Бофорта сейчас слабый ветер"
        elif 5.5 <= weather["wind"]['speed'] <= 7.9:
            wind = "По шкале Бофорта сейчас умеренный ветер"
        elif 8.0 <= weather["wind"]['speed'] <= 10.7:
            wind = "По шкале Бофорта сейчас свежий ветер"
        elif 10.8 <= weather["wind"]['speed'] <= 13.8:
            wind = "По шкале Бофорта сейчас сильный ветер"

        bot.send_message(message.chat.id,
                         "В городе " + str(weather["name"]) + " температура: " + str(
                             int(weather["main"]['temp'])) + '°' + "\n" +
                         "Максимальная температура:" + str(int(weather['main']['temp_max'])) + "\n" +
                         "Минимальная температура: " + str(int(weather['main']['temp_min'])) + "\n" +
                         "Скорость ветра: " + str(int(weather['wind']['speed'])) + ' м/c' + "\n" +
                         "Давление: " + str(int(weather['main']['pressure'])) + 'мм рт. ст.' + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "Видимость: " + str(weather['visibility']) + "\n" +
                         "Описание: " + str(weather['weather'][0]["description"]) + "\n" + temp + "\n" + wind + '\n')
    except:
        # исполняется в случае неправильного отображения погоды
        bot.send_message(message.chat.id, f'похоже что-то не так с api погоды\n напишите пожалуйста нашему админу{admin}')
        logging.error(f"Api погоды не работает корректно!, {time.ctime()}")





























