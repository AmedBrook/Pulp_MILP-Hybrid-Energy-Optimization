
# lisxtr function.


def lixtr():
    import numpy as np
    import pulp

    dt = 1
    t_max = 10
    t = np.atleast_2d(np.arange(0, t_max, dt)).T.conj()
    n = len(t)
    V_steps = [x for x in range(0, n)]
    Optim = pulp.LpProblem('Energy_Opt', pulp.LpMinimize)

    FC_ = ([] for i in range(len(V_steps)))
    P_ = ([] for i in range(len(V_steps)))
    P_load_ = ([] for i in range(len(V_steps)))
    P_to_bat_ = ([] for i in range(len(V_steps)))
    P_From_bat_ = ([] for i in range(len(V_steps)))
    Q_bat_ = ([] for i in range(len(V_steps)))
    Y_ = ([] for i in range(len(V_steps)))
    Y_from_bat_ = ([] for i in range(len(V_steps)))
    Y_to_bat_ = ([] for i in range(len(V_steps)))
    Z_ = ([] for i in range(len(V_steps)))

    nms = {
     0: FC_,
     1: P_,
     2: P_load_,
     3: P_to_bat_,
     4: P_From_bat_,
     5: Q_bat_,
     6: Y_,
     7: Y_from_bat_,
     8: Y_to_bat_,
     9: Z_
     }

    nmss = {
     0: 'FOC_',
     1: 'P_',
     2: 'P_load_',
     3: 'P_to_bat_',
     4: 'P_From_bat_',
     5: 'Q_bat_',
     6: 'Y_',
     7: 'Y_from_bat_',
     8: 'Y_to_bat_',
     9: 'Z_'
     }

    for v in Optim.variables():
        for nm in nmss:
            for i in V_steps:
                if v.name == (((nmss[nm])) + str(i)):
                    nms[nm].append(v.varValue)

    for nm in nms:
        print((nmss[nm]) + '=', (nms[nm]))

    return lixtr

