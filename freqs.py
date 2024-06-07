import os
import math

"""
FITNESS :                1
                   -------------
                     1 + |f - r|
"""

def count_ngrams_freqs(s, n) :
    l=[]
    for i in range(26**n):
        s=""
        for j in range(n):
            s+=chr(i//(26**j)%26+65)
        l.append(s)
    d={key: 0 for key in l}
    for i in range(len(s)-n+1):
        d[s[i:i+n]]+=1

    sum = 0
    for key in d:
        sum += d[key]

    return d



def decrypt(chiffre, cle):
    decrypted_text = ''.join([cle.get(char, char) for char in chiffre])
    return decrypted_text



def fitness_freq_file(file_path, key, l_freqs, n):
    fitness = 0
    ref_freqs = l_freqs[n]  
        
    # S'assurer que le chemin est bien un fichier
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            text = f.read()
            decrypted_text = decrypt(text, key)
            ngram_freqs = count_ngrams_freqs(decrypted_text, n)
            
            # Calcul de la fitness par rapport aux fréquences de référence
            for ngram in ngram_freqs.keys():
                ref = ref_freqs[ngram]
                actual = ngram_freqs[ngram]
                total_fitness += float(1/(1 + math.fabs(ref - actual)))
                
    return fitness



def fitness_freq_all_files(path, key, l_freqs, n):
    total_fitness = 0
    ref_freqs = l_freqs[n]  # On utilise les fréquences de référence
    
    # Parcourir les fichiers dans le répertoire spécifié
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        
        # S'assurer que le chemin est bien un fichier
        if os.path.isfile(file_path):
            total_fitness+=fitness_freq_file(file_path, key, l_freqs, n)
        
    return total_fitness

def fitness_freq_file(file_path, key, l_freqs, n):
    fitness = 0
    ref_freqs = l_freqs[n]  
    #print('\n FLAG 1')
    
    if os.path.isfile(file_path):
        #print('\n FLAG 2')
        with open(file_path, 'r') as f:
            text = f.read()
            decrypted_text = decrypt(text, key)
            ngram_freqs = count_ngrams_freqs(decrypted_text, n)
            #print('\n NGRAM FREQS:', ngram_freqs)
            
            # Calcul de la fitness par rapport aux fréquences de référence
            for ngram in ngram_freqs.keys():
                ref = ref_freqs[ngram]
                actual = ngram_freqs[ngram]
                fitness += float(1/(1 + math.fabs(ref - actual)))
            #print('\n FLAG 3')
    return fitness
