####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Classe mammifere
####################################################################################

#Importation

#Import json
import json

# Import animal
from animal import Animal
# Début de la classe

class Mammifere(Animal):
    """
    Classe Mammifère
    """

    def __init__(self, p_couleur_mammifere = "", p_temps_de_gestation = -1):

        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un mammifère
        """
        self.couleur_mammifere = p_couleur_mammifere
        self.__temps_de_gestation = p_temps_de_gestation

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Accesseur de l'attribut temps_de_gestation

    def _get_temps_de_gestation(self) -> float:

        """
        Accesseur temps_de_gestation
        :return: float
        """

        return self.__temps_de_gestation

    # Mutateur de l'attribut temps_de_gestation

    def _set_temps_de_gestation(self, p_temps_de_gestation) -> None:

        """
        Mutateur temps_de_gestation
        :return: None
        """

        if p_temps_de_gestation > 0:
            self.__temps_de_gestation = p_temps_de_gestation

    # Propriétés de l'attribut temps_de_gestation

    Temps_de_gestation = property(_get_temps_de_gestation, _set_temps_de_gestation)

    #############




    ############################################
    #####          Autres MÉTHODES         #####
    ############################################
    # Code pris de l'exercice cours et adapter pour le projet synthèse
    # Méthode sérialiser
    def serialiser(self, p_fichier):
        """
           Méthode permttant de sérialiser un objet de la classe Etudiant
           ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
           :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """
        self.__dict__["_Animal_enclos"]=str(self.Enclos.Id_enclos)

        try:
            with open(p_fichier , "w") as fichier:
                try:
                    #json.dump(self.__dict__, fichier)
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2