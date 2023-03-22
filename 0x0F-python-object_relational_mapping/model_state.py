#!/usr/bin/python3
"""python file that contains the class definition of a State
    and an instance Base"""

from mysqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ Represents a state column for a MySQL table

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """

    __table__ = "states"
    id = Column(Integer(), primary_key=True,
                autoincrement=True, unique=true, nullable=False)
    name = Column(String(128), nullable=False)
