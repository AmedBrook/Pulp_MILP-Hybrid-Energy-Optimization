# Objective function testing routine

import unittest
from models.heo import *
from models.heo import FOC


class Test_Objective(unittest.TestCase):

    def test_obj_values(self):
        """
        Test if the Objective function returns the sum of the fuel oil consumption
        values over time steps with a tolerance of 3g difference at most.

        """
        delta = 3
        self.assertAlmostEqual(value(Optim.objective), value(sum(FOC.values())/10**3),
                               msg='Total time steps fuel oil consmuption is not matching the objective function!',
                               delta=delta)


if __name__ == '__main__':
    unittest.main()
