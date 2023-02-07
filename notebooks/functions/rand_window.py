# Generating random Load profil.
import random.randrange


def Load(r):

    P_A_max = 1000
    Profile = {}
    for i in range(0, 59):
        Profile[i] = random.randrange(0.2*P_A_max, 0.9*P_A_max)
    return Profile
