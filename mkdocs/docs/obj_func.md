Optimization objective
======================

#### Objective function

The objective function is the goal behind why we set the problem. In our case the problem is an optimization problem so the the objective functin is an optimization objective. However the Optimization objective is two types either a maximization objective or minimization objective. Since we wish to reduce the energy cost then our optimzatio objective is a minimization one. 


#### Problem minimization objective
---

In our case the miminzation objective is that The total fuel consumptions (kg) of the trip which are fuel consumption (as a function of required power output) for the genset including an additional cost for re starting the genset. therefore the Problem minimization objective could be formulated as follow : 

\begin{flalign*}
\mathrm{Minimize}\;\;\;\;\;\sum_{k=1}^n {FC}_{k\;} \cdot \frac{\Delta t}{1000}+K_{\mathrm{start}}. \sum_{k=2}^n Z_k 
\end{flalign*}

<br>

given the fuel consumption linear model : 

\begin{align}
& {FC}_{k\;} ={aP}_{k\;} +b-{fc}_{offset} \cdot \left(1-y_k \right)\  & \forall\,\,\,\,\,\, k=1,\dots ,n
\end{align}

<br>

