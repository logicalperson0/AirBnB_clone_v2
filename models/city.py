#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        if storage_type == 'db':
            __tablename__ = 'cities'
            #if storage_type == 'db':
            name = Column(String(128), nullable=False)
            state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
            places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
        else:
             state_id = ""
             name = ""

        def __init__(self, *args, **kwargs):
            """initializes city"""
            super().__init__(*args, **kwargs)
