####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_Oiseau
####################################################################################

#importation outils PyQt5
from PyQt5 import QtWidgets

#importation de l'interface
from PyQt5.QtCore import pyqtSlot

from Interface import InterfaceOiseau7
######################################################
###### DÉFINITIONS DE LA CLASSE popup_Oiseau    ######
######################################################

class PopUpOiseau(QtWidgets.QDialog, InterfaceOiseau7.Ui_Dialog):
    def __init__(self, parent=None):
        super(PopUpOiseau, self).__init__(parent)
        self.setupUi(self)

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_oiseau_cancel_clicked(self):
        """
        Méthode du bouton cancel pour fermer le popup
        :return: None
        """
        self.close()


