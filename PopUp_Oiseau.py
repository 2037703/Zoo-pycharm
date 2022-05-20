####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_Oiseau
####################################################################################
#Import Logique
from logique import Ls_Animal_animal, Dict_animal

#importation outils PyQt5
from PyQt5 import QtWidgets

#importation de l'interface
from PyQt5.QtCore import pyqtSlot

from Interface import InterfaceOiseau7

#import classe
from oiseau import Oiseau
#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

# Code pris de l'exercice cours
def verifier_id_animal_liste(p_id):
    """
         Vérifie si l'id de l'animal existe dans la liste des oiseau
             :param p_num:  l'id de l'animal
             :return: True si l'id est trouvé dans la liste des oiseau sinon false
    """
    for id in Ls_Animal_animal:
        if id.Id_animal == p_id.capitalize():
            return True
    return False


def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_err_grandeur_ois.setVisible(False)
    objet.label_err_id_ois.setVisible(False)
######################################################
###### DÉFINITIONS DE LA CLASSE popup_Oiseau    ######
######################################################



class PopUpOiseau(QtWidgets.QDialog, InterfaceOiseau7.Ui_Dialog):
    def __init__(self,p_popupOiseau, parent=None):
        super(PopUpOiseau, self).__init__(parent)
        self.setupUi(self)
        self.popupOiseau = p_popupOiseau
        cacher_labels_erreur(self)

    # Boutton ajouter pour créer un poisson
    @pyqtSlot()
    def on_button_ajout_ois_clicked(self):
        """
        Méthode du bouton creer pour créer et ajouter un poisson à la liste view
        :return:
        """

        ois = Oiseau()

        success = True
        # Entrée de donnée pour les attributs de l'objet mammifere


        ois.Grandeur_oiseau = self.doubleSpinBox_grandeur_oiseau.value()
        print(ois.Grandeur_oiseau)
        if ois.Grandeur_oiseau == -1:
            self.label_err_grandeur_ois.setVisible(True)
            success = False
        ois.Couleur_plumage = self.comboBox_couleur_oiseau.currentText()
        ois.Id_animal = self.popupOiseau.lineEdit_id_animal.text()
        ois.Nom_animal = self.popupOiseau.lineEdit_nom_animal.text()
        ois.Poid_animal = float(self.popupOiseau.lineEdit_poid_animal.text())
        ois.Enclos = self.popupOiseau.comboBox_enclos_animal.currentText()
        ois.Regime_animal = self.popupOiseau.comboBox_regime_animal.currentText()

        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des oiseau
        verif_id = verifier_id_animal_liste(ois.Id_animal)

        if verif_id == True:
            success = False
            self.label_err_id_ois.setVisible(True)


        # Ajouter l'objet instancié à la liste des enclos
        if success == True:
            Ls_Animal_animal.append(ois)


    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_oiseau_cancel_clicked(self):
        """
        Méthode du bouton cancel pour fermer le popup
        :return: None
        """
        self.close()


