# testing Load_window function 

import unittest

from Load_window import Load_window


class TestLoad(unittest.TestCase):

    def test_load_bounds(self):
        """
        Test that it makes the load frame along the 60 time steps
        """
        Loadframe = Load_window (200,200,10,400,400,10,600,600,10,600,200,30,0,10,20,30)
        sum = sum(Loadframe[k] for k in range(60))
        self.assertEqual(sum, 24000.0)

    def test_list_fraction(self):

        P_A_max = 1000
        """
        Test that it respects genset's low and max bounds 
        """
        Loadframe = Load_window (200,200,10,400,400,10,600,600,10,600,200,30,0,10,20,30)
        sum = sum(Loadframe[k] for k in range(60))
        Power_max_limit = P_A_max*60*0.9
        power_low_limit = 0

        if sum <= Power_max_limit and sum >= power_low_limit: 
            Power_check = 1

        self.assertEqual(Power_check, 1)

if __name__ == '__main__':
    unittest.main()