#!/usr/bin/python3
"""python file that contains the class definition of a State
    and an instance Base"""

from mysqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    __table__ = "states"
    id = Column(Integer(), primary_key=True,
                autoincrement=True, unique=true, nullable=False)
    name = Column(String(128), nullable=False)
