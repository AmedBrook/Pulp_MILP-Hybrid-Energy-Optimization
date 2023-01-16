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
