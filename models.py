from datetime import datetime

from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

quote_keyword = Table(
    "quote_keyword",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("quote_id", Integer, ForeignKey("quote.id")),
    Column("keyword_id", Integer, ForeignKey("keyword.id")),
)


class Author(Base):
    __tablename__ = "author"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('full_name', String(250), nullable=False)
    author_link = Column('author_link', String(150), nullable=False)
    created_at = Column('created at', DateTime, default=datetime.now())


class Quote(Base):
    __tablename__ = "quote"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(500), nullable=False, unique=True)
    author_id = Column('author_id', Integer, ForeignKey("author.id", ondelete="CASCADE"))
    created_at = Column('created at', DateTime, default=datetime.now())
    keywords = relationship("Keyword", secondary=quote_keyword)
    author = relationship("Author")


class Keyword(Base):
    __tablename__ = "keyword"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    keyword = Column('keyword', String(150), nullable=False, unique=True)
    created_at = Column('created at', DateTime, default=datetime.now())
    quotes = relationship("Quote", secondary=quote_keyword)
