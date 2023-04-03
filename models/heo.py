
'''
Mixed integer energy hybridization problem solved
with Pulp script to optimize fuel oil consumption

'''
# Importing libraries.
import numpy as np
from pulp import *

# Defining set of parameters
Q_max = 250
Q_0 = 0.5*Q_max
Q_final = 0.5*Q_max
eff_to_bat = 0.98
eff_from_bat = 0.98
P_max = 1000
P_min = 0
dt = 1
t_max = 10
t = np.atleast_2d(np.arange(0, t_max, dt)).T.conj()
n = len(t)
m = 1
fc_offset = 190
V_steps = [x for x in range(0, n)]
V_steps_z = V_steps[:-1]


# creating load window function.
def lwd(
 val11, val12, val13,
 val21, val22, val23,
 val31, val32, val33,
 val41, val42, val43,
 L1, L2, L3, L4):

    L = {}

    E1 = np.atleast_2d(np.linspace(val11, val12, val13)).T.conj()
    E2 = np.atleast_2d(np.linspace(val21, val22, val23)).T.conj()
    E3 = np.atleast_2d(np.linspace(val31, val32, val33)).T.conj()
    E4 = np.atleast_2d(np.linspace(val41, val42, val43)).T.conj()

    L1 = dict(enumerate(E1.flatten(), L1))
    L2 = dict(enumerate(E2.flatten(), L2))
    L3 = dict(enumerate(E3.flatten(), L3))
    L4 = dict(enumerate(E4.flatten(), L4))
    L = {**L1, **L2, **L3, **L4}
    return L


L = lwd(200, 50, 5,
        50, 300, 5,
        200, 150, 10,
        150, 250, 30,
        0, 5, 20, 30)


# creating fuelCon function.
def fuelCon(P, P_max):

    fc = {}
    fc = 260 * P - 67 / P_max * P**2
    return fc


# Creating optimization problem variable.
Optim = LpProblem('Energy_Opt', LpMinimize)


# calculating the slope and intercept for the problem.
a_j = (fuelCon(0.9 * P_max, P_max) - fuelCon(0.2 * P_max, P_max)) / (0.9 * P_max)  # slope.
b_j = fuelCon(0.2*P_max, P_max) - a_j*0.2*P_max  # Intercept.
maxFC = fuelCon(0.9*P_max, P_max)  # Max fuel bound.


# setting up the LP variables.
Q_bat = pulp.LpVariable.dicts("Q_bat", V_steps, lowBound=0.2 * Q_max, upBound=Q_max, cat=LpContinuous)
P_From_bat = pulp.LpVariable.dicts("P_From_bat", V_steps, lowBound=P_min, upBound=0.9 * P_max, cat=LpContinuous)
P = pulp.LpVariable.dicts("P", V_steps, lowBound=P_min, upBound=0.9 * P_max, cat=LpContinuous)
P_load = pulp.LpVariable.dicts("P_load", V_steps, lowBound=P_min, upBound=0.9 * P_max, cat=LpContinuous)
Z = pulp.LpVariable.dicts("Z", V_steps_z, lowBound=0, upBound=1, cat=LpInteger)
FOC = pulp.LpVariable.dicts("FOC", V_steps, lowBound=0, upBound=maxFC, cat=LpContinuous)
P_to_bat = pulp.LpVariable.dicts("P_to_bat", V_steps, lowBound=P_min, upBound=0.9*P_max, cat=LpContinuous)
Y_to_bat = pulp.LpVariable.dicts("Y_to_bat", V_steps, lowBound=0, upBound=1, cat=LpInteger)
Y_from_bat = pulp.LpVariable.dicts("Y_from_bat", V_steps, lowBound=0, upBound=1, cat=LpInteger)
Y = pulp.LpVariable.dicts("Y", V_steps, lowBound=0, upBound=1, cat=LpInteger)


# Setting up the objectif function.
FC = sum(FOC[k] for k in V_steps) * dt/1000  # sum of the fuel oil comsumption for all gensets over all k steps.
L_added_cost = sum(Z[i] for i in V_steps_z)  # Sum of all of the additional costs including starting costs.
Optim += lpSum(FC + L_added_cost), "Minimization fuel oil consumption objective"
print(FC)


# Setting up problem constraints.
for k in V_steps:

    # Fuel oil consumption constraint.
    Optim += FOC[k] == P[k]*a_j + b_j - fc_offset*Y[k]

    # Load requirements constraints
    Optim += P_load[k] + eff_from_bat*P_From_bat[k] == L[k]
    Optim += P_load[k] + P_to_bat[k] == P[k]

    # Genset logical constraints.
    Optim += P[k] <= 0.9 * P_max * Y[k]
    Optim += P[k] >= 0.2 * P_max * Y[k]

    # Battery charging logical constraints.
    Optim += P_to_bat[k] <= 0.9 * P_max * Y_to_bat[k]
    Optim += P_From_bat[k] <= 0.9 * P_max * Y_from_bat[k]
    Optim += Y_to_bat[k] + Y_from_bat[k] <= 1

    # Charge balance logical constraints.
    if k == V_steps[0]:
        Optim += Q_bat[k] == Q_0 + eff_to_bat*P_to_bat[k]*dt - P_From_bat[k]*dt

    else:
        Optim += Q_bat[k] == Q_bat[k-1] + eff_to_bat*P_to_bat[k]*dt - P_From_bat[k]*dt

# Additional starting costs constraint.
for k in range(V_steps[0], V_steps[-1]):
    Optim += Z[k] >= Y[k + 1] - Y[k]

# Charge balance at the Final time step.
Optim += Q_bat[V_steps[-1]] == Q_final


# Solving the prblem using Gurobi solver.
status = Optim.solve(GUROBI())


# Printing the LP optimal values.
for v in Optim.variables():
    print(v.name, "=", v.varValue)


# Printing total ptimized fuel oil consuption.
print("Total fuel comsumption of the trip:", value(Optim.objective), 'g')
