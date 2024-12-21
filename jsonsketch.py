import html
import random

import requests
import json
from bs4 import BeautifulSoup
import re

def clean_com(text: str) -> str:
    text =BeautifulSoup(text, "html.parser").get_text()#
    text =html.unescape(text)#
    text=re.sub(r'http[s]?://\S+', '', text)
    return text

def get_most_popular_thread(board):
    url = f"https://2ch.hk/{board}/threads.json"
    response = requests.get(url)

    if response.status_code == 200:
        threads_data = json.loads(response.content.decode('utf-8'))

        most_popular_thread = max(
            threads_data['threads'],
            key=lambda x: x.get('posts_count', 0)
        )

        # Формируем ссылку на тред
        thread_link = f"https://2ch.hk/{board}/res/{most_popular_thread['num']}.html"
        return {
            "id": most_popular_thread['num'],
            "subject": most_popular_thread.get('subject', 'Нет заголовка'),
            "posts_count": most_popular_thread['posts_count'],
            "score": most_popular_thread.get('score', 0),
            "comment": clean_com(most_popular_thread.get('comment', 'Нет комментария')),
            "link": thread_link
        }
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def get_most_rating_thread(board):
    url = f"https://2ch.hk/{board}/threads.json"
    response = requests.get(url)

    if response.status_code == 200:
        threads_data = json.loads(response.content.decode('utf-8'))

        most_rating_thread = max(
            threads_data['threads'],
            key=lambda x: x.get('score', 0)
        )

        # Формируем ссылку на тред
        thread_link = f"https://2ch.hk/{board}/res/{most_rating_thread['num']}.html"
        return {
            "id": most_rating_thread['num'],
            "subject": most_rating_thread.get('subject', 'Нет заголовка'),
            "posts_count": most_rating_thread['posts_count'],
            "score": most_rating_thread.get('score', 0),
            "comment": clean_com(most_rating_thread.get('comment', 'Нет комментария')),
            "link": thread_link
        }
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def get_most_last_thread(board):
    url = f"https://2ch.hk/{board}/threads.json"
    response = requests.get(url)

    if response.status_code == 200:
        threads_data = json.loads(response.content.decode('utf-8'))

        most_popular_thread = max(
            threads_data['threads'],
            key=lambda x: x.get('timestamp', 0)
        )

        # Формируем ссылку на тред
        thread_link = f"https://2ch.hk/{board}/res/{most_popular_thread['num']}.html"
        return {
            "id": most_popular_thread['num'],
            "subject": most_popular_thread.get('subject', 'Нет заголовка'),
            "posts_count": most_popular_thread['posts_count'],
            "score": most_popular_thread.get('score', 0),
            "comment": clean_com(most_popular_thread.get('comment', 'Нет комментария')),
            "link": thread_link
        }
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def get_random_thread(board):
    url = f"https://2ch.hk/{board}/threads.json"
    response = requests.get(url)

    if response.status_code == 200:
        threads_data = json.loads(response.content.decode('utf-8'))

        most_popular_thread = random.choice(
            threads_data['threads'])
        # Формируем ссылку на тред
        thread_link = f"https://2ch.hk/{board}/res/{most_popular_thread['num']}.html"
        return {
            "id": most_popular_thread['num'],
            "subject": most_popular_thread.get('subject', 'Нет заголовка'),
            "posts_count": most_popular_thread['posts_count'],
            "score": most_popular_thread.get('score', 0),
            "comment": clean_com(most_popular_thread.get('comment', 'Нет комментария')),
            "link": thread_link
        }
    else:
        print(f"Ошибка: {response.status_code}")
        return None
