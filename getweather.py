import requests


CITIES = [
    'Лондон',
    'svo',
    'Череповец'
]


PARAMS = {
    'MnqT': '',
    'lang': 'ru'
}


def request_weather(city):
    url = f'http://wttr.in/{city}'
    response = requests.get(url, PARAMS)
    response.raise_for_status()
    return response.text


def main():
    for city in CITIES:
        try:
            forecast = request_weather(city)
        except requests.exceptions.ConnectionError:
            forecast = 'нет сети'
        print(forecast)


if __name__ == '__main__':
    main()
