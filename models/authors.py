from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Authors(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    birthdate = Column(Date)
    nationality = Column(String)