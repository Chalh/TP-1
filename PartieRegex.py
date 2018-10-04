import re

file = open('ingredients.txt', 'r')
fileext= open ("log.txt","w")
p1 = re.compile(r"^((.*tion.*))$")

#   MESURE [UNITÉ] INGRÉDIENT
nb_ligne=1
nb_ok = 1
for line in file:
    m1 = p1.search(line)
    nb_ok = nb_ok +1
    if m1 is None:
        p2= re.compile(r"(^\d+\s*[.,/à]*\d*\s*([Tt]asse[s]*|[Mm][Ll]|((cuillère[s]*|c) à (soupe|café|c|s))|[Oo]z|g\b|[Cc][Ll]|boîte[s]*|[Ll][Bb])*)+(\sà\s\d+\s([Tt]asse[s]*|[Mm][Ll]|((cuillère[s]*|c) à (soupe|café|c|s))|[Oo]z|g\b|[Cc][Ll]|boîte*|[Ll][Bb])*)*(\s\(.*\)\s)*(\sde*d\'*\s)*(.*\n)")
        m2= p2.search(line)
        if m2 is not None:
            fileext.write(nb_ligne.__str__() + ": QUANTITÉ:" + m2.group(1)+"\n")
            fileext.write(nb_ligne.__str__()+ " :INGRÉDIENT:" + m2.group(13)+"\n")

  #          if m2.group(2) is not None:  #MESURE UNITÉ INGRÉDIENT
  #              print("QUANTITÉ:"+m2.group(1))
  #              print ("INGRÉDIENT:"+m2.group(2))
  #          else:                            # MESURE INGRÉDIENT
  #              print("QUANTITÉ:"+m2.group(0))
  #              print ("INGRÉDIENT:"+m2.group(1))
        else:
            print("BB-----------------------------------------------------")
            fileext.write(nb_ligne.__str__() + ": QUANTITÉ:"+"\n")
            fileext.write(nb_ligne.__str__() + ": INGRÉDIENT:" + line + "\n")
    nb_ligne = nb_ligne + 1
file.close()
fileext.close()
print(nb_ok.__str__())