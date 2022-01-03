from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_NAME = 'postgresql://postgres:mike@localhost:5432/toledo'
engine = create_engine(DATABASE_NAME)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def create_db():
    print('Формируется схема базы данных...')
    Base.metadata.create_all(engine)
