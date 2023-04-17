# testing routine for List_Extraction function

import unittest
from src import functions
from models.heo import * 
import numpy as np

class list_extract_test(unittest.TestCase):

    def test_lists_lenght(self):
        """
        Test if it extracts the same list length for all targeted LP varaibles
        """

        dt = 1    # simulation time step dt.
        t_max = 10   # time span for simulation = t_max hours.
        t = np.atleast_2d(np.arange(0, t_max, dt)).T.conj()   # time scale in hours.
        n = len(t)  # number of time steps.
        V_steps = [x for x in range(0, n)]  # Time steps vector.

        functions.lixtr(
            )

        lenn_FC_ = len(FOC)
        lenn_P_ = len(P)
        lenn_P_load_ = len(P_load)
        lenn_P_to_bat_ = len(P_to_bat)
        lenn_P_From_bat_ = len(P_From_bat)
        lenn_Q_bat_ = len(Q_bat)
        lenn_Y_ = len(Y)
        lenn_Y_from_bat_ = len(Y_from_bat)
        lenn_Y_to_bat_ = len(Y_to_bat)
        lenn_Z_ = len(Z)+1

        # error message in case if test case got failed.
        message = "the extracted list doesn't fit the load frame"

        self.assertEqual(lenn_FC_, len(V_steps), message)
        self.assertEqual(lenn_P_, len(V_steps), message)
        self.assertEqual(lenn_P_load_, len(V_steps), message)
        self.assertEqual(lenn_P_to_bat_, len(V_steps), message)
        self.assertEqual(lenn_P_From_bat_, len(V_steps), message)
        self.assertEqual(lenn_Q_bat_, len(V_steps), message)
        self.assertEqual(lenn_Y_, len(V_steps), message)
        self.assertEqual(lenn_Y_from_bat_, len(V_steps), message)
        self.assertEqual(lenn_Y_to_bat_, len(V_steps), message)
        self.assertEqual(lenn_Z_, len(V_steps), message)


if __name__ == '__main__':
    unittest.main()
