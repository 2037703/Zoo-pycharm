####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################

# Importer Pour le model de la listView
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

#Import les boite de dialog
from Popup_Animal import *
from Popup_Enclos import *
#Import les interface graphique
from Interface import InterfaceMenu

#import
import sys
########################################################
###### DÉFINITIONS DE LA CLASSE Menu ######
########################################################

# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)          # Nom de mon fichier ui
class Menu(QtWidgets.QMainWindow, InterfaceMenu.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfaceMain.Ui_MainWindow : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfaceMain.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(Menu, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Menu principale")

    #Boutton ouvrir Animal
    @pyqtSlot()
    def on_button_Animal_main_clicked(self):
        """
        Méthode du bouton cours pour ouvrir la fenêtre de dialogue PopUpAnimal
        """
        # Instancier une boite de dialogue
        dialog_Animal = PopUpAnimal()
        #Afficher la boite de dialogue
        dialog_Animal.show()
        dialog_Animal.exec_()



    #Boutton ouvrir Enclos
    @pyqtSlot()
    def on_button_Enclos_main_clicked(self):
        """
        Méthode du bouton Enclos pour ouvrir la fenêtre de dialogue PopUpEnclos
        """
        # Instancier une boite de dialogue
        dialog_Enclos = PopUpEnclos()
        #Afficher la boite de dialogue
        dialog_Enclos.show()
        dialog_Enclos.exec_()

    #Boutton ouvrir Enclos
    @pyqtSlot()
    def on_button_Quitter_main_clicked(self):
        """
        Méthode du bouton Quitter pour fermer le programme
        :return: None
        """
        self.close()
#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Créer le main qui lance la fenêtre de Qt

def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = Menu()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()














