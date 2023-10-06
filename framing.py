# il reste deux  mais ça marche alors ...

from pathlib import Path
import PIL
import os
from PIL import Image, ImageDraw
print("Collez l'adresse ici :")
inputStr= input(r" -  ")

bordEnPct = 2.5
definition=3000

def reduce(input,output,file,fond,PctBord):
    dimFond = fond.size[0]  #fond carré
    tailleImageFinale = dimFond - (2*PctBord)*dimFond

    imgAddr = input+"/"+file

    img = Image.open(imgAddr)
    width, height = img.size
    if width<height :
         img = img.resize((int(width*tailleImageFinale//height),int(tailleImageFinale)))
    else:
         img = img.resize((int(tailleImageFinale),int(height*tailleImageFinale//width)))
    return img

def overlay(fond,image):
    dimFond = fond.size[0]  #fond carré
    width, height = image.size
    if width<dimFond and height<dimFond:
        left=(dimFond-width)//2
        lower=(dimFond-height)//2
        corner=(left,lower)
        fond.paste(image,corner)
        return fond
    else:
        print("erreur dimension overlay")

def frame_generator(inputStr,definition,bordEnPct):

    path = Path("%s" %inputStr)
    parent_folder=str(path.parent.absolute())
    outputStr=parent_folder+'\\'+os.path.basename(path)+' cadré'
    #outputStr=inputStr+'/cadré'
    if not os.path.exists(outputStr):
        os.mkdir(outputStr)

    input = r'%s'%inputStr
    output = r'%s'%outputStr
    counter = 0
    for file in os.listdir(input):
        if file[-3:]=="jpg" or file[-3:]=="JPG":
            outputImgAddr = output+"/"+file
            if not os.path.exists(outputImgAddr):
                fond = img = Image.new('RGB', (definition, definition), color = 'white')
                img=reduce(input,output,file,fond,bordEnPct/100)
                
                fond=overlay(fond,img)
                fond.save(outputImgAddr)
                print("Framed : "+file)
                counter+=1
        else:
            frame_generator(inputStr+"/"+file,definition,bordEnPct)
    print(str(counter)+" picture"+"s"*(counter!=1)+" framed")


inputStr=inputStr.replace('\\', "/")
frame_generator(inputStr,definition,bordEnPct)