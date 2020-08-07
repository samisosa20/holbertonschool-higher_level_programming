#!/usr/bin/python3
"""
The `State` class inherits from `Base`, an SQLAlchemy declarative base.
Instances of `State` will be a MySQL database.
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Creates the class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
