import telebot
from tokens import api_telegram
from timetable import *
bot = telebot.TeleBot(api_telegram)


def checker(message):
    list_for_a = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10А', '11A']
    list_for_b = ['1Б', '2Б', '3Б', '4Б', '5Б', '6Б', '7Б', '8Б', '9Б', '10Б', '11Б']
    list_for_B = ['1В', '2В', '3В', '4В', '5В', '6В', '7В', '8В', '9В', '10В', '11В']
    list_for_g = ['1Г', '2Г', '3Г', '4Г', '5Г', '6Г', '7Г', '8Г', '9Г', '10Г', '11Г']
    if message.text == list_for_a[0]:
        bot.send_message(message.chat.id, text=q1)
    elif message.text == list_for_a[1]:
        bot.send_message(message.chat.id, text=q2)
    elif message.text == list_for_a[2]:
        bot.send_message(message.chat.id, text=q3)
    elif message.text == list_for_a[3]:
        bot.send_message(message.chat.id, text=q4)
    elif message.text == list_for_a[4]:
        bot.send_message(message.chat.id, text=q5)
    elif message.text == list_for_a[5]:
        bot.send_message(message.chat.id, text=q6)
    elif message.text == list_for_a[6]:
        bot.send_message(message.chat.id, text=q7)
    elif message.text == list_for_a[7]:
        bot.send_message(message.chat.id, text=q8)
    elif message.text == list_for_a[8]:
        bot.send_message(message.chat.id, text=q9)
    elif message.text == list_for_a[9]:
        bot.send_message(message.chat.id, text=q10)
    elif message.text == list_for_a[10]:
        bot.send_message(message.chat.id, text=q11)
    elif message.text == list_for_b[0]:
        bot.send_message(message.chat.id, text=q12)
    elif message.text == list_for_b[1]:
        bot.send_message(message.chat.id, text=q13)
    elif message.text == list_for_b[2]:
        bot.send_message(message.chat.id, text=q14)
    elif message.text == list_for_b[3]:
        bot.send_message(message.chat.id, text=q15)
    elif message.text == list_for_b[4]:
        bot.send_message(message.chat.id, text=q16)
    elif message.text == list_for_b[5]:
        bot.send_message(message.chat.id, text=q17)
    elif message.text == list_for_b[6]:
        bot.send_message(message.chat.id, text=q18)
    elif message.text == list_for_b[7]:
        bot.send_message(message.chat.id, text=q19)
    elif message.text == list_for_b[8]:
        bot.send_message(message.chat.id, text=q20)
    elif message.text == list_for_b[9]:
        bot.send_message(message.chat.id, text=q21)
    elif message.text == list_for_b[10]:
        bot.send_message(message.chat.id, text=q22)
    elif message.text == list_for_B[0]:
        bot.send_message(message.chat.id, text=q23)
    elif message.text == list_for_B[1]:
        bot.send_message(message.chat.id, text=q24)
    elif message.text == list_for_B[2]:
        bot.send_message(message.chat.id, text=q25)
    elif message.text == list_for_B[3]:
        bot.send_message(message.chat.id, text=q26)
    elif message.text == list_for_B[4]:
        bot.send_message(message.chat.id, text=q27)
    elif message.text == list_for_B[5]:
        bot.send_message(message.chat.id, text=q28)
    elif message.text == list_for_B[6]:
        bot.send_message(message.chat.id, text=q29)
    elif message.text == list_for_B[7]:
        bot.send_message(message.chat.id, text=q30)
    elif message.text == list_for_B[8]:
        bot.send_message(message.chat.id, text=q31)
    elif message.text == list_for_B[9]:
        bot.send_message(message.chat.id, text=q32)
    elif message.text == list_for_B[10]:
        bot.send_message(message.chat.id, text=q33)
    elif message.text == list_for_g[0]:
        bot.send_message(message.chat.id, text=q34)
    elif message.text == list_for_g[1]:
        bot.send_message(message.chat.id, text=q35)
    elif message.text == list_for_g[2]:
        bot.send_message(message.chat.id, text=q36)
    elif message.text == list_for_g[3]:
        bot.send_message(message.chat.id, text=q37)
    elif message.text == list_for_g[4]:
        bot.send_message(message.chat.id, text=q38)
    elif message.text == list_for_g[5]:
        bot.send_message(message.chat.id, text=q39)
    elif message.text == list_for_g[6]:
        bot.send_message(message.chat.id, text=q40)
    elif message.text == list_for_g[7]:
        bot.send_message(message.chat.id, text=q41)
    elif message.text == list_for_g[8]:
        bot.send_message(message.chat.id, text=q42)
    elif message.text == list_for_g[9]:
        bot.send_message(message.chat.id, text=q43)
    elif message.text == list_for_g[10]:
        bot.send_message(message.chat.id, text=q44)
