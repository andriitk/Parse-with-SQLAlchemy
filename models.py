from datetime import datetime

from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

quotes_m2m_keywords = Table(
    "quotes_m2m_keywords",
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("quote", Integer, ForeignKey("quotes.id")),
    Column("keyword", Integer, ForeignKey("keywords.id")),
)


class Authors(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    quote = relationship("Quotes", cascade="all, delete", backref="authors")
    keywords = relationship("Keywords", secondary=quotes_m2m_keywords, backref="authors")
    author_link = Column(String(150), nullable=False)
    created = Column(DateTime, default=datetime.now())


class Quotes(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False, unique=True)
    author_id = Column(Integer, ForeignKey(Authors.id, ondelete="CASCADE"))
    created = Column(DateTime, default=datetime.now())


class Keywords(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(String(150), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.now())
