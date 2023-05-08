
# Generating single random load value (for testing).

def GOP():
    P_max = 1000

    from random import randint
    GOP = randint(0.8*P_max, 0.9*P_max)
    return GOP
