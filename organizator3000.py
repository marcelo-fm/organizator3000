
import os, shutil

#print(os.getcwd())

def lista_arquivos(path=os.getcwd()):
    extensoes = {}
    arquivos = os.listdir(path)
    folder = []
    for i in range(len(arquivos)):
        if os.path.isdir(arquivos[i]):
            folder.append(arquivos[i])
            del arquivos[i]
            

