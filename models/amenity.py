#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
>>>>>>> d516bb6042f1e4a01efc9a7747aef8c7c900617f
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """ Amenity: Class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)

    def __init__(self, *args, **kwargs):
        """
            Init for inherited
        """
        super().__init__(*args, **kwargs)
=======
    """ The Amenity class, contains state ID and name """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
>>>>>>> d516bb6042f1e4a01efc9a7747aef8c7c900617f
