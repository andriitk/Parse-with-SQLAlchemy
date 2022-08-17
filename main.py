import requests
from bs4 import BeautifulSoup
from db import create_authors_table, create_quotes_table, create_keywords_table, create_relationship_table


def parse_data():
    data_store = []
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')

        abouts = []
        for about in soup.find_all('a'):
            author_link = about.get('href')
            if '/author' in about.get('href'):
                abouts.append(author_link)

        for i in range(0, len(quotes)):
            quote = quotes[i].text[1:-1].strip()
            author = authors[i].text
            author_link = f'{url[:-1]}{abouts[i]}'
            tagsforquote = tags[i].find_all('a', class_='tag')

            tags_author = []
            for tag in tagsforquote:
                tags_author.append(tag.text)

            data_store.append({
                'quote': quote,
                'author': author,
                'author_link': author_link,
                'tagsforquote': tags_author
            })
        return data_store


if __name__ == '__main__':
    data = parse_data()
    create_authors_table(data)
    create_quotes_table(data)
    create_relationship_table(data)
    create_keywords_table(data)
