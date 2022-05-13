####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Classe Enclos
####################################################################################

class Enclos:
    """
    Classe Enclos
    """

    def __init__(self, p_habitat_naturel = "", p_Dimension = "", p_id_enclos = "", p_Ls_animaux = []):
        """
        Méthode constructeur
        Définition des attributs de la classe Enclos
        """

        self.Habitat_naturel = p_habitat_naturel
        self.Dimension = p_Dimension
        self.__id_enclos = p_id_enclos
        self.Ls_animaux = p_Ls_animaux

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété id_enclos

    def _get_id_enclos(self) -> str:
        """
        Accesseur de l'attribut privé id_enclos
        return: str
        """
        return self.__id_enclos

    def _set_id_enclos(self, p_id_enclos) -> None:
        """
        Mutateur de l'attribut privé id_enclos
        return: none
        """
        if p_id_enclos.isnumeric():
            if len(p_id_enclos) == 7:
                self.__id_enclos = p_id_enclos

    Id_enclos = property(_get_id_enclos,_set_id_enclos)
