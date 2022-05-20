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

#Import enclos
import enclos

# Début de la classe
class Mammifere(Animal):
    """
    Classe Mammifère
    """

    def __init__(self,p_id_animal = "", p_poid_animal = -1, p_nom_animal ="", p_enclos = enclos.Enclos(), p_regime_animal ="", p_couleur_mammifere = "", p_temps_de_gestation = -1, ):

        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un mammifère
        """
        Animal.__init__(self, p_id_animal, p_poid_animal, p_nom_animal, p_enclos, p_regime_animal)
        self.Couleur_mammifere = p_couleur_mammifere
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




    ############################################
    #####          Autres MÉTHODES         #####
    ############################################

    # Code pris de l'exercice cours et adapter pour le projet synthèse
    # Méthode sérialiser
    def serialiser(self,p_fichier):
        """
           Méthode permttant de sérialiser un objet de la classe Mammifere
           ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
           :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
                       1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """




        self.__dict__['Enclos']=str(enclos.Enclos)

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

    def deserialiser(self, p_fichier, ):
        """
            Méthode permttant de désérialiser un objet de la classe mammifere
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
            ::param p_enclos  : Le
                """

        with open(p_fichier, "r") as fichier:
            self.__dict__ = json.load(fichier)

