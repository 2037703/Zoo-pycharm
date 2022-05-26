####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_animal
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
#Import d'outil PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
#importation de l'interface
from Interface import InterfaceAnimal7

#import des classes

from mammifere import Mammifere
from poisson import Poisson
from oiseau import Oiseau

#Importation des fenêtre de dialog

from Popup_Mammifere import *
from PopUp_Poisson import *
from PopUp_Oiseau import *
import Popup_Mammifere
# import logique
from logique import Ls_Enclos
from logique import Dict_animal
from logique import Ls_Animal_animal

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def model_list_view_animaux(objet):
    # Préparer la listview
    model = QStandardItemModel()
    objet.listView_animal.setModel(model)
    for ani in Ls_Animal_animal:
        if Dict_animal[type(ani)] == "Mammifère":

            item = QStandardItem("Id: " + ani.Id_animal + " * " + Dict_animal[type(ani)] +
                " * " + ani.Nom_animal + " * " + ani.Couleur_mammifere + " * Poid:" +
                str(ani.Poid_animal) + " Lbs * Gestation:" + str(ani.Temps_de_gestation) +
             " mois * Régime:" + ani.Regime_animal + " * Enclos: " + str(ani.Enclos.__dict__))

            model.appendRow(item)

        elif Dict_animal[type(ani)] == "Poisson":
            item = QStandardItem("Id: " + ani.Id_animal + " * " + Dict_animal[
                type(ani)] + " * " + ani.Nom_animal + " * Dent: " + ani.Machoire_dente + " * Poid:" + str(
                ani.Poid_animal) + " Lbs * Longueur" + str(
                ani.Longueur_poisson) + " po * Régime:" + ani.Regime_animal + " * Enclos: " + str(ani.Enclos.__dict__))
            model.appendRow(item)

        elif Dict_animal[type(ani)] == "Oiseau":
            item = QStandardItem("Id: " +ani.Id_animal + " * " + Dict_animal[type(ani)] +
                                 " * " + ani.Nom_animal + " * Couleur:" + ani.Couleur_plumage +
                                 " * Poid:" + str(ani.Poid_animal) + " Lbs * Grandeur:" + str(ani.Grandeur_oiseau) +
                                 " cm * Régime:" + ani.Regime_animal + " * Enclos: " + str(ani.Enclos.__dict__))
            model.appendRow(item)
def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_err_poid_animal.setVisible(False)
    objet.label_err_nom_animal.setVisible(False)
    objet.label_err_id_animal.setVisible(False)
    objet.label_err_enclos_animal.setVisible(False)


# Classe
######################################################
###### DÉFINITIONS DE LA CLASSE popup_animal ######
######################################################


class PopUpAnimal(QtWidgets.QDialog, InterfaceAnimal7.Ui_Dialog):
    """
    Classe PopUpAnimal
    """
    def __init__(self, parent=None):
        super(PopUpAnimal, self).__init__(parent)
        self.setupUi(self)
        cacher_labels_erreur(self)
        for eclo in Ls_Enclos:
            self.comboBox_enclos_animal.addItem(eclo.Id_enclos)
        model_list_view_animaux(self)
    # Boutton pour ouvrir les création d'animaux  au menu principale

    @pyqtSlot()
    def on_Button_Choisir_animal_clicked(self):
        """
        Boutton qui ouvre les popup de création d'animaux
        :return: None
        """

        success = True
        success2 = True
        success3 = True

        # cacher les labels d'erreurs précédent
        cacher_labels_erreur(self)
        # Si la comboBox choisie Mammifere

        if self.comboBox_Animal.currentText() == "Mammifère":
            # Instancier une boite de dialogue
            dialog_Mammifere = PopUpMammifere(self)

            mamT = Mammifere()

            poid = self.lineEdit_poid_animal.text()
            try:
                float(poid)
            except:
                self.label_err_poid_animal.setVisible(True)
                success = False
            else:
                mamT.Poid_animal = float(poid)
                if mamT.Poid_animal != float(poid):
                    self.label_err_poid_animal.setVisible(True)
                    success = False

            if self.comboBox_enclos_animal.currentText() == "":
                success = False
                self.label_err_enclos_animal.setVisible(True)


            if self.lineEdit_nom_animal.text() == "":
                self.label_err_nom_animal.setVisible(True)
                success = False

            if len(self.lineEdit_id_animal.text()) != 7:
                self.label_err_id_animal.setVisible(True)
                success = False
            #Afficher la boite de dialogue
            if success == True:
                dialog_Mammifere.show()
                dialog_Mammifere.exec_()

            model_list_view_animaux(self)

        # Si la comboBox choisie Poisson

        elif self.comboBox_Animal.currentText() == "Poisson":

         # Instancier une boite de dialogue
            dialog_Poisson = PopUpPoisson(self)

            poissT = Poisson()

            poid = self.lineEdit_poid_animal.text()
            try:
                float(poid)
            except:
                self.label_err_poid_animal.setVisible(True)
                success2 = False
            else:
                poissT.Poid_animal = float(poid)
                if poissT.Poid_animal != float(poid):
                    self.label_err_poid_animal.setVisible(True)
                    success2 = False

            if self.comboBox_enclos_animal.currentText() == "":
                success2 = False
                self.label_err_enclos_animal.setVisible(True)

            if self.lineEdit_nom_animal.text() == "":
                self.label_err_nom_animal.setVisible(True)
                success2 = False

            if len(self.lineEdit_id_animal.text()) != 7:
                self.label_err_id_animal.setVisible(True)
                success2 = False
            # Afficher la boite de dialogue
            if success2 == True:

                dialog_Poisson.show()
                dialog_Poisson.exec_()

            model_list_view_animaux(self)

        # Si la comboBox choisie Oiseau

        elif self.comboBox_Animal.currentText() == "Oiseau":
            # Instancier une boite de dialogue
            dialog_Oiseau = PopUpOiseau(self)

            oisT = Oiseau()

            poid = self.lineEdit_poid_animal.text()
            try:
                float(poid)
            except:
                self.label_err_poid_animal.setVisible(True)
                success3 = False
            else:
                oisT.Poid_animal = float(poid)
                if oisT.Poid_animal != float(poid):
                    self.label_err_poid_animal.setVisible(True)
                    success3 = False

            if self.comboBox_enclos_animal.currentText() == "":
                success3 = False
                self.label_err_enclos_animal.setVisible(True)

            if self.lineEdit_nom_animal.text() == "":
                self.label_err_nom_animal.setVisible(True)
                success3 = False

            if len(self.lineEdit_id_animal.text()) != 7:
                self.label_err_id_animal.setVisible(True)
                success3 = False
            # Afficher la boite de dialogue
            if success3 == True:

                dialog_Oiseau.show()
                dialog_Oiseau.exec_()

                model_list_view_animaux(self)

    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_quitter_animal_clicked(self):
        """
        Méthode du bouton Menu principal pour fermer le popup
        :return: None
        """
        self.close()




