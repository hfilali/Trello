#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:44:19 2018

@author: hadil filali
"""
import re
import sys

if len(sys.argv) < 2:
    print("Indiquer en paramètre l'export csv Trello à traiter")
    sys.exit(1)
filename = sys.argv[1]

#filename = "./Trello/vivier-dev.csv"
export_Trello = open(filename, "r")

# Creaton du fichier de résultat
output_file = open("./Export/resultat.csv", "w")

# Variables globales
nb_carte = 0
b_begin = True
consultant = "Hadil Filali"
profil = ""
candidat = ""
linkedin = ""
statut = "En process"
sep = ";"

# Pattern pour identifier le début d'une carte Trello
url_carte = "https://trello.com/c/"
url_linkedin = "linkedin.com"

# Lecture de l'export Trello ligne par ligne
for line in export_Trello:
    
    if (line.find(url_carte) > 0) and (re.match("^[a-zA-Z0-9]+",line)):
        if b_begin == False:
            #print(consultant + sep + profil + sep + sep + candidat + sep + sep + linkedin + sep + sep + sep + statut)
            output_file.write(consultant + sep + profil + sep + sep + candidat + sep + sep + sep + linkedin + sep + sep + sep + statut + "\n")
            profil = ""
            candidat = ""
            linkedin = ""
        b_begin = False
        nb_carte += 1
        candidat = ((line.split(",")[1]).split("(")[0]).strip()
        if re.match("^\"",candidat):
            candidat = candidat[1:]
        debut_desc = (re.search(r"\(",line)).end()
        fin_desc = (re.search(r"\)",line)).start()
        description = line[int(debut_desc):int(fin_desc)]
        profil = (description.split("|")[0]).strip()
    
    if line.find(url_linkedin) > 0:
        debut_url = (re.search(r"http",line)).start()
        line = line[int(debut_url):]
        linkedin = line.split(",")[0]
        if re.search("\"",linkedin):
            linkedin = linkedin[0:-1]
        linkedin = linkedin.rstrip()

#print(consultant + sep + profil + sep + sep + candidat + sep + sep + linkedin + sep + sep + sep + statut)
output_file.write(consultant + sep + profil + sep + sep + candidat + sep + sep + sep + linkedin + sep + sep + sep + statut)
print("[success] : " + str(nb_carte) + " candidats exportés :)")
#Fermeture des fichiers
export_Trello.close
output_file.close
