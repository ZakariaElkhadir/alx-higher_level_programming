#!/use/bin/python3
"""
database module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """represents a state for mysql database"""
    tablename = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
