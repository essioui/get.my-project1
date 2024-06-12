#!/usr/bin/python3

from baseModel import baseModel

class City(baseModel):

    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country
