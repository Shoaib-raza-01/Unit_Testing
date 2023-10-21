import sys
sys.path.append("../src")
from plot4  import execute 

import unittest

class TestPlot2(unittest.TestCase):
    def test_plot2(self):
        res = {'TG Southee': {'total': 6, 'over': 3, 'economy': 2.0}, 'CH Morris': {'total': 2, 'over': 3, 'economy': 0.67}, 'DJ Hooda': {'total': 1, 'over': 1, 'economy': 1.0}, 'P Kumar': {'total': 2, 'over': 3, 'economy': 0.67}, 'DW Steyn': {'total': 0, 'over': 2, 'economy': 0.0}, 'RS Bopara': {'total': 7, 'over': 6, 'economy': 1.17}}
        self.assertEqual(execute(), res)