####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_enclos
####################################################################################

#importation outils PyQt5
from PyQt5 import QtWidgets

#importation de l'interface
from PyQt5.QtCore import pyqtSlot

from Interface.InterfaceMenu import *
from Interface import InterfaceEnclos3
######################################################
###### DÉFINITIONS DE LA CLASSE popup_enclos ######
######################################################

class PopUpEnclos(QtWidgets.QDialog, InterfaceEnclos3.Ui_Dialog):
    def __init__(self, parent=None):
        super(PopUpEnclos, self).__init__(parent)
        self.setupUi(self)

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_quitter_enclos_clicked(self):
        """
        Méthode du bouton Menu principal pour fermer le popup
        :return: None
        """
        self.close()

