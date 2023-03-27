Problem size.
=================

Linear programing (LP) variables are the variables whose values the optimizer will solve for in each time step. 

![Screenshot](img/hyh_illustration_lpvariables.png)

We need to know the problem size in order to see if the problem is computationaly cost effective or not, our problem size is mainly dependant on the size of the load window time frame (aka : steps ${n}$ ), the number of LP variables and the number of gensets ${m}$ (we use 1 genset in our case). 

- Continuous : $\hspace{3cm}\hspace{1cm} {3} \cdot {n} \cdot {m}$    
- Binary : $\hspace{4cm}\hspace{1cm} {2} \cdot {n} \cdot {m}$   

- Number of constraints : $\hspace{1cm}\hspace{1cm} {7} \cdot {n} \cdot {m} + {3} \cdot {n}$ $\hspace{1cm}$ 