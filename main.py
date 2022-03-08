# импортируем необходимые библиотеки
import requests
import telebot
from telebot import types
# импортируем данные для работы бота
from tokens import url, api_weather, api_telegram, url_school, city, admin
from checker import checker
from parser_for_site import news_list
photo = open('imgs/rasp_zvon.JPG', 'rb')
bot = telebot.TeleBot(api_telegram)


# ниже представлен набор команд, которые умеет обрабатывать бот
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',' + '\n' +
                     'нажмите /help чтобы узнать команды, которые поддерживает бот')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     '/start - запуск бота\n/help - команды бота\n/weather - узнать погоду'
                     '\n/timetable_junior - узнать расписание в младших классах'
                     '\n/timetable_middle - узнать расписание в средней школе'
                     '\n/timetable_high - узнать расписание в средней школе'
                     '\n/web - сайт школы'
                     '\n/zvonki - расписание звонков')


@bot.message_handler(commands=['weather'])
def test(message):
    try:
        # создаем глобальные переменные чтобы не было проблем с выводом локальных переменных в будущем
        global wind
        global temp

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
        #bot.send_message(message.chat.id, 'вы ввели город, которого нет в базе данных \n')
        # bot.send_message(message.chat.id, 'рестарт... \n')
        #bot.send_message(message.chat.id, 'введите название города')
        bot.send_message(message.chat.id, f'похоже что-то не так с api погоды\n напишите пожалуйста нашему админу{admin}')


@bot.message_handler(commands=['zvonki'])
def zvon(message):
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['web'])
def web(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Сайт школы', url=url_school)
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, news_list, reply_markup=markup)


@bot.message_handler(commands=['timetable_junior'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('1A', '1Б', '1В', '1Г')
    keyboard.row('2A', '2Б', '2В', '2Г')
    keyboard.row('3A', '3Б', '3В', '3Г')
    keyboard.row('4A', '4Б', '4В', '4Г')
    bot.send_message(message.chat.id, text='Выберите класс', reply_markup=keyboard)


@bot.message_handler(commands=['timetable_middle'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('5A', '5Б', '5В', '5Г')
    keyboard.row('6A', '6Б', '6В', '6Г')
    keyboard.row('7A', '7Б', '7В', '7Г')
    keyboard.row('8A', '8Б', '8В', '8Г')
    keyboard.row('9A', '9Б', '9В', '9Г')
    bot.send_message(message.chat.id, text='Выберите класс', reply_markup=keyboard)


@bot.message_handler(commands=['timetable_high'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('10A', '10Б', '10В', '10Г')
    keyboard.row('11A', '11Б', '11В', '11Г')
    bot.send_message(message.chat.id, text='Выберите класс', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def step1(message):
    checker(message)


bot.polling(none_stop=True)
