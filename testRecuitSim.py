import recuitSimule as rs
import freqs as fr
import lecture as lec

n0 = 1

  
#--------------------------------------------------------#

l_freqs = lec.read_freqs(r'donnees',n0)

def fitness_func(key,n):
    return fr.fitness_freq_file(r'Chiffres/chiffre_germinal_1_119_1', key, l_freqs ,n)


cle = rs.algoRecuitSimule(
    initial_temp=1000, 
    cooling_rate=0.75,
    calc_fitness=fitness_func, 
    n=n0, 
    max_iterations=5000
    )


print('\n CLE: ', cle)
print('\n FITNESS: ', fitness_func(cle,n0))
chiffre = chaine1 = "KPSNDSRVMPSHDTSPTTPRDMKPMRDPDCMBNYNDSRNVSHPTCPYPHTRNTSHPTNCEOHDWOMIPMNKNMSQVPKPTUPVFMOKSVHMPTRPTGNBTRPCNEOVDCCPPSRVUPH"
print('\n DECRYPTED TEXT: ', fr.decrypt(chiffre,cle))