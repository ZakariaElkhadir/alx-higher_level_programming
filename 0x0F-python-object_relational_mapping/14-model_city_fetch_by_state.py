#!/usr/bin/python3
"""
database module
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states = session.query(State, City).join(
        City, State.id == City.state_id).order_by(City.id)

    for state, city in cities_states:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
