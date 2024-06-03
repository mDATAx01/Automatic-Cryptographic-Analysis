import recuitSimule as rs
import freqs as fr

ITE_MAX = 1000
INITIAL_TEMP = 100
COOLING_RATE = 0.99

n = 1
l_freqs = fr.read_freq('C:\Users\Destock-afric\Desktop\X2\INFO\UE_Projet\algoGen\donnees')

def fitness_func(key,n):
    return fr.fitness_freq('C:\Users\Destock-afric\Desktop\X2\INFO\UE_Projet\algoGen\Chiffres', key, l_freqs,n)

print(rs.algoRecuitSimule(INITIAL_TEMP, COOLING_RATE, fitness_func,n, ITE_MAX))

