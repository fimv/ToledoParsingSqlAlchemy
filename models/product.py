import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from models.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(300))
    price = Column(Float)
    amount = Column(Integer)
    created = Column(DateTime(), default=datetime.datetime.now)
    group = Column(Integer, ForeignKey('groups.id'))

    def __repr__(self):
        return f'Продукт [ID: {self.id}, Название: {self.product_name}, Цена: {self.price}, Количество: {self.amount}]'
