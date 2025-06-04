import requests


CITIES = [
    'Лондон',
    'svo',
    'Череповец'
]


def make_url(city):
    return F'http://wttr.in/{city}'


def make_parameters():
    params = {
        '?MnqT': '',
        'lang': 'ru'
    }
    return params


def fetch_weather(city):
    try:
        request = requests.get(make_url(city), params=make_parameters())
        if request.status_code == 200:
            return request.text
        else:
            return 'ошибка на сервере'
    except requests.ConnectionError:
        return 'нет сети'


def main():
    for city in CITIES:
        print(fetch_weather(city))


if __name__ == '__main__':
    main()
