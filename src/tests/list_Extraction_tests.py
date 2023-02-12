# testing routine for List_Extraction function

import unittest
from src import functions


class list_extract_test(unittest.TestCase):

    def test_lists_lenght(self):
        """
        Test if it extracts the same list length for all targeted LP varaibles
        """
        import numpy as np

        dt = 1    # simulation time step dt.
        t_max = 60   # time span for simulation = t_max hours.
        t = np.atleast_2d(np.arange(0, t_max, dt)).T.conj()   # time scale in hours.
        n = len(t)  # number of time steps.
        V_steps = [x for x in range(0, n)]  # Time steps vector.

        functions.list_extract(
            'FC_A_', 'P_A_', 'P_A_load_',
            'P_A_to_bat_', 'P_From_bat_',
            'Q_bat_', 'Y_', 'Y_from_bat_',
            'Y_to_bat_', 'Z_')

        lenn_FC_A_ = len('FC_A_')
        lenn_P_A_ = len('P_A_')
        lenn_P_A_load_ = len('P_A_load_')
        lenn_P_A_to_bat_ = len('P_A_to_bat_')
        lenn_P_From_bat_ = len('P_From_bat_')
        lenn_Q_bat_ = len('Q_bat_')
        lenn_Y_ = len('Y_')
        lenn_Y_from_bat_ = len('Y_from_bat_')
        lenn_Y_to_bat_ = len('Y_to_bat_')
        lenn_Z_ = len('Z_')

        # error message in case if test case got failed.
        message = "the extracted list doesn't fit the load frame"

        self.assertEqual(lenn_FC_A_, len(V_steps), message)
        self.assertEqual(lenn_P_A_, len(V_steps), message)
        self.assertEqual(lenn_P_A_load_, len(V_steps), message)
        self.assertEqual(lenn_P_A_to_bat_, len(V_steps), message)
        self.assertEqual(lenn_P_From_bat_, len(V_steps), message)
        self.assertEqual(lenn_Q_bat_, len(V_steps), message)
        self.assertEqual(lenn_Y_, len(V_steps), message)
        self.assertEqual(lenn_Y_from_bat_, len(V_steps), message)
        self.assertEqual(lenn_Y_to_bat_, len(V_steps), message)
        self.assertEqual(lenn_Z_, len(V_steps), message)


if __name__ == '__main__':
    unittest.main()
