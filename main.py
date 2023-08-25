from bs4 import BeautifulSoup
import requests


def main():
    list_with_traks = list()
    list_with_time = list()
    url = 'https://music.yandex.ru/artist/5313769/tracks'
    responce = requests.get(url)
    bs = BeautifulSoup(responce.text, "lxml")
    count = 0
    for item in bs.find_all('a', 'd-track__title deco-link deco-link_stronger'):
        temp = item.text
        temp = temp.lstrip().rstrip()
        list_with_traks.append(temp)
    for time in bs.find_all('span', 'typo-track deco-typo-secondary'):
        list_with_time.append(time.text)
    total_list = [(track, time) for track, time in zip(list_with_traks, list_with_time)]
    print(total_list)
    print()


if __name__ == "__main__":
    main()
