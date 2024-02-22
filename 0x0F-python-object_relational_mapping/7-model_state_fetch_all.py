#!/usr/bin/python3
"""
database module
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all()
for state in states:
    print(f"{state.id}: {state.name}")
session.close()

