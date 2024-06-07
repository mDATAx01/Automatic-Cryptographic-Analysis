import os
import itertools

#l_freqs = fr.read_freq(r'donnees')


def read_freqs(path,n):
    l_res = []  
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  
    lfiles = os.listdir(path)  

    if len(lfiles) == 0:
        return []
    
    for i in range(n+1):
        ngrams = ["".join(elt) for elt in itertools.product(alphabet, repeat=i)]
        with open(os.path.join(path, "d" + str(i)), 'r') as f:
            c = f.read()

        c = c.split("\n")
        c.pop()
        
        # Convertir les valeurs en nombres et calculer la somme
        t = [int(elt) for elt in c]
        total = sum(t)
        
        d = {ngrams[i]: int(c[i]) / total for i in range(len(ngrams))}
        
        l_res.append(d)
    l_res[0] = n
    return l_res
        
with open('frequences.txt', 'w') as f:
    for d in read_freqs(r'donnees',2):
        f.write(str(d))
        f.write('\n')