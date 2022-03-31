# импортируем необходимые библиотеки
import telebot
from telebot import types
# импортируем данные для работы бота
from tokens import api_telegram, url_school
from checker import checker
from parser_for_site import news_list
from database import delete, upload
from weather import weather
bot = telebot.TeleBot(api_telegram)


# ниже представлен набор команд, которые умеет обрабатывать бот
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',' + '\n' +
                     'нажмите /help чтобы узнать команды, которые поддерживает бот')


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    # смотрите в database.py
    delete(message)


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    # смотрите в database.py
    upload(message)


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     '/start - запуск бота\n/help - команды бота\n/weather - узнать погоду'
                     '\n/timetable_junior - узнать расписание в младших классах'
                     '\n/timetable_middle - узнать расписание в средней школе'
                     '\n/timetable_high - узнать расписание в средней школе'
                     '\n/web - сайт школы'
                     '\n/zvonki - расписание звонков'
                     '\n/subscribe - подписаться на рассылку новостей'
                     '\n/unsubscribe - отписаться от рассылки новостей'
                     )


@bot.message_handler(commands=['weather'])
def weather_main(message):
    # смотрите weather.py
    weather(message)


@bot.message_handler(commands=['zvonki'])
def zvon(message):
    photo = open('imgs/rasp_zvon.JPG', 'rb')
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
    # смотрите в checker.py
    checker(message)


bot.polling(none_stop=True)
