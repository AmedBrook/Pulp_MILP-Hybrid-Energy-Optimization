HYH
==============================

MILP Hybrid Energy Optimization 


Project's title.
=================


Fuel minimization: MILP model with semi-continuous power supply and battery logic.



Project's description and context. 
===============================


The project aims to explore the possibility of integrating 
energy storage faciltities within the shipping industry marcket. 
In this application we simulate one possible solution on how to
synchronize fuel based gensets with a battery storage system
alonge side with energy optimization to reduce energy cost throughout 
the trip journey. The whole project is build based on an optimization 
mathimatical model and uses MILP (mixed intiger linrear programing) 
methodes to solve optimaly the problem.  

In this Python notebook script we simulate an application used to optimize
fuel consumption for vessels using one genset to produce the energy one 
and one batter to store and realese to excess of that energy when needed in 
a hybrid mode.
The power from genset can be either in interval 0.2P_max - 0.9P_max or exactly 0.
The framwork used in this case study is Pupl, to solve a mixed intger linear 
programming problem toguether with first the built-in solver: CBCو and then with 
a commercial sover: Gurobi.





Project's case usage.
====================

this particular case is initially specefic for the offshore shipping industry as 
they are the most transportation fuel consuming and needing some sort of solutions to use fuel 
optimally in their trips. However this is not only exlusive to this sector, it 
can be easily extended to other sectors as long as the purpose is to optimize energy
usage and energy hybridization.





Project's environment.
======================

Using Conda environnment manager: 

. You create a new environment aside of the root, and called somthing
  recognisable, we named here as Energy_Optim, we have used here python version 3.9.7. to do so you tape: 
 
	- $ conda create --HYH_model python=3.9.7

. Activate the environment by taping :
  
	- $ conda activate --HYH_model.


 


Project's installations.
======================


Pulp modler.
------------

. In order to install Pulp modler pacjakges we use the command : 

	- $ conda install -c forge-pulp. 

. Then you can test the availble packages after installation using the commands: 

	- $ conda search -c forge-pulp. 
	- $ conda list


Gurobi Solver. 
-------------

. To install Gurobi solver packages, we use the command:
	- $ conda install -c gurobi gurobi.  

. Then you can test the availble packages after installation using the commands: 

	- $ conda search -c gurobi gurobi. 
	- $ conda list
