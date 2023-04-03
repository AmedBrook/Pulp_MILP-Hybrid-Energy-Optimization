
'''
Mixed integer energy hybridization problem solved
with Pulp script to optimize fuel oil consumption

'''
# IMPORTING LIBRARIES.
import numpy as np
from pulp import *
from src.functions.load_window import lwd
from src.functions.fuel_consumption import fuelCon

# DEFINING SET OF PARAMETERS.
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

# CONSTRUCTING LOAD PROFILE.
L = lwd(200, 50, 5,
        50, 300, 5,
        200, 150, 10,
        150, 250, 30,
        0, 5, 20, 30)


# CREATING OPTIMIZATION PROBLEM VARIABLE.
Optim = LpProblem('Energy_Opt', LpMinimize)


# CALCULATING THE SLOPE AND INTERCEPT FOR THE PROBLEM.
a_j = (fuelCon(0.9 * P_max, P_max) - fuelCon(0.2 * P_max, P_max)) / (0.9 * P_max)  # slope.
b_j = fuelCon(0.2*P_max, P_max) - a_j*0.2*P_max  # Intercept.
maxFC = fuelCon(0.9*P_max, P_max)  # Max fuel bound.


# SETTING UP THE LP VARIABLES.
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


# SETTING UP THE OBJECTIF FUNCTION.
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

# ADDITIONAL STARTING COSTS CONSTRAINT.
for k in range(V_steps[0], V_steps[-1]):
    Optim += Z[k] >= Y[k + 1] - Y[k]

# CHARGE BALANCE AT THE FINAL TIME STEP.
Optim += Q_bat[V_steps[-1]] == Q_final


# SOLVING THE PRBLEM USING GUROBI SOLVER.
status = Optim.solve(GUROBI())


# PRINTING THE LP OPTIMAL VALUES.
for v in Optim.variables():
    print(v.name, "=", v.varValue)


# PRINTING TOTAL PTIMIZED FUEL OIL CONSUPTION.
print("Total fuel comsumption of the trip:", value(Optim.objective), 'g')
