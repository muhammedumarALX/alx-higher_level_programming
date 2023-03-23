#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a;ll the table associated with the Base metadata
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all Stat objects from the database and order by states.id
    states = session.query(State).filter(State.name.like("%a%"))\
            .order_by(State.id).all()

    # print the State objects in the format specified
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
