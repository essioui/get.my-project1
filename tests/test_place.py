#!/usr/bin/python3
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.place import Place
from models.user import User

class Test(unittest.TestCase):

    def testCreateCity(self):
        user = User("salah@mail.,net", "101010", "salah", "sioui")
        place = Place("Lake Zurich", "The Lake", "zurich city", "Zurich", "137.365", "174587", user, None, None, "200000", "80")
        self.assertEqual(place.name, "Lake Zurich")
        self.assertEqual(place.city, "Zurich")
        self.assertEqual(place.host, user)

    def test_add_amenity(self):
        place = Place("Lake Zurich", "The Lake", "zurich city", "Zurich", "137.365", "174587", "salah", None, None, "200000", "80")
        place.add_amenity("sky")
        self.assertIn("sky", place.amenities)

    def test_add_review(self):
        user = User("salah@mail.,net", "101010", "salah", "sioui")
        place = Place("Lake Zurich", "The Lake", "zurich city", "Zurich", "137.365", "174587", user, None, None, "200000", "80")
        review = {"text": "Lake Zurich", "rating": 8.9}
        place.add_review(review)
        self.assertIn(review, place.reviews)

if __name__ == '__main__':
    unittest.main()
