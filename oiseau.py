####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Classe Oiseau
####################################################################################

# Importation

#Importation de la classe Animal
from animal import Animal

#Import json

import json

class Oiseau(Animal):
    """
    Class Oiseau
    """

    def __init__(self, p_couleur_plumage = "", p_grandeur_oiseau = -1):

        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un Oiseau
        """

        self.couleur_plumage = p_couleur_plumage
        self.__grandeur_oiseau = p_grandeur_oiseau

        ##################################################
        ####   Propriétés, accesseurs et mutateurs    ####
        ####                                          ####
        ##################################################

        # Accesseur de l'attribut grandeur_oiseau

    def _get_grandeur_oiseau(self) -> float:
        """
        Accesseur grandeur_oiseau
        :return: float
        """

        return self.__grandeur_oiseau

        # Mutateur de l'attribut grandeur_oiseau

    def _set_grandeur_oiseau(self, p_grandeur_oiseau) -> None:

        """
        Mutateur grandeur_oiseau
        :return: None
        """
        if p_grandeur_oiseau > 0:
            self.__grandeur_oiseau = p_grandeur_oiseau

        # Propriétés de l'attribut grandeur_oiseau

    Grandeur_oiseau = property(_get_grandeur_oiseau, _set_grandeur_oiseau)

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

    # Méthode désérialiser

    def deserialiser(self, p_fichier, p_enclos):
        """
            Méthode permttant de désérialiser un objet de la classe Etudiant
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
                """

        with open(p_fichier, "r") as fichier:
            self.__dict__ = json.load(fichier)

        self.enclos = p_enclos