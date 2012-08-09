from random import randint
from random import choice

N = 1000

def simulate(N):
    K = 0
    doors = range(1, 4)
    for i in range(N):
        actual_position = randint(1, 3)
        guess = randint(1, 3)
        shown = choice([d for d in doors if d not in [guess, actual_position]])
        switch = [x for x in doors if x not in [guess, shown]][0]
        if switch == actual_position:
            K += 1
    return float(K) / float(N)

print simulate(N)
