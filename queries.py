from sqlalchemy.orm import joinedload, join, outerjoin
from sqlalchemy import text
from db import session
from models import Author, Quote, Keyword


def get_author_with_quote():
    quotes = session.query(Quote).options(joinedload('author')).all()
    for q in quotes:
        print('-----------------------------------')
        print(f"[QUOTE] {q.title}")
        print(f"[AUTHOR NAME] {q.author.name}")
    print("-------------------------------------")


def get_quote_with_author():
    authors = session.query(Author).options(joinedload('quote')).all()
    for a in authors:
        print('-----------------------------------')
        print(f"[AUTHOR NAME] {a.name}")
        for _i, q in enumerate(a.quote, start=1):
            print(f"{_i}. [QUOTE] {q.title}")
    print("-------------------------------------")


def get_quotes_with_keyword():
    keywords = session.query(Keyword).options(joinedload('quotes')).all()
    for k in keywords:
        print(f"[KEYWORD] {k.keyword}")
        for _i, a in enumerate(k.quotes, start=1):
            print(f"{_i}. {a.title}")
        print("-------------------------------------")


def get_keywords_with_quote():
    quotes = session.query(Quote).options(joinedload('keywords')).all()
    for q in quotes:
        print(f"[QUOTE] {q.title}")
        for _i, a in enumerate(q.keywords, start=1):
            print(f"{_i}. {a.keyword}")
        print("-------------------------------------")


def get_quotes_with_one_keyword():
    keywords = session.query(Keyword).options(joinedload('quotes')).filter(text('keyword = :keyword')).params(
        keyword='humor')
    print('-------------------------------')
    for k in keywords:
        print(f"[KEYWORD] {k.keyword}")
        for _i, a in enumerate(k.quotes, start=1):
            print(f"{_i}. {a.title}")
        print("-------------------------------------")


if __name__ == '__main__':
    # get_author_with_quote()
    # get_quote_with_author()
    # get_quotes_with_keyword()
    # get_keywords_with_quote()
    get_quotes_with_one_keyword()
