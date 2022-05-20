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
import enclos
from animal import Animal

#Import json

import json

class Oiseau(Animal):
    """
    Class Oiseau
    """

    def __init__(self,p_id_animal = "", p_poid_animal = -1, p_nom_animal ="", p_enclos = enclos.Enclos(), p_regime_animal ="", p_couleur_plumage = "", p_grandeur_oiseau = -1):

        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un Oiseau
        """
        Animal.__init__(self, p_id_animal, p_poid_animal, p_nom_animal, p_enclos, p_regime_animal)
        self.Couleur_plumage = p_couleur_plumage
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
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    # Inspirer de Hasna Hocini
    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine = " "*60+"\n"+"*"*60+"\n\n"+"   L'id de l'animal' : "+str(self.Id_animal)+"\n"+\
                 "   Le poid de l'animal : "+str(self.Poid_animal)+"\n"+\
                "   Le nom de l'animal : "+self.Nom_animal+"\n"+\
                 "  L'id de l'enclos : "+str(self.enclos.Id_enclos) +"\n" +\
                 "  Le regime de l'animal "+ self.regime_animal+"\n" + \
                "  La couleur du plumage " + self.Couleur_plumage + "\n" + \
                "   La grandeur du oiseau : " + self.Grandeur_oiseau + "\n" +"*"*60
        return chaine




