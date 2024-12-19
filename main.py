
import os
import telebot
import requests
import json

TOKEN = os.getenv('TOKEN')


TOKENB=''

bot = telebot.TeleBot(TOKENB)
user_data={}


boards = ['2d', 'aa', 'cute', 'es', 'a', 'fd', 'ma']

commands = {
    '1': "Посмотреть данные по самому популярному треду",
    '2': "Посмотреть данные по самому высокорейтинговому треду",
    '3': "Посмотреть последний тред",
    '4': "Посмотреть рандомный тред"
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Выбери нужную доску:\n"
                                      "2d - Аниме/Беседка,\n"
                                      "aa - Аниме арт,\n"
                                      "cute - Милое,\n"
                                      "es - Бесконечное Лето,\n"
                                      "a - Аниме,\n"
                                      "fd - Фэндом,\n"
                                      "ma - Манга")


@bot.message_handler(func=lambda message: True)
def handle_input(message):
    user_id = message.chat.id
    user_input = message.text.strip().lower()

    if user_id not in user_data:
        if user_input in boards:
            user_data[user_id] = {'argument': user_input, 'step': 'function_choice'}
            bot.send_message(user_id, "Данные приняты. Теперь выбери, что ты хочешь:\n"
                                      "1. Посмотреть данные по самому популярному треду\n"
                                      "2. Посмотреть данные по самому высокорейтинговому треду\n"
                                      "3. Посмотреть последний тред\n"
                                      "4. Посмотреть рандомный тред")
        else:
            bot.send_message(user_id, "Ты ввел неверную доску! Пожалуйста, выбери из списка доступных досок.")
            bot.send_message(user_id, "Выбери доску:\n" + '\n'.join([f"/{board}" for board in boards]))
            return

    elif user_data[user_id]['step'] == 'function_choice':
        if user_input in commands:

            bot.send_message(user_id, f"Ты выбрал: {commands[user_input]}")

            if user_input == '1':
                # Функция для популярного треда
                pass
            elif user_input == '2':
                # Функция для высокорейтингового треда
                pass
            elif user_input == '3':
                # Функция для последнего треда
                pass
            elif user_input == '4':
                # Функция для рандомного треда
                pass
        else:
            bot.send_message(user_id, "Пожалуйста, выбери правильную команду:\n"
                                      "1. Посмотреть данные по самому популярному треду\n"
                                      "2. Посмотреть данные по самому высокорейтинговому треду\n"
                                      "3. Посмотреть последний тред\n"
                                      "4. Посмотреть рандомный тред")

bot.polling()













