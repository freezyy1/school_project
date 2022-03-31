# импортируем необходимые библиотеки
import telebot
from tokens import api_telegram
bot = telebot.TeleBot(api_telegram)
import sqlite3

def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f'DELETE FROM login_id WHERE id={people_id}')
    connect.commit()
    bot.send_message(message.chat.id, 'вы успешно отписались от рассылки')


def upload(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            id INTEGER
        )""")
    connect.commit()

    people_id = message.chat.id
    cursor.execute(f'SELECT id FROM login_id WHERE id = {people_id}')
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
        bot.send_message(message.chat.id, 'вы успешно подписались на рассылку')
    else:
        bot.send_message(message.chat.id, 'вы уже были подписаны на рассылку')
