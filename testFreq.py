import algoGen as ag
import freqs as fr
import lecture as lec

l_freqs = lec.read_freqs(r'donnees',2)
n=1
def fitness_func(key,n):
    return fr.fitness_freq_file(r'Chiffres/chiffre_germinal_1_119_1', key, l_freqs ,n)

chaine1 = "KPSNDSRVMPSHDTSPTTPRDMKPMRDPDCMBNYNDSRNVSHPTCPYPHTRNTSHPTNCEOHDWOMIPMNKNMSQVPKPTUPVFMOKSVHMPTRPTGNBTRPCNEOVDCCPPSRVUPH"
chaine2 = "CETAITDUNETRISTESSEDINCENDIEILNYAVAITDAUTRESLEVERSDASTRESALHORIZONMENACANTQUECESFEUXNOCTURNESDESPAYSDELAHOUILLEETDUFER"

correspondance = {}

for char1, char2 in zip(chaine1, chaine2):
    correspondance[char1] = char2

print(correspondance)
print( '\n',fr.decrypt(chaine1,correspondance))
fit=fitness_func(correspondance,n)
print('\n FITNESS: ', fit)