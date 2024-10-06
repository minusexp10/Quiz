import requests


def data(category):
    category_key = {
        'General Knowledge': 9,
        'Science: Computers': 18,
        'Science & Nature': 17,
        'Entertainment: Cartoon & Animations': 17,
        'Entertainment: Video Games': 15,
        'Entertainment: Japanese Anime and Manga': 31,
        'Mythology': 20,
        'Politics': 24
    }

    response = requests.get(url=f'https://opentdb.com/api.php?amount=10&category={category_key[category]}&type=boolean')
    response.raise_for_status()
    return response.json()['results']
