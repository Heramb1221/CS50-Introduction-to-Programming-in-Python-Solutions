import unittest
from seasons import get_date

class TestDate(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(get_date(), "1999-01-01")
