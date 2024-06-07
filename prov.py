
def count_monograms(s) :
    l=[chr(i+65).upper for i in range(26)]
    d={key: 0 for key in l}
    for i in range(len(s)):
        d[s[i]]+=1
    return d

def count_bigrams(s) :
    l=[]
    for i in range(26):
        for j in range(26):
            l.append( (chr(i+65)+chr(j+65)).upper)
    d={key: 0 for key in l}
    for i in range(len(s)-1):
        d[s[i]+s[i+1]]+=1
    return d

def count_trigrams(s) :
    l=[]
    for i in range(26):
        for j in range(26):
            for k in range(26):
                l.append( (chr(i+65)+chr(j+65)+chr(k+65)).upper)
    d={key: 0 for key in l}
    for i in range(len(s)-2):
        d[s[i]+s[i+1]+s[i+2]]+=1
    return d

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
                fitness -= math.log(1 / abs(ngram_freqs[ngram] - ref_freqs[ngram]))





"""
def makedicofreq(chaine):
    with open(r"C:\Users\Jeune\Documents\projet\data") as f:
        # Lit la première ligne du fichier, la divise en une liste de chaînes en utilisant la tabulation comme séparateur
        l = f.readline().split("\t")

    # dict pour stocker les correspondances entre les lettres de l'alphabet et les éléments de la première ligne du fichier
    dico = dict()

    # Associe chaque lettre majuscule de l'alphabet à un élément de la liste 'l'
    for i in range(len(l)):
        dico[chr(i + 65)] = l[i]
    
    # Calcule la longueur de la chaîne d'entrée
    lengthchaine = len(chaine)
    
    # dict pour stocker les fréquences des lettres dans la chaîne d'entrée
    dicochaine = dict()
    
    # Initialise chaque lettre de l'alphabet à 0 dans le dictionnaire 'dicochaine'
    for la in alphabet:
        dicochaine[la] = 0
    
    # Boucle à travers chaque lettre de la chaîne d'entrée
    for letter in chaine:
        # Vérifie si la lettre fait partie de l'alphabet
        if letter in alphabet:
            # Incrémente la fréquence de la lettre dans 'dicochaine' par la fraction (1/longueur de la chaîne)
            dicochaine[letter] += (1 / lengthchaine)
    
    # Renvoie les dictionnaires 'dico' et 'dicochaine' en tant que résultats de la fonction
    return dico, dicochaine



def makedicosuiv(chaine):
    with open(r"C:\Users\Jeune\Documents\projet\data") as f:
        l=f.read().split("\n")
        print(len(l))
    dico = dict()
    l=l[1:len(l)-1]

    for i in range(len(alphabet)):
        dico[chr(i+65)]=dict()
        g=l[i].split("\t")
        for j in range(len(alphabet)):
            dico[chr(i+65)][chr(j+65)]=g[j]
    dicochaine=dict()
    dicotemp={y:0 for y in alphabet}
    for letter in chaine:
        if letter in alphabet : 
            dicotemp[letter]+=(1)
    for la in alphabet:
        dicochaine[la]={la:0 for la in alphabet}
    for u in range(len(chaine)-1):
        if chaine[u] and chaine[u+1] in alphabet : 
            dicochaine[chaine[u]][chaine[u+1]]+=(1/dicotemp[chaine[u]])
    return dico, dicochaine


def evaluation(chaine):
    val = 0
    dicofreq, dicochainefreq = makedicofreq(chaine)
    dicosuiv, dicosuivchaine = makedicosuiv(chaine)
    for i in dicofreq.keys(): 
        if i in alphabet:
            val+=(float(dicofreq[i])-dicochainefreq[i])**2
    for i in dicosuiv.keys():
        for j in alphabet:
            val+=math.pow((float(dicosuiv[i][j])-dicosuivchaine[i][j])**2,1/16)
    return vals


def execution(evaluation, file, k):
    # Rembobine le fichier à son début
    file.seek(0)
    
    # Lit tout le contenu du fichier et le stocke dans 'c'
    c = file.read()
    
    # Initialise une liste contenant l'alphabet
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Crée une copie de l'alphabet pour représenter la clé de substitution
    clef = alphabet.copy()
    
    # Initialise un compteur
    compteur = 0
    
    # Effectue les étapes suivantes tant que le compteur est inférieur à 200
    while compteur < 200:
        # Choix aléatoire de deux lettres de l'alphabet
        lettre1, lettre2 = random.choice(alphabet), random.choice(alphabet)
        
        # Copie de la chaîne 'c' pour pouvoir la modifier
        listechaine = list(c)
        chainenouv = listechaine.copy()
        
        # Remplace les occurrences de 'lettre1' par 'lettre2' et vice versa dans la chaîne
        for lettre in range(len(c)):
            if chainenouv[lettre] == lettre1:
                chainenouv[lettre] = lettre2
            elif chainenouv[lettre] == lettre2:
                chainenouv[lettre] = lettre1
        
        # Évalue la chaîne actuelle et la chaîne modifiée avec la fonction d'évaluation
        evalprec = evaluation("".join(listechaine), l, k)
        eval = evaluation("".join(chainenouv), l, k)
        
        # Si la nouvelle évaluation est meilleure que l'évaluation précédente
        if evalprec < eval:
            # Met à jour la chaîne et la clé de substitution
            listechaine = chainenouv.copy()
            clef[clef.index(lettre1)], clef[clef.index(lettre2)] = lettre2, lettre1
        
        # Si l'évaluation précédente est égale à l'évaluation de la chaîne actuelle, incrémente le compteur
        if evalprec == evaluation("".join(listechaine), l, k):
            compteur += 1
        else:
            compteur = 0  # Réinitialise le compteur
        
        # Met à jour la chaîne 'c' avec la chaîne modifiée
        c = "".join(listechaine)
    
    # Retourne la chaîne résultante, la clé de substitution et la longueur de la chaîne
    return c, "".join(clef), len(list(c))

"""
