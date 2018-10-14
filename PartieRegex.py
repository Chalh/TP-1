
# -*- coding: utf-8 -*-
# ########################################################################################################################
#                                                                                                                      #
# AUTEUR: CHIHEB EL OUEKDI
#  IFT - 7022
#  TRAVAIL-1
# DATE: 12 OCTOBRE 2018                                                                                                #
########################################################################################################################


import re
import sys
reload(sys)

########################################################################################################################
#                                                                                                                      #
#               FONCTION D'EXTRACTION DES QUANTITÉS/INGRÉDIENTS D'UNE PHRASE EN PARAMÈTRES
#                                                                                                                      #
########################################################################################################################

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

########################################################################################################################
#                                                                                                                      #
#               CHERCHER LES LIGNES QUI CONTIENNENT LE SUFFIXE "TION" POUR LES IGNORER DANS LA SUITE
#                                                                                                                      #
########################################################################################################################



p1 = re.compile(r"^((.*tion.*))$")



for line in file:
    m1 = p1.search(line)
    if m1 is None:
        quantite_ingredient = get_ingredient(line)
        ligne_ecrire = line.rstrip("\n") + "  " + "; QUANTITÉ:" + quantite_ingredient[0] + " ; " + "INGRÉDIENT:" + quantite_ingredient[1]

#    else:
#LES LIGNES QUI CONTIENNENT LE SUFFIXE "TION" ON ECRIT S/O DANS QUANTITÉ ET INGRÉDIENT
 #       ligne_ecrire = line.rstrip("\n") + "  " + "; QUANTITÉ:" +  " S/O ; INGRÉDIENT: S/O " + "\n"
    print ligne_ecrire

file.close()
fileext.close()


