# fuelcon testing routines

import unittest
from src.functions import fuel_consumption


class TestfuelCon(unittest.TestCase):

    def test_max_consumption(self):
        """
        Test if it doesn't exceed the maximum fuel consumption allowed.
        """
        # Normally it should return 125880.237, 630 is a random power value
        P_A_max = 1000
        maxcons = fuel_consumption.fuelCon(0.9*630, P_A_max)

        self.assertEqual(maxcons, 125880.237)

    def test_neg_value(self):

        """
        Test if it doesn't return a negative fuel consumption value.
        """
        P_A_max = 1000
        negcons = fuel_consumption.fuelCon((0.9*P_A_max), P_A_max)
        if negcons >= 0:
            res = 1
        else:
            res = 0

        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
