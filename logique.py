####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Sert à stocker les listes
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
#Importation des animal
import mammifere
import poisson
import oiseau

Ls_Enclos = []

Ls_Animal_animal = []


Dict_animal = {type(mammifere.Mammifere()) : "Mammifère"
                , type(poisson.Poisson()) : "Poisson"
                , type(oiseau.Oiseau()) : "Oiseau" }

