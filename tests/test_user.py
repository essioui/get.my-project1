#!/usr/bin/python3
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User

class Test(unittest.TestCase):
    def testCreate(self):
        user1 = User("salahsioui@thunder.net", "101010", "salah", "sioui")
        self.assertEqual(user1.email, "salahsioui@thunder.net")
        self.assertEqual(user1.password, "101010")
        self.assertEqual(user1.first_name, "salah")
        self.assertEqual(user1.last_name, "sioui")

    def test_id(self):
        User2 = User("salahsioui@thunder.net", "12345678", "salah", "sioui")
        User3= User("lionel_messi@gmail.arg", "123654", "lionel", "messi")
        self.assertNotEqual(User2, User3)

if __name__ == '__main__':
    unittest.main()
