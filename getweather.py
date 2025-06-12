import requests


CITIES = [
    'Лондон',
    'svo',
    'Череповец'
]


def request_weather(city):
    url = f'http://wttr.in/{city}'
    response = requests.get(url, params)
    response.raise_for_status()
    if response.ok:
        return response.text


def main():
    global params
    params = {
        'MnqT': '',
        'lang': 'ru'
    }
    for city in CITIES:
        try:
            forecast = request_weather(city)
        except requests.HTTPError:
            forecast = 'Вы ввели неправильную ссылку или неверный токен.'
        print(forecast)


if __name__ == '__main__':
    main()
