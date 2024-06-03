import algoGen, chromosome

ITE_MAX = 100
OBJECTIF = 75
POP_SIZE = 20000
OBJECTIF_GLOBAL = 75

chiffre_1 = 'KPSNDSRVMPSHDTSPTTPRDMKPMRDPDCMBNYNDSRNVSHPTCPYPHTRNTSHPTNCEOHDWOMIPMNKNMSQVPKPTUPVFMOKSVHMPTRPTGNBTRPCNEOVDCCPPSRVUPH'
clair_1 = 'CETAITDUNETRISTESSEDINCENDIEILNYAVAITDAUTRESLEVERSDASTRESALHORIZONMENACANTQUECESFEUXNOCTURNESDESPAYSDELAHOUILLEETDUFER'

algoGen.geneticAlgorithm(chiffre_1, clair_1, POP_SIZE, 0.2, 0.7, 0.7)

"""
chromo_sol = dict()
for c,i in zip(chiffre_1,range(len(chiffre_1)) ):
    chromo_sol[c] = clair_1[i]

dechiffre_1 = algoGen.decrypt_string(chiffre_1, chromo_sol)
fitness_score = chromosome.calc_fitness(chiffre_1, clair_1, chromo_sol)
    

fitness_list = []
i = 0
while i < 1000:
    print('Iteration: ', i)
    chromo_sol = algoGen.geneticAlgorithm(chiffre_1,clair_1, POP_SIZE, 0.7, 0.7, 0.7)
    dechiffre_1 = algoGen.decrypt_string(chiffre_1, chromo_sol)
    fitness_score = chromosome.calc_fitness(chiffre_1, clair_1, chromo_sol)
    fitness_list.append(fitness_score)
    if fitness_score >= OBJECTIF_GLOBAL:
        break
    i+=1

print('Solution: \n ')
print(chromo_sol)
print('\n Texte clair: \n', clair_1)
print('Texte dechiffre: \n', dechiffre_1)
print('Fitness: ', fitness_score, ' / ', len(chiffre_1))
"""