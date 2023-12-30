from sqlalchemy import Column, Integer, String, Text, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    price = Column(Float)
    publication_date = Column(Date)
    author = relationship("Authors")