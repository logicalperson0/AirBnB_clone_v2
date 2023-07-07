#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    if storage_type == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""


    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
