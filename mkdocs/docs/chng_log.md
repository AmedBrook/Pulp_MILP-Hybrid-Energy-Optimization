## Releases.

#### Version 0.2.1.
   
    Date: 21-12-2022.
   * Re-scaling up the model to 60 time steps for an implementation to the full  
     time frame. 
   * Adopting dt=1 instead of 2/3.
   * Adding the a load requirement window 'L' compounded of tree level of power: 200 kwh, 
     400 kwh, 600 kwh as a matter of exemple.
   * Forcing logical constraints for the 'Y' LpVariable. 
   * Adapting suitable width for the bargraphs.
   * Setting up environment variables for Gurobi licence secret keys.
   
#### Version 0.1.5.
 

   * Importing 'sys' module and addiing the python 'environment cell' to keep track of the 
     python version. 
   * Dispensing of the CPLEX solver and adopting the built in solver CBC. 
   * Adopting one genset for the study m=5 ---> m=1 (1 Genset, One Battery). 
   * Addopting an additional fuel consumption when starting genset j (kg) of 
     K_j_start[0]=30 insted of 0.1 at the begining asumming can't ne shuted of during the  
     simulation time frame. The aditional cost are only on the initial step.
   * Moving the 'merge_dictionaries' function to the Introducing problem parameters section 
     instead of the Setting-up problem Constraints.
   * changing the name of the problem variable 'Prob' ---> 'Optim'. 
   * Adopting 'V_steps' vector instead of the 'steps' vector and dispencing of 'steps'.
   * Adopting List comprehension to define the 'V_steps' vector: V_steps = [x for x in  
     range (60)],instead of simple range : V_steps =  range(0, steps.shape[0]).
   * Rducing the LPvaraible dicitionnary path to :LpVariable.dicts(..) instead of full  
     attribute path pulp.LpVariable.dicts(..). 
   * Redefine the bounds for the 'P_bat' LpVariable as: lowBound=0.2*P_A_max, 
     upBound=0.9*P_A_max instead of lowBound=0, upBound=None.
   * Define the cat argument for the 'P_A' LpVaraible as Integer. 
   * Assiging a lowbound argument of zero to 'SFOC_A' LPVariable instead of 'None' value. 
   * Adopting binary LPvaribles 'Y_to_bat' and 'Y_from_bat' for the battery charge and discharge 
     binaray logic.
   * adopting the time steps loop (for k in V_steps:..) as the outer loop instead of the 
     number of the Genset for loop since we have only one Genset (for j in              
     range(1,m+1):..). 
   * Adopting 'V_steps' as a variable index instead of 'P_A' LPvariablein in the  
     dictionnary comprehension for the 'FC_k_j' varaible in the linear model for fuel 
     consumption of genset j defining the objective function.
   * Fixing the fuel consumption formulation of the 'FC' varabiable.
   * Using the lpSum function to sum up the 'FC' and 'L_added_cost' expressions in the   
     objective functin formulation. 
   * Adopting the Pulp 'lpSum' function to formulate load requirements constraint unstead 
     of the 'merge_dicitionnaries' function. 
   * Adopting a global outer for loop instead of doing for each constraint an own foorloop. 
   * Using a dicitionnay comprehension instead of to define 'P_A_A' variable.
   * Adding charge balance constraints using Optim += operator instead of just logical   
     definition.
   * Printing out the constraints status using the command 'Optim.variables'
      
#### Version 0.1.4.


   * Installing and testing out Pulp module and its packages
   * First formulation of the fuel minimization problem.
   * Structuring an Optimization problem using the PulP modeler. 
   * Trying out to print the returned values stored in the LP variables. 
   

Tests

#### Version 0.2.0.
   
   * Scaling down the the model to 3 time steps for testing purposes
   * Adopting Gurobi solver instead of Pulp's bilt in solver (CBC solver). 
   * Setting up a Gurobi licence container. 
   * Using different set of load profil scenarios 'L' insted of a fixed load vector. 
   * Dispensing of the 'merge_dictionaries' function. 
   * Introducing a fuel consumption function 'fuelCon' instead of using fixed values of 
     slope and intercept of the fule consumtion caracteristic.
   * formulating the a_j, b_j and maxFC values function of the fuelCon function.
   * Introducing the 'V_steps_z' vector specificaly for the Z LPvaraiable.
   * Introducion the 'V_steps' vector in the paramters section instead of setting-up 
     decision variables section.
   * Adopting the 'FC_A' LPvariable instead of the 'SFOC_A'
   * Visulizing the different returned values of the LPvariables outputs. 
   * Changing the name of the 'P_bat' to 'P_From_bat' for power transfered from the battery 
     to the load.
   * Changing the name of the 'Z_k_j' to 'Z' for Aditional cost fuel oil consumption. 
   * Adopting a lower bound of zero value for the 'P_A', 'P_A_load', 'P_From_bat' and 
     'P_A_to_bat' LPvariables instead of 0,2*P_A_max. 
   * Changing the 'Y_to_bat' and 'Y_to_bat' cat to LPvaraiables as LPinteger rather than 
     LPBinary. 
   * Adding the 'Y' LPvaraible (controlling the on-off logic of the genset).  
   * Dispensing of the outer for loops in the objective function formulation.
   * Dispensing of the FC_k_j variable in the objective function formulation. 
   * Adopting the 'K_j_start' as scaler in the objective fucntion rather than dictionnary. 
   * Dispensing of the 'lpSum' method in formulating power requirement constraint.
   * Dispensing of the 'merge_dicitionaries' function in formulating power requirements 
     constraint. 
   * Adopting the battery transfer efficiency rate 'eff_from_bat' in formulating   
     formulating 
     power requirements constraint.
   * Replacing the specific fuel oil consumption constraint by the Fuel consumption 
     constraint. 
   * Adopting If statment to reformulate the battery charge logics, 
   * Fixing the logic about the charge balance state doesn't depend on the privious 
     value of charge and power Optim += Q_bat[k] == Q_bat[k-1] + 
     eff_to_bat*P_A_to_bat[k]*dt - P_From_bat[k]*dt. 
   * Adding the battery charging logical constraints. 
   * Adopting the final step battery charge logic out of the nested if statement and out of 
     the for outer for loop. 
   
   
   
