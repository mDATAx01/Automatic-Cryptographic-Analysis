import numpy as np
import os
import random

import chromosome

ITE_MAX = 1000
OBJECTIF = 5000
POP_SIZE = 20000



def geneticAlgorithm(pop_size, elit_rate, cross_rate,mut_rate, calc_fitness,n, max_iterations):
    #population initiale de chromosomes aleatoires
    population = [chromosome.makeRandomChromo_dict() for i in range(pop_size)]
    
    # probabilites des rangs pour la sélection de chromosomes
    #on cree ici une liste de probabilités decroissantes [0, 1/n, 2/n, ..., 1]
    sum_r = (len(population) * len(population) + 1) / 2
    ranksProbabilities = [((i + 1) / sum_r) for i in range(len(population))]
    ranksProbabilities = sorted(ranksProbabilities, reverse=True)
   
    # Boucle jusqu'à ce qu'une condition de fin soit atteinte
    i = 0

    solution = []


    while i<max_iterations:
        # fitness de la population
        #liste decroissante de tuples: [ (evaluation, index), ... ]
        populationScores = chromosome.popFitness(population, calc_fitness,n)
        
        # Verifie si l'un des chromosomes a atteint la solution
        if populationScores[0][0] >= OBJECTIF:
            print( chromosome.calc_fitness(population[populationScores[0][1]],n) )

        # Selection les meilleurs chromosomes (elitisme), puis crossover et mutation
        # pour passer a la generation suivante
        newPopulation = [ population[populationScores[i][1]] for i in range(int(pop_size * elit_rate)) ]
        
        #reproduction
        for i in range(len(newPopulation)-1):
            new_chromo = chromosome.reproduce(newPopulation[i], newPopulation[i+1])
            newPopulation.append(new_chromo)

        #crossover
        cross_size = int(cross_rate * pop_size) 
        for i in range(cross_size):
            # deux parents selectionnes par roulette de selection basee sur les ranksProbabilities
            parent = np.random.choice(newPopulation, 2, ranksProbabilities)
            
            tmp_1,tmp_2 = chromosome.crossover(parent[0], parent[1])
            i1,i2 = newPopulation.index(parent[0]), newPopulation.index(parent[1])

            newPopulation[i1]=tmp_1
            newPopulation[i2]=tmp_2

        #mutation
        mut_size = int(mut_rate * pop_size)
        for i in range(mut_size):
            i_mutant= random.randint(0,len(newPopulation)-1)   
            newPopulation[i_mutant] = chromosome.mutation(newPopulation[i_mutant])
        
        
        newPopulationScores = chromosome.popFitness(newPopulation, calc_fitness,n)
        solution.append(newPopulation[newPopulationScores[0][1]])

        population = newPopulation
        print('Taille de la population: ', len(population))
        i+=1
    
    #pas de solution satisfaisante trouvée
    sol_fitness = []
    for i in range(len(solution)):
        fit_tmp =calc_fitness(solution[i],n)
        sol_fitness.append(fit_tmp)
    print('Meilleure fitness atteinte: \n', max(sol_fitness))

def decrypt_string(chiffre_txt, chromo_dict):
    # Dechiffrer le texte en utilisant le chromosome fourni
    dechiffre_txt = ''
    for char in chiffre_txt:
        dechiffre_txt += chromo_dict[char]
        
    return dechiffre_txt

def decrypt_file(chiffre_file, chromo_dict):
    # Charger le contenu du fichier chiffre
    with open(chiffre_file, 'r') as f:
        chiffre_text = f.read().strip()

    # Dechiffrer le texte en utilisant le chromosome fourni
    clair_text = ''
    for char in chiffre_text.lower():
        clair_text += chromo_dict[char]
        
    return clair_text

