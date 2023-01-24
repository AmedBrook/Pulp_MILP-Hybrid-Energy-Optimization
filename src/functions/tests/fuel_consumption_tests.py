# fuelcon testing routines

import unittest

from fuel_consumption import fuelCon


class TestfuelCon(unittest.TestCase):

    def test_max_consumption(self):
        """
        Test that it doesn't exceed the maximum fuel consumption allowed.
        """
        P_A_max = 1000
        maxcons = fuelCon (0.9*630, P_A_max) # Normally it should return 163800, 630 is a random power value
        
        self.assertEqual(maxcons, 163800.0) 

    def test_neg_value(self):

        """
        Test that it doesn't return a negative fuel consumption value.
        """
        P_A_max = 1000
        negcons = fuelCon((x for x in range(0,0.9*P_A_max)), P_A_max)
        if negcons >= 0: 
            res = 1
        else:
            res = 0 

        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()
