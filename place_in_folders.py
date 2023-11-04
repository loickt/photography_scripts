import os
inputStr= input(r"collez ici l'adresse")
rename= input(r"Renommer ? (1/0)")
files=os.listdir(inputStr)
files.sort()

file_counts = {}

def create_folder(ext, inputString):
    if not os.path.exists(inputString+"/"+ext):
        os.mkdir(inputString+"/"+ext)
    return 0 # first iteration set to false

for file in files:
    file_extension=file[-3:]
    
    if file_extension in file_counts:
        file_counts[file_extension] += 1
    else:
        create_folder(file_extension,inputStr)
        file_counts[file_extension] = 1
    if rename==1:
        os.rename(inputStr+"/"+file, inputStr+'/'+file_extension+"/"+str(file_counts.get(file_extension, 0))+"."+file_extension)
    else:
        os.rename(inputStr+"/"+file, inputStr+'/'+file_extension+"/"+file)
