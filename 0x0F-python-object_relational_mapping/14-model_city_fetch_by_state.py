#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a;ll the table associated with the Base metadata
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all Stat objects from the database
    query = session.query(City, State)
    states = query.filter(City.state_id == State.id).order_by(City.id).all()

    # Print cties
    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close the session
    session.close()
