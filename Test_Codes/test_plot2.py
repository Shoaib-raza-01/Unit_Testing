import sys
sys.path.append("../src")
from plot2  import execute 

import unittest

class TestPlot2(unittest.TestCase):
    def test_plot2(self):
        res = {2017: {'Kings XI Punjab': 1, 'Gujarat Lions': 1, 'Kolkata Knight Riders': 1}, 2009: {'Deccan Chargers': 1}, 2010: {'Chennai Super Kings': 1, 'Kings XI Punjab': 1}, 2016: {'Rising Pune Supergiants': 1}, 2015: {'Rajasthan Royals': 1, 'Delhi Daredevils': 1}}
        self.assertEqual(execute(), res)