#!/usr/bin/python3
"""
This module defines a class called DBStorage, which is responsible for
storing and retrieving data using an SQL database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.orm import scoped_session


class DBStorage():
    """
    This class is responsible for storing and retrieving data using
    an SQL database. It includes methods for creating a new object,
    saving objects to the database, deleting objects from the database,
    and loading all tables in the database. The all() method returns a
    dictionary of all objects in the database, or a dictionary of
    objects of a specified class. The class takes its database
    connection parameters from environment variables set in the
    operating system."""
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the SQL database storage by creating an engine object
        with the given parameters and starting a session with the database.
        """
        from models.base_model import Base

        db_user = os.environ.get('HBNB_MYSQL_USER')
        db_password = os.environ.get('HBNB_MYSQL_PWD')
        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db_name = os.environ.get('HBNB_MYSQL_DB')
        mode = os.environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(db_user,
                                             db_password, db_host,
                                             db_name), pool_pre_ping=True)
        if (mode == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects in the database,
        or a dictionary of objects of a specified class.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from console import HBNBCommand

        object_dict = {}
        if cls is None:
            for key in HBNBCommand.classes:
                if key != "BaseModel":
                    val = HBNBCommand.classes[key]
                    for row in self.__session.query(val).all():
                        object_dict.update({'{}.{}'.format(key, row.id): row})
            return object_dict
        else:
            if cls is not BaseModel:
                for row in self.__session.query(cls).all():
                    object_dict.update({'{}.{}'.format(cls, row.id): row})
            return object_dict

    def new(self, obj):
        """
        Adds a new object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session.
        """
        if not obj:
            return
        # key = str(obj.__class__.__name__)
        self.__session.delete(obj)
        # search = self.__session.query(key)
        # for data in search:
        #    if obj is data:
        #        self.__session.delete(data)

    def reload(self):
        """
        Creates all tables in the database and starts a new
        session with the database.
        """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()

    def close(self):
        """
        Closes the current database session and disposes of the
        database engine.
        """
        self.__session.close()
        self.__engine.dispose()
