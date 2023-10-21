import sys
sys.path.append("../src")
from plot3  import execute 

import unittest

class TestPlot2(unittest.TestCase):
    def test_plot2(self):
        res = {'Sunrisers Hyderabad': 2, 'Rising Pune Supergiants': 1}
        self.assertEqual(execute(), res)