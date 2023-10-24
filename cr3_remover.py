import os
import shutil
print("\n\nS'assurer que aucune photo ait été prise juste en raw")
inputStr= input(r"collez l'adresse, suppression définitive !")

files=os.listdir(inputStr)
files.sort()
rm=0
for i in range (len(files)):
    if files[i][-4:]==".CR3":
        if files[i][:-4]+".JPG" not in files:
            rm+=1
            os.remove(inputStr+"/"+files[i])
print(str(rm)+" fichier" + "s"*(rm>1)+" supprimé" + "s"*(rm>1))
