####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_Mammifere
####################################################################################

#importation outils PyQt5
from PyQt5 import QtWidgets

#importation de l'interface
from PyQt5.QtCore import pyqtSlot

from Interface import InterfaceMammifere7


#Import de la classe Mammifere
from enclos import Enclos
from mammifere import *

Enclos1 =Enclos()
#Instanciation de mammifere

Mam1 = Mammifere("1234567", 25, "Chien", Enclos1, "Carnivore", "Bleu", 15)

######################################################
###### DÉFINITIONS DE LA CLASSE popup_Mammifere ######
######################################################

class PopUpMammifere(QtWidgets.QDialog, InterfaceMammifere7.Ui_Mammifere):
    def __init__(self, parent=None):
        super(PopUpMammifere, self).__init__(parent)
        self.setupUi(self)

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_cancel_mammifere_clicked(self):
        """
        Méthode du bouton cancel pour fermer le popup
        :return: None
        """
        self.close()

    #Test des set
    Mam1.Temps_de_gestation = -1
    Mam1.Couleur_mammifere = "blou"
    Mam1.Regime_animal = "carnivore"
    Mam1.Id_animal = "adw"
    Mam1.Poid_animal = -1
    Mam1.Nom_animal = 22

#Test de sérialisation
    #Mam1.serialiser("a")

    Mam1.deserialiser("a", Enclos1)

    print(Mam1.__dict__)

