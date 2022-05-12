####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_animal
####################################################################################

######################################################
###### DÉFINITIONS DE LA CLASSE popup_animal ######
######################################################
#Import d'outil PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

#importation de l'interface
from Interface import InterfaceAnimal3

#Importation des fenêtre de dialog

from Popup_Mammifere import *

class PopUpAnimal(QtWidgets.QDialog, InterfaceAnimal3.Ui_Dialog):
    def __init__(self, parent=None):
        super(PopUpAnimal, self).__init__(parent)
        self.setupUi(self)


    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_quitter_animal_clicked(self):
        """
        Méthode du bouton Menu principal pour fermer le popup
        :return: None
        """
        self.close()

    # Boutton pour ouvrir les création d'animaux  au menu principale
    @pyqtSlot()
    def on_Button_Choisir_animal_clicked(self):
        """
        Boutton qui ouvre les popup de création d'animaux
        :return: None
        """

        # Instancier une boite de dialogue
        dialog_Mammifere = PopUpMammifere()
        dialog_Oiseau = Pop
        #Afficher la boite de dialogue
        dialog_Mammifere.show()
        dialog_Mammifere.exec_()