import random
import math
from itertools import product

import freqs as fr




def modify_key(key):
    """
    échanger deux lettres au hasard.
    
    """
    new_key = key.copy()
    keys = list(new_key.keys())
    a, b = random.sample(keys, 2)
    new_key[a], new_key[b] = new_key[b], new_key[a]
    return new_key


def generate_random_key():
    
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def algoRecuitSimule(initial_temp, cooling_rate, calc_fitness, n, max_iterations):
    
    current_key = generate_random_key()
    current_fitness = calc_fitness(current_key, n)
    best_key = current_key
    best_fitness = current_fitness
    temp = initial_temp

    i=0
    for i in range(max_iterations):
        print('\n \nIteration: ', i)
        new_key = modify_key(current_key)
        new_fitness = calc_fitness(new_key, n)

        if new_fitness > current_fitness:
            current_key = new_key
            current_fitness = new_fitness

        else:
            p=temp/initial_temp
            if random.random() < p:
                current_key = new_key
                current_fitness = new_fitness
        
        temp *= cooling_rate  

    return current_key

