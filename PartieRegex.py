# -*- coding: utf-8 -*-

import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

file = open('ingredients.txt','r')
fileext =  open("log.txt", 'w')

# Une ligne d ingredient ne contient pas de mot contenant la suffixe tion

p1 = re.compile(r"^((.*tion.*))$")

#   MESURE [UNITÉ] INGRÉDIENT
nb_ligne = 1
nb_ok = 1
for line in file:
    m1 = p1.search(line)
    nb_ok = nb_ok + 1
    if m1 is None:
        p2 = re.compile(
            r"(^\d+\s*[.,/à]*\d*\s*([Tt]asse[s]*|[Mm][Ll]|((cuillère[s]*|c) à (soupe|café|c|s))|[Oo]z|g\b|[Cc][Ll]|boîte[s]*|[Ll][Bb])*)+(\sà\s\d+\s([Tt]asse[s]*|[Mm][Ll]|((cuillère[s]*|c) à (soupe|café|c|s))|[Oo]z|g\b|[Cc][Ll]|boîte*|[Ll][Bb])*)*(\s\(.*\)\s)*(\sde*d\'*\s)*(.*\n)")
        m2 = p2.search(line)
        if m2 is not None:
            ligne_ecrire = nb_ligne.__str__() +":" +line[:-1] + "  " +  ": QUANTITÉ:" + m2.group(1) + "  " + "INGRÉDIENT:" + m2.group(13) + "\n"
            print ligne_ecrire
            fileext.write (ligne_ecrire)
            #fileext.write(nb_ligne.__str__() + " :INGRÉDIENT:" + m2.group(13) + "\n")
        else:
            ligne_ecrire =nb_ligne.__str__() +":"+ line[:-1] + "  " +  ": QUANTITÉ:" + "  " + "INGRÉDIENT:" + line[:-1] + "\n"
            print ligne_ecrire
            fileext.write (ligne_ecrire)
    nb_ligne = nb_ligne + 1
file.close()
fileext.close()
print(nb_ok.__str__())