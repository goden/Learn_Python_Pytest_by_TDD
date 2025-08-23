from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Board(Base):
    __tablename__ = 'board'
    id:int = Column(Integer, primary_key=True, autoincrement=True)
    name:str = Column(String(64), nullable=False)
    create_time:datetime = Column(DateTime)