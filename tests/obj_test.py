# Objective function testing routine

import unittest
from models.heo import *
from models.heo import FOC


class Test_Objective(unittest.TestCase):

    def test_FOC_value(self):
        """
        Test if the Objective function returns the summ of
        the fuel oil consumption values over time steps.
        """
        delta = 3
        self.assertAlmostEqual(value(Optim.objective), value(sum(FOC.values())/1000),
                               msg='Time steps Fuel oil consmuption is not matching the objective function!',
                               delta= delta)
        
if __name__ == '__main__':
    unittest.main()

