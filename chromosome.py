import string, random, os
from operator import itemgetter

#////////////////////CREATION ET OPERATIONS SUR LES CHROMOSOMES////////////////////
def makeRandomChromo_dict():
    #associe a chaque lettre Maj de l alphabet une lettre au hasard pour former un dict
    set_of_chars = set(string.ascii_uppercase)
    chromo = {}
    for c in string.ascii_uppercase:
        char = random.choice(list(set_of_chars))
        set_of_chars.remove(char)
        chromo[c] = char
    return chromo


def makeChromo_dict(chromo_list):
    #retourne le dict a partir de la liste correspondant au chromosome
    chromo_dict = {}
    for c in string.ascii_uppercase:
        char = chromo_list[0]
        chromo_list.remove(char)
        chromo_dict[c] = char
    return chromo_dict

def makeChromo_list(chromo_dict):
    #retourne la liste correspondant au chromosome a partir du dict
    chromo_list = []
    for c in string.ascii_uppercase:
        chromo_list.append(chromo_dict[c])
    return chromo_list

def reproduce(pere,mere):
    #on choisit un point de croisement aleatoire
    list_pere = makeChromo_list(pere)
    list_mere = makeChromo_list(mere)
    moitie = len(pere) // 2

    # Sélectionner aléatoirement la moitié des éléments de chaque liste
    elements_pere = random.sample(list_pere, moitie)
    for e in elements_pere:
        list_mere[list_mere.index(e)] = e

# Former la liste résultante en fusionnant les éléments sélectionnés
    return makeChromo_dict(list_mere)

def crossover(chromosome1, chromosome2):
    # Selectionner un (locus) point de croisement aleatoire
    crossover_point = random.randint(0, 25)
    
    # Créer les parties de chromosome résultantes du crossover
    e1 = {}
    e2 = {}
    
    for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        if i <= crossover_point:
            e1[c] = chromosome1[c]
            e2[c] = chromosome2[c]
        else:
            e1[c] = chromosome2[c]
            e2[c] = chromosome1[c]
    
    return e1, e2



def mutation(chromo_dict):
    #on choisis au hasard entre 0 et 5 le nbr de genes qui vont muter par inversion 
    size = len(list(chromo_dict.values()))
    nbr_genes_mutants = random.randint(0, 5)

    for i in range(nbr_genes_mutants):
        pt1 = random.randint(0, size - 1)
        pt2 = random.randint(0, size - 1)

        values = list(chromo_dict.values())
        keys = list(chromo_dict.keys())
        chromo_dict[keys[pt1]], chromo_dict[keys[pt2]] = values[pt2], values[pt1]

    return chromo_dict


#////////////////////CALCUL DE LA FITNESS D'UNE POPULATION///////////////////


def popFitness(population,calc_fitness,n):
    #calcule la fitness de chaque chromosome dans la population
    #Les resultats d'evaluation sont stockés avec l'index correspondant du chromosome dans 
    #une liste (decroissante) de tuples: [ (evaluation, index), ... ]
    populationScores = [ calc_fitness(population[i],n) for i in range(len(population)) ]
    populationScores = sorted(populationScores, key=itemgetter(0), reverse = True) #itemgetter(0) pour trier / au 1er élément du tuple
    return populationScores



