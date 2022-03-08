import telebot
from tokens import api_telegram
bot = telebot.TeleBot(api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',' + '\n' +
                     'нажмите /help чтобы узнать команды, которые поддерживает бот')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, 'здесь будут перечислены все команды, которые умеет обрабатывать бот')


bot.polling(none_stop=True)