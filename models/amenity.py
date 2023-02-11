#!/usr/bin/env python

from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ''
    
    def __init__(self, *args, **kwargs):
        """ Initialize user """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
