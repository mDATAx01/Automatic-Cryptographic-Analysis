import random
import math
import os
from itertools import product

import freqs as fr


def generate_random_key():
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))


def modify_key(key):
    """
    echanger deux lettres au hasard.
    """
    new_key = key.copy()
    a, b = random.sample(new_key.keys(), 2)
    new_key[a], new_key[b] = new_key[b], new_key[a]
    return new_key


def algoRecuitSimule(initial_temp, cooling_rate, calc_fitness,n, max_iterations):
    current_key = generate_random_key()
    current_temp = initial_temp
    
    best_key = current_key
    best_fitness = calc_fitness(current_key,n)

    for i in range(max_iterations):
        new_key = modify_key(current_key)
        new_fitness = calc_fitness(new_key,n)

        if new_fitness < best_fitness:
            best_key = new_key
            best_fitness = new_fitness

        if new_fitness < calc_fitness(current_key,n):
            current_key = new_key
        else:
            proba = math.exp((calc_fitness(current_key,n) - new_fitness) / current_temp)
            if random.random() < proba:
                current_key = new_key

        current_temp *= cooling_rate

        if current_temp < 1e-10:
            break

    return best_key

