import os
import telebot
from jsonsketch import get_most_popular_thread, get_most_rating_thread, get_most_last_thread, get_random_thread

TOKEN = os.getenv('TOKEN')
TOKENB=''

bot = telebot.TeleBot(TOKENB)
user_data={}


boards = ['2d', 'aa', 'cute', 'es', 'a', 'fd', 'ma']

commands = {
    '1': "Посмотреть данные по самому популярному треду",
    '2': "Посмотреть данные по самому высокорейтинговому треду",
    '3': "Посмотреть последний тред",
    '4': "Посмотреть случайный тред"}


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
                                  "4. Посмотреть случайный тред")
        bot.register_next_step_handler(message, process_command)
    else:
        bot.send_message(user_id, "Ты ввел неверную доску! Пожалуйста, выбери из списка доступных досок.")
        bot.register_next_step_handler(message, process_board)

def process_command(message):
    user_id = message.chat.id
    user_input = message.text.strip()

    #
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
                                         f"Ссылка: {most_popular_thread['link']}")
            else:
                bot.send_message(user_id, "Не удалось получить данные о самом популярном треде.")
        elif user_input == '2':
            # Функция для высокорейтингового треда
            most_rating_thread = get_most_rating_thread(board)
            if most_rating_thread:
                bot.send_message(user_id,
                                 f"Самый популярный тред на доске {board}:\n"
                                 f"Заголовок: {most_rating_thread['subject']}\n"
                                 f"Количество постов: {most_rating_thread['posts_count']}\n"
                                 f"Рейтинг: {most_rating_thread['score']}\n"
                                 f"Комментарий: {most_rating_thread['comment']}\n"
                                 f"Ссылка: {most_rating_thread['link']}")
            else:
                bot.send_message(user_id, "Не удалось получить данные о самом рейтинговом треде.")
        elif user_input == '3':
            # Функция для последнего треда
            most_last_thread = get_most_last_thread(board)
            if most_last_thread:
                bot.send_message(user_id,
                                 f"Самый поcледний тред на доске {board}:\n"
                                 f"Заголовок: {most_last_thread['subject']}\n"
                                 f"Количество постов: {most_last_thread['posts_count']}\n"
                                 f"Рейтинг: {most_last_thread['score']}\n"
                                 f"Комментарий: {most_last_thread['comment']}\n"
                                 f"Ссылка: {most_last_thread['link']}")
            else:
                bot.send_message(user_id, "Не удалось получить данные о последнем треде.")
        elif user_input == '4':
            # Функция для рандомного треда
            random_thread = get_random_thread(board)
            if random_thread:
                bot.send_message(user_id,
                                 f"Случайный тред на доске {board}:\n"
                                 f"Заголовок: {random_thread['subject']}\n"
                                 f"Количество постов: {random_thread['posts_count']}\n"
                                 f"Рейтинг: {random_thread['score']}\n"
                                 f"Комментарий: {random_thread['comment']}\n"
                                 f"Ссылка: {random_thread['link']}")
            else:
                bot.send_message(user_id, "Не удалось получить данные о случайном треде треде.")
    else:
        bot.send_message(user_id, "Пожалуйста, выбери правильную команду:\n"
                                  "1. Посмотреть данные по самому популярному треду\n"
                                  "2. Посмотреть данные по самому высокорейтинговому треду\n"
                                  "3. Посмотреть последний тред\n"
                                  "4. Посмотреть случайный тред")
        bot.register_next_step_handler(message, process_command)
bot.polling()













