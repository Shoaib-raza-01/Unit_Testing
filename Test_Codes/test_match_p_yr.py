# from ..src import match_per_year
# from UNIT_TESTING.src import match_per_year
import sys
sys.path.append("../src")
from match_per_year  import execute 
import unittest

class TestMatchesPerYearFunctions(unittest.TestCase):
    def test_matches_per_year(self):
        self.assertEqual(execute(), {2017 : 3, 2009 :1, 2010 : 2 , 2016 :1 , 2015 : 2})


if __name__ == '__main__':
    unittest.main()