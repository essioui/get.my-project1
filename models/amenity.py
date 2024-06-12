#!/usr/bin/python3

from baseModel import baseModel

class Amenity(baseModel):

    def __init__(self, name):
        super().__init__()
        self.name =name
