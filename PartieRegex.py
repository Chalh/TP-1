# -*- coding: utf-8 -*-

import re
import sys
reload(sys)


def get_ingredient(ligne_ingredients):

    p2 = re.compile(
        r"((^\d+\s*[.,/à]*\d*\s*([Tt]asse[s]*|[Mm][Ll]|((cuillère[s]*|c) à (soupe|café|c|s))|[Oo]z|g|[Kk]g\b|[Cc][Ll]|boîte[s]*( de conserve)*|[Ll][Bb])*)+(\sà\s\d+\s([Tt]asse[s]*|[Mm][Ll]|((cuillère[s]*|c) à (soupe|café|c|s))|[Oo]z|g\b|[Cc][Ll]|boîte*|[Ll][Bb])*)*(\s\(.*\)\s)*)(\sde*d\'*\s)*(.*)(\n)")
    m2 = p2.search(ligne_ingredients)
    if m2 is not None:
        t_quantites =  m2.group(1)
        t_ingredient = m2.group(15)

    else:
        t_quantites = ""
        t_ingredient = ligne_ingredients[:-1]


    return t_quantites, t_ingredient


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
        quantite_ingredient = get_ingredient(line)
        ligne_ecrire = line.rstrip("\n") + "  " + "; QUANTITÉ:" + quantite_ingredient[0] + " ; " + "INGRÉDIENT:" + quantite_ingredient[1]
        nb_ligne = nb_ligne + 1
    else:
        ligne_ecrire = line.rstrip("\n") + "  " + "; QUANTITÉ:" +  " S/O ; INGRÉDIENT: S/O " + "\n"
    print ligne_ecrire

file.close()
fileext.close()
print(nb_ligne.__str__())
print(nb_ok.__str__())

