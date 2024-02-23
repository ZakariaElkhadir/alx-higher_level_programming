#!/usr/bin/python3
"""
database model
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_update = session.query(State).filter(
        State.name == 'Louisiana').order_by(State.id == 2).first()

    if states_update:
        states_update.name = 'New Mexico'
        session.commit()
    session.close()
