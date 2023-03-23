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
    state_delete = session.query(State).filter(State.name.like("%a%")).all()

    # delete
    session.delete(state_delete)

    # commit changes
    session.commit()

    # close the session
    session.close()
