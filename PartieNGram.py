import nltk
import re
from nltk import word_tokenize
import math
import sys
from nltk.probability import *


reload(sys)
sys.setdefaultencoding('utf8')

#Lecture du contenu du fichier d'entrainement
file = open('proverbes.txt', 'rb')
contenu_proverbes_train = file.read()
file.close()


#Preparation de la structure de calcul de probabilite avec NLTK

tokens_train = word_tokenize(contenu_proverbes_train)
bigram_train = list(nltk.bigrams(tokens_train))
trigram_train = list(nltk.trigrams(tokens_train))
vocabulaire = set(tokens_train)
nb_mot_vocabulaire = len(vocabulaire)
nb_mot_proverbe =len (tokens_train)
freq_dist_unigram = FreqDist(tokens_train)
freq_dist_bigrame = FreqDist(bigram_train)
freq_dist_trigrame = FreqDist(trigram_train)

def unigram_probalite(mot, lissage, delta):
    if lissage == "Aucun":
        prob_mot = float(freq_dist_unigram.freq(mot))
    else: #Laplace
        prob_mot =  float(freq_dist_unigram.__getitem__(mot)+delta)/float(nb_mot_proverbe + nb_mot_vocabulaire)
    if prob_mot ==0:
        return -99
    else:
        return math.log(prob_mot)


def bigram_probalite(bigram_seq, lissage,delta):
    c_mot_precedent = freq_dist_unigram.__getitem__(bigram_seq[0])

    if lissage == "Aucun":
        if c_mot_precedent == 0:
            prob_mot = 0
        else:
            prob_mot = float(freq_dist_bigrame.__getitem__(bigram_seq))/float(c_mot_precedent)
    else:  # Laplace
        prob_mot = float(freq_dist_bigrame.__getitem__(bigram_seq) + delta) / float(c_mot_precedent + nb_mot_vocabulaire)

    if prob_mot ==0:
        return -99
    else:
        return math.log(prob_mot)


def trigram_probalite(trigram_seq, lissage,delta):
    bigram_seq_precedent = list(nltk.bigrams(trigram_seq))
    c_seq_precedent = freq_dist_bigrame.__getitem__(bigram_seq_precedent.__getitem__(0))

    if lissage == "Aucun":
        if c_seq_precedent ==0:
            prob_mot = 0
        else:
            prob_mot = float((freq_dist_trigrame.__getitem__(trigram_seq))/float(c_seq_precedent))
    else:  # Laplace
         prob_mot = float(freq_dist_trigrame.__getitem__(trigram_seq) + delta) / float(c_seq_precedent + nb_mot_vocabulaire)

    if prob_mot ==0:
        return -99
    else:
        return math.log(prob_mot)


def probalite_phrase(phrase, lissage, delta, N):
    switcher = {
        1: unigram_probalite,
        2: bigram_probalite,
        3: trigram_probalite,
    }
    tok_phrase = word_tokenize(phrase)
    prob_phrase = 0
    func = switcher.get(N, lambda: "Invalid")
    # Execute the function
    if N ==1:
        for v in tok_phrase:
            prob_phrase = func(v, lissage,delta) + prob_phrase
    else:
        if N ==2:
            bgrm_phrase = list(nltk.bigrams(tok_phrase))
            for v in bgrm_phrase:
                prob_phrase = func(v, lissage,delta) + prob_phrase
        else:
            trm_phrase = list(nltk.trigrams(tok_phrase))
            for v in trm_phrase:
                prob_phrase = float(func(v, lissage,delta) + prob_phrase)
    return prob_phrase

def Calcul_Perplexite(phrase, lissage, delta, N):
    tok_phrase = word_tokenize(phrase)
    nbr_mot = tok_phrase.__len__()
    probabilite_phr = math.exp(probalite_phrase(phrase, lissage, delta, N))
    perplexite = float(probabilite_phr**(-(1/float(nbr_mot))))

    return perplexite

p1 = re.compile(r'{*"(.*)":\s*\["(.+\b)",\s"(.+\b)",\s"(.+\b)",\s"(.+\b)"],*}*')

Lissage = "Lapace"
test_delta = 2
#Lissage = "Aucun"


for n in range(1,4):
    print ("---------------------------------------"+n.__str__()+"- GRAME---------------------------------------------")
    file = open('test1.txt', 'r')
    for line in file:

        m1 = p1.search(line)

        if m1 is not None:
            proverbe = m1.group(1)
            proverbe_final = proverbe.replace("***", m1.group(2))
            prob_phrase_essai = prob_phrase = probalite_phrase(proverbe_final,Lissage,test_delta,n)

            for j in range (0,4):
                proverbe_essai = proverbe.replace("***", m1.group(2+j))
                prob_phrase = probalite_phrase(proverbe_essai,Lissage,test_delta,n)
               # print proverbe_essai + ";" + prob_phrase.__str__()
                if prob_phrase_essai < prob_phrase:
                    proverbe_final =  proverbe_essai
                    prob_phrase_essai = prob_phrase
            perplexite_prvfinal = Calcul_Perplexite(proverbe_final,Lissage,test_delta,n)
            print proverbe_final+";"+ perplexite_prvfinal.__str__()

file.close()