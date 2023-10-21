"""importing the module"""
import unittest
import sys
sys.path.append("../src")
from match_per_year  import execute
class TestMatchesPerYearFunctions(unittest.TestCase):
    def test_matches_per_year(self):
        self.assertEqual(execute(), {2017 : 3, 2009 :1, 2010 : 2 , 2016 :1 , 2015 : 2})


if __name__ == '__main__':
    unittest.main()
