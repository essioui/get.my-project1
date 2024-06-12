#!/usr/bin/python3

from baseModel import baseModel

class Review(baseModel):
    def __init__(self, user, place, rating, text):
        super().__init__()
        self.user = user
        self.place = place
        self.rating = rating
        self.text = text
