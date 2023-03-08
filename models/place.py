#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from os import getenv
from models.amenity import Amenity
from models.review import Review
=======
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import environ
>>>>>>> d516bb6042f1e4a01efc9a7747aef8c7c900617f

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))

<<<<<<< HEAD
association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
=======

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
>>>>>>> d516bb6042f1e4a01efc9a7747aef8c7c900617f
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
<<<<<<< HEAD
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=True)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def reviews(self):
            """Get a list of all Reviews"""
            reviewlist = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviewlist.append(review)
            return reviewlist

        @property
        def amenities(self):
            """ Get Linked Amenities"""
            amenitylist = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenitylist.append(amenity)
            return amenitylist

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
=======
    amenity_ids = []

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", backref="place_amenities",
                                 secondary=place_amenity, viewonly=False)

    else:
        @ property
        def reviews(self):
            """ getter method for reviews"""
            reviews_list = []
            reviews = models.storage.all(Reviews)
            for review in reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @ property
        def amenities(self):
            """ getter method for amenities"""
            amenities_list = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @ amenities.setter
        def amenities(self, object=None):
            """ setter method for amenities"""
            if type(object).__name__ == "Amenity":
                self.amenity_ids.append(object)
>>>>>>> d516bb6042f1e4a01efc9a7747aef8c7c900617f
