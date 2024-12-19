
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
    bot.register_next_step_handler(message, process_board)

def process_board(message):
    user_id = message.chat.id
    user_input = message.text.strip().lower()

    if user_input in boards:
        user_data[user_id] = {'board': user_input, 'step': 'waiting_for_command'}
        bot.send_message(user_id, "Данные приняты. Теперь выбери, что ты хочешь:\n"
                                  "1. Посмотреть данные по самому популярному треду\n"
                                  "2. Посмотреть данные по самому высокорейтинговому треду\n"
                                  "3. Посмотреть последний тред\n"
                                  "4. Посмотреть рандомный тред")
        bot.register_next_step_handler(message, process_command)
    else:
        bot.send_message(user_id, "Ты ввел неверную доску! Пожалуйста, выбери из списка доступных досок.")
        bot.register_next_step_handler(message, process_board)

def process_command(message):
    user_id = message.chat.id
    user_input = message.text.strip()

    if user_input in commands:
        bot.send_message(user_id, f"Ты выбрал: {commands[user_input]}")
        # Выполнение соответствующей функции в зависимости от команды
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
        bot.register_next_step_handler(message, process_command)
bot.polling()













