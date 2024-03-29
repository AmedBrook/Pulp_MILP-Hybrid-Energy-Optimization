## User quick guide.
---

### Optimization variable. 

The optimization variable is the variable that will host problem solving results, it is created via the command ```LpProblem()```. Inside the parenthesis we can assign a name for the optimization problem beeing solved as well as defining which type the problem is. whether is a maximization or minmization ('LpMaximize' for maximization or 'LpMinimize' for minimization problem). 

In our case it is Minimization problem, therfore to create our optimization problem variable we can do something like : 

```python 
 Optim = LpProblem('Energy_Opt',LpMinimize)
```

$\newline$ 
### Decision variables. 


###### LpVariable(). 
Creating decsion variables is easy as using the command ```LpVariable()```, inside the parenthesis we can give it a name, and setting the variable min and max bounds admissible for that paticular decision variable.
note : it's important to set carfully the bounds otherwise it can easily leads to an infeasable problem within the solving process.  


###### LpVariable.dicts().
In our case, each decision variable is descritisized depending to load window vector steps, they will contain as much points as the number of steps : dem(LpVaraible) = dem(V_steps). Based on this approach it's convinent to set our decision variable points as key-values pair in a dictionnary. To create a dictionary decision variable we use the command ``LpVariable.dicts()``, inside the parenthesise we can define the LpVariable lower and upper bounds type using ``LowBound`` and ``upBound``, the ``cat`` argument can be used to define the LpVariable type as well. 

Our 10 decision varaibles then are set up as following: 

```
Q_bat = LpVariable.dicts("Q_bat", V_steps, lowBound=0.2*Q_max, upBound=Q_max, cat=LpContinuous)  # Battery charge at time step k.
P_From_bat = LpVariable.dicts("P_From_bat", V_steps, lowBound=0, upBound=0.9*P_A_max, cat=LpContinuous) # Power transfered from the battery to the load.
P = LpVariable.dicts("P_A", V_steps, lowBound=0, upBound=0.9*P_A_max, cat=LpContinuous)  # Power generated by the Genset A.
P_load = LpVariable.dicts("P_A_load", V_steps, lowBound=0, upBound=0.9*P_A_max, cat=LpContinuous) # Power transfered from the Genset A to the load at time step k.
Z = LpVariable.dicts("Z", V_steps_z, lowBound=0, upBound=1, cat=LpInteger) # Aditional cost fuel oil consumption when starting Genset j.
FOC = LpVariable.dicts("FC_A", V_steps, lowBound=0, upBound= maxFC, cat=LpContinuous) # Specific fuel oil consumption.
P_to_bat =  LpVariable.dicts("P_A_to_bat", V_steps, lowBound=0, upBound=0.9*P_A_max, cat=LpContinuous) 
Y_to_bat = LpVariable.dicts("Y_to_bat", V_steps, lowBound=0, upBound=1, cat=LpBinary) # Genset selecter to charge the battery at time step k. 
Y_from_bat = LpVariable.dicts("Y_from_bat", V_steps, lowBound=0, upBound=1, cat=LpBinary) # Battery selecter to transfert to the Genset j st time step k.
Y = LpVariable.dicts("Y", V_steps, lowBound=0, upBound=1, cat=LpBinary) # Genset selecter : turned on : Y=1, turned off : Y=0. 
```


$\newline$ 
### Setting up the objective function.

To set up the objective function of the problem, the ``lpSum`` function is used along side with the optimization variable created ``Optim``, so it can be formulated as : ``Optim += lpSum (Expression) ``. the ``+=`` operator is used to update the Optim variable after each solving itteration. Note: the Objective function must be included first before the constraints are made, outherwise, it will just be interpreted as a constraint by the solver. 

In our case the, the objective is to minimize the Genset fuel oil consumption, therefore it is expressed as: 

```
Optim += lpSum (FC + L_added_cost), "objective function Minimization fuel oil consumption" 
```


$\newline$ 
### Setting up problem constraints. 

Constraints are expressed using the same command used for setting up the objective function, that's why the objective fucntion should be included first. 

The set of constraints for our problem are expressed as follow:

```

for k in V_steps:

  # Fuel oil consumption constraint.
  Optim += FOC[k] == P[k]*a_j + b_j - fc_j_offset*(1-Y[k]) 

  # Load requirements constraints
  Optim += P_load[k] + eff_from_bat*P_From_bat[k] == L[k]  
  Optim += P_load[k] + P_to_bat[k] == P[k] 


  # Genset logical constraints.
  Optim += P[k]  <= 0.9 * P_max * Y[k]
  Optim += P[k]  >= 0.2 * P_max * Y[k]

  # Battery charging logical constraints.
  Optim += P_to_bat[k] <= 0.9 * P_max * Y_to_bat[k]
  Optim += P_From_bat[k] <= 0.9 * P_max * Y_from_bat[k]
  Optim += Y_to_bat[k] + Y_from_bat[k]  <= 1
  

  # Charge balance logical constraints.
  if k == V_steps[0] : 
    Optim += Q_bat[k] == Q_0 + eff_to_bat*P_to_bat[k]*dt - P_From_bat[k]*dt


  else :   
    Optim += Q_bat[k] == Q_bat[k-1] + eff_to_bat*P_to_bat[k]*dt - P_From_bat[k]*dt

    
# Additional starting costs constraint.
for k in range(V_steps[0], V_steps[-1]): 
  Optim += Z[k] >= Y[k + 1] - Y[k] 
  
# Charge balance at the Final time step.
Optim += Q_bat[V_steps[-1]] == Q_final
```


$\newline$ 
### Solving the problem. 

After constructing the problem with the different steps, now we can solve it using the command, and store the results in a variable. something like : 

```
result = Optim.solve() 
```
Note that inside the parenthesis you can specify the solver you want to use, if nothing is specified then the defaut solver is used which is CBC solver. However, in our case we are using the Gurobi solver, therfore, we can call it as follow : 

```
result = Optim.solve(GUROBI())
```