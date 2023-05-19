import json
import sqlalchemy
import sys
import os
from sqlalchemy.orm import sessionmaker
import pprint

from models import create_tables, Publisher,Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:3543@localhost:5432/azoxe_orm'           #строка подключения к источнику данных
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as data_file:
    data = json.load(data_file)
for i in data:
    model = {
        'publisher': Publisher,
        'book': Book,
        'shop': Shop,
        'stock': Stock,
        'sale': Sale,
    }[i.get('model')]
    session.add(model(id=i.get('pk'), **i.get('fields')))
session.commit()

def get_info(author):
    info = session.query(Book.title, Shop.name, Stock.count, Sale.date_sale).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    f = info.filter(Publisher.name == author).all()
    for b, s, st, sa in f:
        print(b, s, st, sa)

get_info("Pearson")

session.close()


