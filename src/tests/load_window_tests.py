# testing Load_window function

import unittest
from src import functions


class TestLoad(unittest.TestCase):

    def test_load_frame(self):
        """
        Test that it makes the load frame along the 60 time steps
        """
        Loadframe = functions.Load_window(

         200, 200, 10,
         400, 400, 10,
         600, 600, 10,
         600, 200, 30,
         0, 10, 20, 30
         )

        res = sum(Loadframe[k] for k in range(60))
        self.assertEqual(res, 24000.0)

    def test_load_bounds(self):

        P_A_max = 1000
        """
        Test that it respects genset's low and max bounds
        """
        Loadframe = functions.Load_window(

         200, 200, 10,
         400, 400, 10,
         600, 600, 10,
         600, 200, 30,
         0, 10, 20, 30)

        res = sum(Loadframe[k] for k in range(60))
        Power_max_limit = P_A_max*60*0.9
        power_low_limit = 0

        if res <= Power_max_limit and res >= power_low_limit:
            Power_check = 1

        self.assertEqual(Power_check, 1)


if __name__ == '__main__':
    unittest.main()
