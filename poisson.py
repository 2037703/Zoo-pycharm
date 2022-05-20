####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Classe Poisson
####################################################################################


#Importation
#import la classe animal
import enclos
from animal import Animal

#import json
import json

class Poisson(Animal):
    """
    Class Poisson
    """

    def __init__(self,p_id_animal = "", p_poid_animal = -1, p_nom_animal ="", p_enclos = enclos.Enclos(), p_regime_animal ="", p_longueur_poisson = -1, p_machoire_dente = ""):

        """
        Méthode de type Constructeur avec paramètres et valeurs par défaut
        Définition des attributs d'un Oiseau
        """
        Animal.__init__(self, p_id_animal, p_poid_animal, p_nom_animal, p_enclos, p_regime_animal)
        self.__longueur_poisson = p_longueur_poisson
        self.Machoire_dente = p_machoire_dente

        ##################################################
        ####   Propriétés, accesseurs et mutateurs    ####
        ####                                          ####
        ##################################################

        # Accesseur de l'attribut longueur_poisson

    def _get_longueur_poisson(self) -> float:

        """
        Accesseur longueur_poisson
        :return: float
        """

        return self.__longueur_poisson
        # Mutateur de l'attribut longueur_poisson

    def _set_longueur_poisson(self, p_longueur_poisson) -> None:

        """
        Mutateur longueur_poisson
        :return: None
        """
        if p_longueur_poisson > 0:
            self.__longueur_poisson = p_longueur_poisson

        # Propriétés de l'attribut longueur_poisson

    Longueur_poisson = property(_get_longueur_poisson, _set_longueur_poisson)


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
                 "   Le nom de l'étudiant : "+str(self.Poid_animal)+"\n"+\
                "   Le programme de l'étudiant : "+self.Nom_animal+"\n"+\
                 "   La date de naissance de l'étudiant : "+str(self.enclos.Id_enclos) +"\n" +\
                 "  Le regime de l'animal "+ self.regime_animal+"\n" + \
                "  La couleur du mammifère " + str(self.Longueur_poisson) + "\n" + \
                "   Le casier de l'étudiant : " + self.machoire_dente + "\n\n" +"*"*60
        return chaine

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
        self.__dict__["Enclos"]=str(self.Enclos.Id_enclos)

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