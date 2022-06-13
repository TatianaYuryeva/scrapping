import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


HEADERS = Headers().generate()
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'php', 'алгоритмы', 'android', 'игры']


def search_matching():
    base_url = 'https://habr.com'
    url = 'https://habr.com/ru/all/'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='tm-articles-list__item')
    for article in articles:
        matching = set(article.text.lower().split(" ")).intersection(set(KEYWORDS))
        if len(matching) > 0:
            article_date = article.find('time').text
            article_header = article.find('h2').text
            article_link = base_url + (article.find('a', class_='tm-article-snippet__title-link')).attrs.get('href')
            print(*matching)
            print(f'<{article_date}> - <{article_header}> - <{article_link}>')


if __name__ == '__main__':
    search_matching()
