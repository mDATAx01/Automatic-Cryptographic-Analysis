import algoGen as ag
import freqs as fr

ITE_MAX = 1000
OBJECTIF = 5000
POP_SIZE = 20000

n = 1
l_freqs = fr.read_freq('C:\Users\Destock-afric\Desktop\X2\INFO\UE_Projet\algoGen\donnees')

def fitness_func(key,n):
    return fr.fitness_freq('C:\Users\Destock-afric\Desktop\X2\INFO\UE_Projet\algoGen\Chiffres', key, l_freqs,n)

#geneticAlgorithm(pop_size, elit_rate, cross_rate,mut_rate, calc_fitness,n)
ag.geneticAlgorithm(POP_SIZE, 0.2, 0.5,0.1, fitness_func, n, ITE_MAX)
