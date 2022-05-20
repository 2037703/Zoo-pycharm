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

#Import logique
from logique import Ls_Animal_animal, Dict_animal
#Import de classes
from enclos import *
from poisson import Poisson

#Instanciation d'un enclos

Enclos2 = Enclos()
# Instanciation d'un poisson

poiss1 = Poisson("1234537", 25, "Brochet", Enclos2, "Carnivore", 15, "Oui")


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

# Code pris de l'exercice cours
def verifier_id_animal_liste(p_id):
    """
         Vérifie si l'id de l'animal existe dans la liste des mammifere
             :param p_num:  l'id de l'animal
             :return: True si l'id est trouvé dans la liste des mammifere sinon false
    """
    for id in Ls_Animal_animal:
        if id.Id_animal == p_id.capitalize():
            return True
    return False

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_err_longueur_poisson.setVisible(False)
    objet.label_err_id_poiss.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE popup_Poisson    ######
######################################################

class PopUpPoisson(QtWidgets.QDialog, InterfacePoisson7.Ui_Dialog):
    def __init__(self,p_popupPoisson, parent=None):
        super(PopUpPoisson, self).__init__(parent)
        self.setupUi(self)
        self.popupPoisson = p_popupPoisson
        cacher_labels_erreur(self)

    # Boutton ajouter pour créer un poisson
    @pyqtSlot()
    def on_button_ajout_poisson_clicked(self):
        """
        Méthode du bouton creer pour créer et ajouter un poisson à la liste view
        :return:
        """
        poiss = Poisson()

        success = True
        # Entrée de donnée pour les attributs de l'objet mammifere


        poiss.Longueur_poisson = self.doubleSpinBox_longueur_poisson.value()
        print(type(poiss.Longueur_poisson))
        print(poiss.Longueur_poisson)
        if poiss.Longueur_poisson == -1:
            self.label_err_longueur_poisson.setVisible(True)
            success = False
        poiss.Machoire_dente = self.comboBox_machoire_poisson.currentText()
        poiss.Id_animal = self.popupPoisson.lineEdit_id_animal.text()
        poiss.Nom_animal = self.popupPoisson.lineEdit_nom_animal.text()
        poiss.Poid_animal = float(self.popupPoisson.lineEdit_poid_animal.text())
        poiss.Enclos = self.popupPoisson.comboBox_enclos_animal.currentText()
        poiss.Regime_animal = self.popupPoisson.comboBox_regime_animal.currentText()

        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des mammifere
        verif_id = verifier_id_animal_liste(poiss.Id_animal)

        if verif_id == True:
            success = False
            self.label_err_id_poiss.setVisible(True)

        # Ajouter l'objet instancié à la liste des enclos
        if success == True:
            Ls_Animal_animal.append(poiss)
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

