## Random Chance Simulation

# Simulating Coin Flips
import random as rand

def sim_probability(num_heads, num_flips):
    n = 1
    count = 0
    while n < 10000:
        flips = 0
        heads_trial = 0
        while flips < num_flips:
            r = rand.random()
            if r < 0.5:
                heads_trial += 1
            flips += 1
        if num_heads == heads_trial:
            count += 1
        n += 1
    return count/10000

# Roulette Wheel Selection