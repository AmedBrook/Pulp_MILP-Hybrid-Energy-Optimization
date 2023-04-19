
# lisxtr function.

from models.heo import *


def lixtr(FOC_,
          P_,
          P_load_,
          P_to_bat_,
          P_From_bat_,
          Q_bat_, Y_,
          Y_from_bat_,
          Y_to_bat_,
          Z_):

    FOC_ = []
    P_ = []
    P_load_ = []
    P_to_bat_ = []
    P_From_bat_ = []
    Q_bat_ = []
    Y_ = []
    Y_from_bat_ = []
    Y_to_bat_ = []
    Z_ = []

    nms = {0: FOC_,
           1: P_,
           2: P_load_,
           3: P_to_bat_,
           4: P_From_bat_,
           5: Q_bat_, 6: Y_,
           7: Y_from_bat_,
           8: Y_to_bat_,
           9: Z_}

    nmss = {0: 'FOC_',
            1: 'P_',
            2: 'P_load_',
            3: 'P_to_bat_',
            4: 'P_From_bat_',
            5: 'Q_bat_',
            6: 'Y_',
            7: 'Y_from_bat_',
            8: 'Y_to_bat_',
            9: 'Z_'}

    for v in Optim.variables():
        for nm in nmss:
            for i in V_steps:
                if v.name == (((nmss[nm])) + str(i)):
                    nms[nm].append(v.varValue)

    for nm in nms:
        print((nmss[nm]) + '=', (nms[nm]))

    return lixtr
