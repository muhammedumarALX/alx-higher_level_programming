#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a;ll the table associated with the Base metadata
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all Stat objects from the database
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print cties
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # close the session
    session.close()
