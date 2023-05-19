import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique = True)
    
    def __str__(self):
        return f'publisher {self.id}: {self.name}'
    
        
class Book(Base):
    __tablename__ = "book"
    
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique = True)
    publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    
    Publisher = relationship(Publisher,backref = "Book")
    
    def __str__(self):
        return f'book {self.id}: ({self.title}, {self.id_publisher})'
    
class Shop(Base):
    __tablename__ = "shop"
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique = True)
    
    def __str__(self):
        return f'shop {self.id}: {self.name}'
    
class Stock(Base):
    __tablename__ = "stock"
    
    id = sq.Column(sq.Integer, primary_key=True)
    book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    
    Shop = relationship(Shop,backref = "Stock")
    # Book = relationship(Book,backref = "Stock")
    
    def __str__(self):
        return f'stock {self.id}: ({self.id_book}, {self.id_shop}, {self.count})'
    
class Sale(Base):
    __tablename__ = "sale"
    
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.DECIMAL(10,2), nullable=False)
    date_sale = sq.Column(sq.Date)
    stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    
    Stock = relationship(Stock,backref = "Sale")
    
    def __str__(self):
        return f'sale {self.id}: ({self.price}, {self.date_sale}, {self.id_stock}, {self.count})'    
    
def create_tables(engine):
    Base.metadata.drop_all(engine)       
    Base.metadata.create_all(engine)    