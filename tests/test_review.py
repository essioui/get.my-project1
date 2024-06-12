#!/usr/bin/python3
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.review import Review
from models.user import User
from models.place import Place

class Test(unittest.TestCase):
    def testReview(self):
        user = User("salah@mail.,net", "101010", "salah", "sioui")
        place = Place("Lake Zurich", "The Lake", "zurich city", "Zurich", "137.365", "174587", "21354", None, None, "200000", "80")
        review = Review(user, place, 8.9, "beauty")
        self.assertEqual(review.user, user)
        self.assertEqual(review.place, place)
        self.assertEqual(review.rating, 8.9)
        self.assertEqual(review.text, "beauty")
        

if __name__ == '__main__':
    unittest.main()
    