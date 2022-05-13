####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Classe Animal
####################################################################################

#Importation

#Import de la classe Enclos
import enclos



#Début de la classe Animal
class Animal:
    """
    Classe Animal
    """

    def __init__(self, p_id_animal = "", p_poid_animal = -1, p_nom_animal ="", p_enclos = enclos.Enclos(), p_regime_animal =""):
        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un animal
        """

        self.__id_animal = p_id_animal
        self.__poid_animal = p_poid_animal
        self.__nom_animal = p_nom_animal
        self.Enclos = p_enclos
        self.Regime_animal = p_regime_animal

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    #Accesseur id_animal

    def _get_id_animal(self) -> str:
        """
        Accesseur de id_animal
        :return: str
        """

        return self.__id_animal
    #Mutateur id_animal
    def _set_id_animal(self, p_id_animal) -> None:
        """
        Mutateur de id_animal
        :return: None
        """
        if p_id_animal.isnumeric():
            if len(p_id_animal) == 7:
                self.__id_animal = p_id_animal

    #Propriétés de id_animal

    Id_animal = property(_get_id_animal,_set_id_animal)
    ########

    #Accesseur poid_animal

    def _get_poid_animal(self) -> float:
        """
        Accesseur de poid_animal
        :return: float
        """
        return self.__poid_animal

    #Mutateur poid_animal

    def _set_poid_animal(self, p_poid_animal) -> None:
        """
        Mutateur de poid_animal
        :return: None
        """
        if p_poid_animal > 0:
            self.__poid_animal = p_poid_animal

    #Propriétés de poid_animal

    Poid_animal = property(_get_poid_animal,_set_poid_animal)
    #########

    #Accesseur nom_animal

    def _get_nom_animal(self) -> str:
        """
        Accesseur de nom_animal
        :return: str
        """
        return self.__nom_animal

    #Mutateur de nom_animal

    def _set_nom_animal(self, p_nom_animal:str)  -> None:
        """
        Mutateur de nom_animal
        :return: none
        """
        if str(p_nom_animal).isalpha():
            self.__nom_animal = p_nom_animal

    #Propriétés de nom_animal

    Nom_animal = property(_get_nom_animal, _set_nom_animal)
    #########


