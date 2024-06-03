import os
import math

def read_freq(path):
    """
    
# lire une série de fichiers dans un répertoire donné et les traiter 
# pour créer une liste de dictionnaires. Chaque dictionnaire mappe 
# des clés dérivées des combinaisons de lettres de l'alphabet à des 
# valeurs provenant des fichiers.

 **Lecture et traitement du premier fichier ("d0")**:
   - Ouvre et lit le fichier "d0".
   - Sépare le contenu en lignes.
   - Remplit un dictionnaire où chaque lettre de l'alphabet est une clé et chaque ligne correspondante est une valeur.
   - Ajoute ce dictionnaire à la liste `l`.

 **Lecture et traitement des fichiers suivants ("d1", "d2", etc.)**:
   - Pour chaque fichier, lit le contenu et le sépare en lignes.
   - Crée un nouveau dictionnaire basé sur les clés existantes et l'alphabet.
   - Utilise une formule pour calculer une valeur numérique pour chaque nouvelle clé et assigne la ligne correspondante à cette clé.
   - Ajoute le nouveau dictionnaire à la liste `l`.
    
    """
    
    l = list()  #liste pour stocker les dictionnaires
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  #liste des lettres majiscules de l'alphabet
    lfiles = os.listdir(path)  # On liste tous les fichiers dans le répertoire donné

    if len(lfiles) == 0:
        return []

    d1 = dict()  
    with open(os.path.join(path, "d0"), 'r') as f:
        c = f.read()

    # On sépare le contenu en lignes
    c = c.split("\n")
    
    # On remplit le dictionnaire avec les lettres de l'alphabet comme clés et les lignes du fichier comme valeurs
    for la in range(len(alphabet)):
        d1[alphabet[la]] = c[la]
    
    # On ajoute ce dictionnaire à la liste l
    l.append(d1)

    # On parcourt les autres fichiers (d1, d2, etc.)
    for i in range(1, len(lfiles)):
        with open(os.path.join(path, "d" + str(i)), 'r') as f:
            c = f.read()

        c = c.split("\n")
        
        # On obtient les clés actuelles du dictionnaire
        lclefs = list(d1.keys())
        
        # On initialise un nouveau dictionnaire vide
        d2 = dict()
        
        # On parcourt chaque clé et chaque lettre de l'alphabet pour créer de nouvelles clés
        for j in range(len(lclefs)):
            for k in range(len(alphabet)):
                if l[-1][lclefs[j]] == 0:
                    # Si la valeur de la clé précédente est 0, on assigne 0 à la nouvelle clé
                    d2[lclefs[j] + alphabet[k]] = 0
                else:
                    # On calcule une valeur numérique pour la clé basée sur la position des lettres dans l'alphabet
                    val = [ord(m) - ord('A') for m in list(lclefs[j] + alphabet[k])]
                    sval = 0
                    for n in range(len(val)):
                        sval += (26 ** (len(val) - 1 - n)) * val[n]
                    # On assigne la ligne correspondante du fichier à la nouvelle clé
                    d2[lclefs[j] + alphabet[k]] = c[sval]
        
        # On ajoute le nouveau dictionnaire à la liste l
        l.append(d2)
    
    # On retourne la liste des dictionnaires
    return l

def count_ngrams(s, n) :
    l=[]
    for i in range(26**n):
        s=""
        for j in range(n):
            s+=chr(i//(26**j)%26+65)
        l.append(s)

    d={key: 0 for key in l}
    for i in range(len(s)-n+1):
        d[s[i:i+n]]+=1
    return d

def decrypt(chiffre, cle):
    decrypted_text = ''.join([cle.get(char, char) for char in chiffre])
    return decrypted_text

def fitness_freq(path, key, ref_freqs,n):
    fitness = 0
    lfiles = os.listdir(path)
    for filename in lfiles:
        with open(os.path.join(path, filename), 'r') as f:
            chiffre = f.read()
        decrypted = decrypt(chiffre, key)
        ngram_freqs = count_ngrams(decrypted, n)  
        for ngram in ngram_freqs: #itère sur les cles du dict
            if ngram in ref_freqs:
                fitness -= math.log(abs(ngram_freqs[ngram] - ref_freqs[ngram]))
