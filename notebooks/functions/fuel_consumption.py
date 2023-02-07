
# Some parameters to define fuelCon function.

import numpy as np
P_A_max = 1000  # max output from gen set A.
dt = 2/3  # simulation time step dt.
t_max = 5  # time span for simulation = t_max hours.
t = np.atleast_2d(np.arange(2, t_max, dt)).T.conj()    # time scale in hours.
n = len(t)  # number of time steps.
V_steps = [x for x in range(2, n)]  # Time steps vector.
V_steps_z = V_steps[:-1]  # Time steps vector without the final step.

# fuel consumption function.


def fuelCon(P_A, P_A_max):

    fc = {}
    fc = 260 * P_A - 67 / P_A_max * P_A**2
    return fc
