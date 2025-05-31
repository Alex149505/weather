import requests


def create_forcast():
    cities = (
        'Лондон',
        'svo',
        'Череповец'
    )
    url_template = 'http://wttr.in/{}?MnqT&lang=ru'
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url)
        print(response.text)


def main():
    create_forcast()


if __name__ == '__main__':
    main()
