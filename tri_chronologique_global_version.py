from os import walk
import os.path, time
from time import localtime, strftime
import shutil
import os

firsttime=str(input("first time ?(y/n)"))
Frequency=str(input("do you want to sort your files at regular frequency?(y/n)"))
if Frequency=="y":
    wahttime=int(input("What is the frequency? (in seconds)"))
if firsttime=="y":
    folder=str(input("In which folder do you want to store your data? (the absolute path with '/' and not antislash)"))
    if "/" not in folder:
        print("with SLASH and not antislash")
        folder=str(input("In which folder do you want to store your data? (the absolute path with '/' and not antislash)"))
    ouverture=open("folder.txt", "w")
    ouverture.write(folder)
    ouverture.close()
else:
    ouverture=open("folder.txt", "r")
    folder=ouverture.read()
    ouverture.close()



def creation_dossier(folder):

    Today_Date=strftime("%m-%d-%Y", localtime())
    if not os.path.exists(folder+"/"+Today_Date):
        os.makedirs(folder+"/"+Today_Date)
        os.makedirs(folder+"/"+Today_Date+"/Videos")
        os.makedirs(folder+"/"+Today_Date+"/3D Objects")
        os.makedirs(folder+"/"+Today_Date+"/Musics")
        os.makedirs(folder+"/"+Today_Date+"/Pictures")
        os.makedirs(folder+"/"+Today_Date+"/Documents")
        os.makedirs(folder+"/"+Today_Date+"/Others")
        os.makedirs(folder+"/"+Today_Date+"/Folders")
    listeFichiers=[]
    for (repertoire, sousRepertoires, fichiers) in walk(folder+"/"+Today_Date):
        listeFichiers.extend(fichiers)
    nom_fichier="Historique_"+Today_Date+".txt"
    if nom_fichier not in listeFichiers:
        ouv=open(folder+"/"+Today_Date+"/Historique_"+Today_Date+".txt", "x")
        ouv.close()


def obtenir_date_fichier(chemin,fichier,date_fichier2):
    date_fichier=time.ctime(os.path.getmtime(chemin+fichier))
    date_fichier1=date_fichier.split(" ")
    for i in date_fichier1:
        if i=="":
            date_fichier1.remove(i)
    strV=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    intV=["01","02","03","04","05","06","07","08","09","10","11","12"]
    mois=date_fichier1[1]
    for i in strV:
        if i==mois:
            ai=strV.index(i)
            mois=intV[ai]
    jour=date_fichier1[2]
    annee=date_fichier1[-1]
    date_fichier2=mois+"-"+jour+"-"+annee
    return date_fichier2



def chronological_file_sort():
    UserN=os.getenv("USERNAME")
    chemin1,chemin2,chemin3,chemin4,chemin5,chemin6,chemin7="C:/Users/"+UserN+"/Music/","C:/Users/"+UserN+"/Videos/","C:/Users/"+UserN+"/Downloads/","C:/Users/"+UserN+"/3D Objects/","C:/Users/"+UserN+"/Desktop/","C:/Users/"+UserN+"/Pictures/","C:/Users/"+UserN+"/Documents/"
    Today_Date=strftime("%m-%d-%Y", localtime())
    listeFichiers = []
    ouv=open(folder+"/"+Today_Date+"/Historique_"+Today_Date+".txt", "a")
    ouv.write("\n \n Nouveau tri=========================================================\n \n")
    chemin_dacces=[chemin1,chemin2,chemin3,chemin4,chemin5,chemin6,chemin7]
    for chemin in chemin_dacces:
        for (repertoire, sousRepertoires, fichiers) in walk(chemin):
            listeFichiers.extend(fichiers)


            for fichier in listeFichiers:
                date_fichier2=""
                date_fichier2=obtenir_date_fichier(chemin,fichier,date_fichier2)
                if date_fichier2==Today_Date:
                    fichier2=fichier.split(".")
                    fichier2=fichier2[-1]

                    documents_formats=["txt","odt","doc","docx","pdf","pur"]
                    images_formats=["jpg","jpeg","png","gif","psd"]
                    videos_formats=["mp4","mov","avi","mkv","MP4"]
                    audio_formats=["mp3","wav","aif","ogg","flac"]
                    ThreeD_formats=["obj","mtl","fbx","c4d","mb","ZPR"]


                    if fichier2 in documents_formats:
                        shutil.copy(chemin+fichier, folder+"/"+Today_Date+"/Documents")
                    elif fichier2 in videos_formats:
                        shutil.copy(chemin+fichier, folder+"/"+Today_Date+"/Videos")
                    elif fichier2 in audio_formats:
                        shutil.copy(chemin+fichier, folder+"/"+Today_Date+"/Musics")
                    elif fichier2 in ThreeD_formats:
                        shutil.copy(chemin+fichier, folder+"/"+Today_Date+"/3D Objects")
                    elif fichier2 in images_formats:
                        shutil.copy(chemin+fichier, folder+"/"+Today_Date+"/Pictures")
                    else:
                        shutil.copy(chemin+fichier, folder+"/"+Today_Date+"/Others")
                    ouv.write("\n"+fichier)
            listeFichiers=[]
            break

    ouv.close()


def chronological_folder_sort(folder):
    Today_Date=strftime("%m-%d-%Y", localtime())
    folder3=folder.split("/")
    folder3=folder3[-1]
    UserN=os.getenv("USERNAME")
    chemin1,chemin2,chemin3,chemin4,chemin5,chemin6="C:/Users/"+UserN+"/Music/","C:/Users/"+UserN+"/Videos/","C:/Users/"+UserN+"/Downloads/","C:/Users/"+UserN+"/3D Objects/","C:/Users/"+UserN+"/Desktop/","C:/Users/"+UserN+"/Pictures/"
    Today_Date=strftime("%m-%d-%Y", localtime())
    listeFichiers2=[]
    ouv=open(folder+"/"+Today_Date+"/Historique_"+Today_Date+".txt", "a")
    chemin_dacces=[chemin1,chemin2,chemin3,chemin4,chemin5,chemin6]
    for chemin in chemin_dacces:
        for (repertoire, sousRepertoires, fichiers) in walk(chemin):
            listeFichiers2.extend(sousRepertoires)
            for folder2 in listeFichiers2:
                print(folder2)
                date_folder2=""
                date_folder2=obtenir_date_fichier(chemin,folder2,date_folder2)
                if os.path.exists(folder+"/"+Today_Date+"/Folders/"+folder2):
                    try:
                        shutil.rmtree(folder+"/"+Today_Date+"/Folders/"+folder2)
                    except PermissionError:
                        shutil.rmtree(folder+"/"+Today_Date+"/Folders/"+folder2)
                if date_folder2==Today_Date:
                    if folder2!=folder3:
                        if folder2!="Screenshots":
                            ouv.write("\n"+folder2)
                            shutil.copytree(chemin+folder2, folder+"/"+Today_Date+"/Folders/"+folder2)
                            print("dates correspondantes")
            listeFichiers2=[]
            break


creation_dossier(folder)

if Frequency=="y":
    op=1
    while op==1:
        op=0
        chronological_file_sort()
        chronological_folder_sort(folder)
        time.sleep(wahttime)
        op=1
else:
    chronological_file_sort()
    chronological_folder_sort(folder)

