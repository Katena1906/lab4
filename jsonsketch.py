import requests
import json


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
            "comment": most_popular_thread.get('comment', 'Нет комментария'),
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
            "comment": most_rating_thread.get('comment', 'Нет комментария'),
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
         #ожидается чудо

        # Формируем ссылку на тред
        thread_link = f"https://2ch.hk/{board}/res/{most_last_thread['num']}.html"
        return {
            "id": most_last_thread['num'],
            "subject": most_last_thread.get('subject', 'Нет заголовка'),
            "posts_count": most_last_thread['posts_count'],
            "score": most_last_thread.get('score', 0),
            "comment": most_last_thread.get('comment', 'Нет комментария'),
            "link": thread_link
        }
    else:
        print(f"Ошибка: {response.status_code}")
        return None