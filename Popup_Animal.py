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
from Interface import InterfaceAnimal7

#Importation des fenêtre de dialog

from Popup_Mammifere import *
from PopUp_Poisson import *
from PopUp_Oiseau import *



# Classe
class PopUpAnimal(QtWidgets.QDialog, InterfaceAnimal7.Ui_Dialog):
    """
    Classe PopUpAnimal
    """
    def __init__(self, parent=None):
        super(PopUpAnimal, self).__init__(parent)
        self.setupUi(self)

    # Boutton pour ouvrir les création d'animaux  au menu principale


    @pyqtSlot()
    def on_Button_Choisir_animal_clicked(self):
        """
        Boutton qui ouvre les popup de création d'animaux
        :return: None
        """
        if self.comboBox_Animal.currentText() == "Mammifère":
            # Instancier une boite de dialogue
            dialog_Mammifere = PopUpMammifere()
            #Afficher la boite de dialogue
            dialog_Mammifere.show()
            dialog_Mammifere.exec_()

        elif self.comboBox_Animal.currentText() == "Poisson":

         # Instancier une boite de dialogue
            dialog_Poisson = PopUpPoisson()

            dialog_Poisson.show()
            dialog_Poisson.exec_()


        elif self.comboBox_Animal.currentText() == "Oiseau":
            # Instancier une boite de dialogue
            dialog_Oiseau = PopUpOiseau()

            dialog_Oiseau.show()
            dialog_Oiseau.exec_()

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_quitter_animal_clicked(self):
        """
        Méthode du bouton Menu principal pour fermer le popup
        :return: None
        """
        self.close()

