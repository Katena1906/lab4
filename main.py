
import os
import telebot
from jsonsketch import get_most_popular_thread

TOKEN = os.getenv('TOKEN')


TOKENB='7594677312:AAHbPxHvd5ZkBW7hwqzm4dJmssvbnQQEgMM'

bot = telebot.TeleBot(TOKENB)
user_data={}


boards = ['2d', 'aa', 'cute', 'es', 'a', 'fd', 'ma']

commands = {
    '1': "Посмотреть данные по самому популярному треду",
    '2': "Посмотреть данные по самому высокорейтинговому треду",
    '3': "Посмотреть последний тред"}


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
                                  "3. Посмотреть последний тред")
        bot.register_next_step_handler(message, process_command)
    else:
        bot.send_message(user_id, "Ты ввел неверную доску! Пожалуйста, выбери из списка доступных досок.")
        bot.register_next_step_handler(message, process_board)

def process_command(message):
    user_id = message.chat.id
    user_input = message.text.strip()

    board = user_data[user_id]['board']
    if user_input in commands:
        bot.send_message(user_id, f"Ты выбрал: {commands[user_input]}")
        # Выполнение соответствующей функции в зависимости от команды
        if user_input == '1':
            # Функция для популярного треда
            most_popular_thread=get_most_popular_thread(board)
            if most_popular_thread:
                bot.send_message(user_id,
                                    f"Самый популярный тред на доске {board}:\n" 
                                         f"Заголовок: {most_popular_thread['subject']}\n" 
                                         f"Количество постов: {most_popular_thread['posts_count']}\n" 
                                         f"Рейтинг: {most_popular_thread['score']}\n" 
                                         f"Комментарий: {most_popular_thread['comment']}\n" 
                                         f"Ссылка: {most_popular_thread['link']}")
            else:
                bot.send_message(user_id, "Не удалось получить данные о самом популярном треде.")
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
                                  "3. Посмотреть последний тред")
        bot.register_next_step_handler(message, process_command)
bot.polling()













