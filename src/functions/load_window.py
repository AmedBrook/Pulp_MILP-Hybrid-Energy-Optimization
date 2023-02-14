# lwd function.
import numpy as np


def lwd(
 val11, val12, val13,
 val21, val22, val23,
 val31, val32, val33,
 val41, val42, val43,
 L1, L2, L3, L4):

    L = {}

    E1 = np.atleast_2d(np.linspace(val11, val12, val13)).T.conj()
    E2 = np.atleast_2d(np.linspace(val21, val22, val23)).T.conj()
    E3 = np.atleast_2d(np.linspace(val31, val32, val33)).T.conj()
    E4 = np.atleast_2d(np.linspace(val41, val42, val43)).T.conj()

    L1 = dict(enumerate(E1.flatten(), L1))
    L2 = dict(enumerate(E2.flatten(), L2))
    L3 = dict(enumerate(E3.flatten(), L3))
    L4 = dict(enumerate(E4.flatten(), L4))
    L = {**L1, **L2, **L3, **L4}
    return L
# Function testing.


lwd(
 200, 200, 10,
 400, 400, 10,
 600, 600, 10,
 600, 200, 30,
 0, 10, 20, 30)
