#!/usr/bin/python3

from baseModel import baseModel

class Country(baseModel):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)
