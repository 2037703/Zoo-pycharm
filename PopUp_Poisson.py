####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_Poisson
####################################################################################

#importation outils PyQt5
from PyQt5 import QtWidgets

#importation de l'interface
from PyQt5.QtCore import pyqtSlot

from Interface import InterfacePoisson7

#Import de classes
from enclos import *
from poisson import Poisson

#Instanciation d'un enclos

Enclos2 = Enclos()
# Instanciation d'un poisson

poiss1 = Poisson("1234537", 25, "Brochet", Enclos2, "Carnivore", 15, "Oui")
######################################################
###### DÉFINITIONS DE LA CLASSE popup_Poisson    ######
######################################################

class PopUpPoisson(QtWidgets.QDialog, InterfacePoisson7.Ui_Dialog):
    def __init__(self, parent=None):
        super(PopUpPoisson, self).__init__(parent)
        self.setupUi(self)

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_cancel_poisson_clicked(self):
        """
        Méthode du bouton cancel pour fermer le popup Poisson
        :return: None
        """
        self.close()

    # Test de sérialisation
    #poiss1.serialiser("a2")
    poiss1.deserialiser("a2", Enclos2)

    print(poiss1.__dict__)