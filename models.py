from sqlalchemy import Column, Integer,\
    String, Text, text, create_engine,\
        DATETIME, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime

DATABASE = 'postgresql'
USER     = 'book_userY'
PASSWORD = 'ryu0110'
HOST     = 'localhost'
PORT     = '5432'
DB_NAME  = 'book_data'

URL = '{}://{}:{}@{}:{}/{}'.format(DATABASE,\
    USER, PASSWORD, HOST, PORT, DB_NAME)
engin = create_engine(URL, echo=True)

Base = declarative_base()
Connection = sessionmaker(bind=engin)
connection = Connection()

class Books(Base):
    __tablename__ = "books"
    id_ = Column('id', Integer, primary_key = True)
    name = Column('name', String(255))
    volume = Column('volume', String(255))
    author = Column('author', String(255))
    publisher = Column('publisher', String(255))
    memo = Column('memo', Text())
    create_date = Column('create_date',\
        DateTime(timezone=True), default=func.now(), nullable=False)
    delFlg = Column('del', Boolean)
    
class BookUser(Base):
    __tablename__ = "book_user"
    user_id = Column('user_id', String(255), primary_key = True)
    passwd = Column('passwd', String(255), nullable=False)
    email = Column('email', String(255), nullable=False)
    user_shi = Column('user_shi', String(255))
    user_mei = Column('user_mei', String(255))
    delFlg = Column('del', Boolean)

if __name__ == "__main__":
    Base.metadata.create_all(engin)