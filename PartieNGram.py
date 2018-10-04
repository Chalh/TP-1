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

def unigram_probalite(mot, lissage):
    if lissage == "Aucun":
        prob_mot = freq_dist_unigram.freq(mot)
    else: #Laplace
        prob_mot =  (freq_dist_unigram.__getitem__(mot)+1)/(nb_mot_proverbe + nb_mot_vocabulaire)

    return prob_mot

def bigram_probalite(bigram_seq, lissage):
    if lissage == "Aucun":
        prob_mot = freq_dist_bigrame.freq(bigram_seq)
    else: #Laplace
        prob_mot =  (freq_dist_bigrame.__getitem__(bigram_seq)+1)/(nb_mot_proverbe + nb_mot_vocabulaire)

    return prob_mot


def trigram_probalite(trigram_seq, lissage):
    if lissage == "Aucun":
        prob_mot = freq_dist_trigrame.freq(trigram_seq)
    else: #Laplace
        prob_mot =  (freq_dist_trigrame.__getitem__(trigram_seq)+1)/(nb_mot_proverbe + nb_mot_vocabulaire)

    return prob_mot


def probalite_phrase(phrase, lissage, N):
    switcher = {
        1: unigram_probalite,
        2: bigram_probalite,
        3: trigram_probalite,
    }
    tok_phrase = word_tokenize(phrase)
    prob_phrase = 1
    func = switcher.get(N, lambda: "Invalid")
    # Execute the function
    if N ==1:
        for v in tok_phrase:
            prob_phrase = func(v, lissage) + prob_phrase
    else:
        if N ==2:
            bgrm_phrase = list(nltk.bigrams(tok_phrase))
            for v in bgrm_phrase:
                prob_phrase = func(v, lissage) + prob_phrase
        else:
            trm_phrase = list(nltk.trigrams(tok_phrase))
            for v in trm_phrase:
                prob_phrase = func(v, lissage) + prob_phrase

    return prob_phrase



p1 = re.compile(r'{*"(.*)":\s*\["(.+\b)",\s"(.+\b)",\s"(.+\b)",\s"(.+\b)"],*}*')

#Lissage = "Lapace"
Lissage = "Aucun"

for n in range(1,4):
    print ("---------------------------------------%d - GRAME---------------------------------------------",n)
    file = open('test1.txt', 'r')
    for line in file:

        m1 = p1.search(line)

        if m1 is not None:
            proverbe = m1.group(1)
            proverbe_final = proverbe.replace("***", m1.group(2))
            prob_phrase_essai = probalite_phrase(proverbe_final, Lissage, n)

            for j in range (1,4):
                proverbe_essai = proverbe.replace("***", m1.group(2+j))
                prob_phrase = probalite_phrase(proverbe_essai,Lissage,n)
                if prob_phrase_essai < prob_phrase:
                    proverbe_final =  proverbe_essai
                    prob_phrase_essai = prob_phrase

            print proverbe_final

file.close()