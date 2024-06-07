import algoGen as ag
import freqs as fr
import lecture as lec

n0 = 3

#geneticAlgorithm(pop_size, elit_rate, cross_rate,mut_rate, calc_fitness,n, max_iterations, taille_file, marge):
    
#--------------------------------------------------------#

l_freqs = lec.read_freqs(r'donnees',n0)

def fitness_func(key,n):
    return fr.fitness_freq_file(r'Chiffres/chiffre_germinal_1_119_1', key, l_freqs ,n)

#cle= ag.geneticAlgorithm(2000, 0.2, 0.4, 5, fitness_func, 1, 500, 50, 0.5)
cle = ag.geneticAlgorithm(
    pop_size=20000,
    elit_rate=0.2,
    cross_rate=0.4,
    mut_rate=0.1,
    calc_fitness=fitness_func,
    n=n0,
    max_iterations=500,
    taille_file=10,
    marge=0.1
)


print('\n CLE: ', cle)
print('\n FITNESS: ', fitness_func(cle,n0))
chiffre = chaine1 = "KPSNDSRVMPSHDTSPTTPRDMKPMRDPDCMBNYNDSRNVSHPTCPYPHTRNTSHPTNCEOHDWOMIPMNKNMSQVPKPTUPVFMOKSVHMPTRPTGNBTRPCNEOVDCCPPSRVUPH"
print('\n DECRYPTED TEXT: ', fr.decrypt(chiffre,cle))