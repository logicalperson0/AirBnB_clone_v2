#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
#from sqlalchemy.ext.declarative import declarative_base

class State(BaseModel, Base):
    """ State class/ table model """
    if storage_type == 'db':
        __tablename__ = 'states'
        #if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                            backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if storage_type != 'db':
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
