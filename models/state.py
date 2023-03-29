#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
from os import environ


class State(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if (environ.get("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """ getter method for cities"""
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
