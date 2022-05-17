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
         Vérifie si l'étudiant existe dans la liste des étudiants
             :param p_Id:  le numéro d'étudiant
             :return: True si l'étudiant est trouvé dans la liste des étudiants et False sinon
    """
    for ecl in Ls_Enclos:
        if ecl.Id_enclos == p_Id_enclos:
            return True
    return False



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
        # Entrée de donnée pour les attributs de l'objet Etudiant
        enclos.Id_enclos = self.lineEdit_id_enclos.text()
        enclos.Habitat_naturel = self.comboBox_habitat_enclos.currentText()
        enclos.Dimension = self.comboBox_dimension_enclos.currentText()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_enclos = verifier_Id_enclos_liste(enclos.Id_enclos)
        if verifier_enclos is False:
            print("verif")

            # Ajouter l'objet instancié à la liste des enclos
            Ls_Enclos.append(enclos)
            print("Wow")
            # Réinitialiser les lineEdits du nom, du numéro d'étudiant et du dateEdit
            self.lineEdit_id_enclos.clear()

        else:
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            self.lineEdit_id_enclos.clear()
            self.label_err_id_enclos.setVisible(True)
            # Réinitialiser les lineEdits du nom, du numéro d'étudiant et du dateEdit
            self.lineEdit_id_enclos.clear()

        print("Wow2")
        print(Ls_Enclos)
        # Préparer la listview
        model = QStandardItemModel()
        self.listView_enclos.setModel(model)
        for cls in Ls_Enclos:
            item = QStandardItem(cls.Id_enclos+" * "+cls.Habitat_naturel + " * " + cls.Dimension )
            model.appendRow(item)

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_quitter_enclos_clicked(self):
        """
        Méthode du bouton Menu principal pour fermer le popup
        :return: None
        """
        self.close()


