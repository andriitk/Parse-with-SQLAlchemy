from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool
from models import Author, Quote, Keyword, quote_keyword, Base

engine = create_engine("sqlite:///my_spider_data.db", echo=True, poolclass=SingletonThreadPool)

Base.metadata.bind = engine
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_authors_table(data: list):
    for el in data:
        author = Author(
            name=el.get('author'),
            author_link=el.get('author_link')
        )
        session.add(author)
    session.commit()


def create_quotes_table(data: list):
    authors = session.query(Author.id).all()

    for el, author_id in zip(data, authors):
        quote = Quote(
            title=el.get('quote'),
            author_id=author_id.id
        )
        session.add(quote)
    session.commit()


def create_keywords_table(data: list):
    kws = set()
    for el in data:
        for _i in el.get('tagsforquote'):
            if _i not in kws:
                kws.add(_i)
                keyword = Keyword(
                    keyword=_i
                )
                session.add(keyword)
        session.commit()


def create_relationship_table(data):
    keywords = session.query(Keyword).all()
    quotes = session.query(Quote).all()

    for el, quote in zip(data, quotes):
        keywords_data = el.get('tagsforquote')
        for i in keywords:
            if i.keyword in keywords_data:
                quote.keywords.append(i)
                session.add(quote)
    session.commit()
