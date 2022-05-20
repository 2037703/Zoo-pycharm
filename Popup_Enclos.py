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
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

#importation de l'interface

from Interface.InterfaceMenu import *
from Interface import InterfaceEnclos10

#Importation de la classe Enclos()

from enclos import *

# Importation des listes du fichier logique

from logique import *
#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################
def verifier_Id_enclos_liste(p_Id_enclos):
    """
         Vérifie si l'enclos existe dans la listes des enclos
             :param p_Id:  le numero de l'enclos
             :return: True si l'enclos est dans la liste
    """
    for ecl in Ls_Enclos:
        if ecl.Id_enclos == p_Id_enclos:
            return True
    return False

def model_list_view_animaux(objet):
    # Préparer la listview
    model = QStandardItemModel()
    objet.listView_enclos.setModel(model)
    for cls in Ls_Enclos:
        item = QStandardItem(cls.Id_enclos + " * " + cls.Habitat_naturel + " * " + cls.Dimension)# + " * " + cls.Ls_animaux)
        model.appendRow(item)


def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_err_id_enclos.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE popup_enclos ######
######################################################

class PopUpEnclos(QtWidgets.QDialog, InterfaceEnclos10.Ui_Dialog):
    def __init__(self,  parent=None ):
        super(PopUpEnclos, self).__init__(parent)
        self.setupUi(self)
        cacher_labels_erreur(self)
        model_list_view_animaux(self)

        # #Rendue Ici essaie de transferrer les animaux dans la liste d'enclos
        # for ani in Ls_Animal_animal:
        #     Enclos.Ls_animaux.append(ani.Id_animal)

    # Boutton créer pour créer un enclos
    @pyqtSlot()
    def on_button_creer_enclos_clicked(self):
        """
        Méthode du bouton creer pour créer un enclos
        :return: None
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Eudiant
        enclos = Enclos()
        # Entrée de donnée pour les attributs de l'objet enclos
        enclos.Id_enclos = self.lineEdit_id_enclos.text()
        enclos.Habitat_naturel = self.comboBox_habitat_enclos.currentText()
        enclos.Dimension = self.comboBox_dimension_enclos.currentText()
        # Booleen qui nous informe si le numéro de l'enclos existe ou pas dans la liste des enclos
        verifier_enclos = verifier_Id_enclos_liste(enclos.Id_enclos)
        if verifier_enclos is False:


            # Ajouter l'objet instancié à la liste des enclos
            Ls_Enclos.append(enclos)

            # Réinitialiser les lineEdits du numéro d'enclos
            self.lineEdit_id_enclos.clear()

        else:
            # Effacer le lineEdit du numéro d'enclos et afficher le message d'erreur
            self.lineEdit_id_enclos.clear()
            self.label_err_id_enclos.setVisible(True)
            # Réinitialiser les lineEdits
            self.lineEdit_id_enclos.clear()

        model_list_view_animaux(self)


    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_quitter_enclos_clicked(self):
        """
        Méthode du bouton Menu principal pour fermer le popup
        :return: None
        """
        self.close()


