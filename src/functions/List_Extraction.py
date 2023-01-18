
#List extraction function.


def list_extract():
  
  import numpy as np
  import pulp
  pulp.pulpTestAll()
  from pulp import all
  
  dt = 1
  t_max = 60
  t = np.atleast_2d(np.arange(0,t_max,dt)).T.conj()
  n = len(t)
  V_steps = [x for x in range (0,n)]   
  Optim = pulp.LpProblem('Energy_Opt',pulp.LpMinimize)

  FC_A_, P_A_, P_A_load_, P_A_to_bat_, P_From_bat_, Q_bat_, Y_, Y_from_bat_, Y_to_bat_, Z_ = ([] for i in range(10))


  nms = {0:FC_A_, 1:P_A_, 2: P_A_load_, 3:P_A_to_bat_, 4:P_From_bat_, 5: Q_bat_, 6: Y_, 7: Y_from_bat_, 8: Y_to_bat_, 9:Z_}
  nmss = {0:'FC_A_', 1:'P_A_', 2: 'P_A_load_', 3:'P_A_to_bat_', 4:'P_From_bat_', 5: 'Q_bat_', 6: 'Y_', 7: 'Y_from_bat_', 8: 'Y_to_bat_', 9:'Z_'}

  for v in Optim.variables():
    for nm in nmss:
      for i in V_steps:
        if v.name == (((nmss[nm])) + str(i)):
          nms[nm].append(v.varValue)

  for nm in nms:
      print((nmss[nm]) + '=', (nms[nm]))

  return list_extract
