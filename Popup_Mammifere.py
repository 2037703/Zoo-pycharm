####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet Synthèse
###  Nom: Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Description de la classe popup_Mammifere
####################################################################################



#######################################
###  IMPORTATIONS - Portée globale  ###
#######################################
#importation outils PyQt5
from PyQt5 import QtWidgets

#importation de l'interface
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Interface import InterfaceMammifere7
from Interface import InterfaceAnimal7
#Importation de popup

from Popup_Animal import *
#Import des classes
from enclos import Enclos
from mammifere import *

#Import logique
from logique import Dict_animal
from logique import Ls_Animal_animal

Enclos1 =Enclos()



#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################
# Code pris de l'exercice cours
def verifier_id_animal_liste(p_id) -> bool:
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
    objet.label_err_temps_gest_mam.setVisible(False)
    objet.label_err_id_mam.setVisible(False)
    objet.label_err_general_mam.setVisible(False)
######################################################
###### DÉFINITIONS DE LA CLASSE popup_Mammifere ######
######################################################

class PopUpMammifere(QtWidgets.QDialog, InterfaceMammifere7.Ui_Mammifere):
    def __init__(self,p_popupAnimal,  parent=None):
        super(PopUpMammifere, self).__init__(parent)
        self.setupUi(self)
        self.popupAnimal = p_popupAnimal
        cacher_labels_erreur(self)
    # Boutton ajouter pour créer un mammifère
    @pyqtSlot()
    def on_button_ajout_mammifere_clicked(self):
        """
        Méthode du bouton ajouter pour créer un mammifère
        :return: None
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet mammifere

        mam = Mammifere()

        success = True
        # Entrée de donnée pour les attributs de l'objet mammifere

        mam.Temps_de_gestation = self.spinBox_temps_gestation.value()
        if mam.Temps_de_gestation == -1:
            self.label_err_temps_gest_mam.setVisible(True)
            success = False
        mam.Couleur_mammifere = self.comboBox_couleur_mammifere.currentText()
        mam.Id_animal = self.popupAnimal.lineEdit_id_animal.text()
        mam.Nom_animal = self.popupAnimal.lineEdit_nom_animal.text()
        mam.Poid_animal = float(self.popupAnimal.lineEdit_poid_animal.text())
        mam.Enclos = self.popupAnimal.comboBox_enclos_animal.currentText()
        mam.Regime_animal = self.popupAnimal.comboBox_regime_animal.currentText()


        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des mammifere
        verif_id = verifier_id_animal_liste(mam.Id_animal)

        if verif_id == True:
            success = False
            self.label_err_id_mam.setVisible(True)

        # Ajouter l'objet instancié à la liste des enclos
        if success == True:
            Ls_Animal_animal.append(mam)

    # Boutton ajouter pour créer un mammifère
    @pyqtSlot()
    def on_button_modif_mammifere_clicked(self):
        """
        Méthode du bouton modifier pour modifier un modifier
        :return: None
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet mammifere

        mam = Mammifere()

        success = True
        # Entrée de donnée pour les attributs de l'objet mammifere

        mam.Temps_de_gestation = self.spinBox_temps_gestation.value()
        if mam.Temps_de_gestation == -1:
            self.label_err_temps_gest_mam.setVisible(True)
            success = False
        mam.Couleur_mammifere = self.comboBox_couleur_mammifere.currentText()
        mam.Id_animal = self.popupAnimal.lineEdit_id_animal.text()
        mam.Nom_animal = self.popupAnimal.lineEdit_nom_animal.text()
        mam.Poid_animal = float(self.popupAnimal.lineEdit_poid_animal.text())
        mam.Enclos = self.popupAnimal.comboBox_enclos_animal.currentText()
        mam.Regime_animal = self.popupAnimal.comboBox_regime_animal.currentText()

        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des mammifere
        verif_id = verifier_id_animal_liste(mam.Id_animal)

        if verif_id == False:
            success = False
            self.label_err_general_mam.setText(
                                "<font color=\"#ff0000\">Aucun id ne correspond à celui entrée</font>")
            self.label_err_general_mam.setVisible(True)

        if verif_id == True:
            for ani in Ls_Animal_animal:
                if ani.Id_animal == mam.Id_animal:
                    if success == True:
                        Ls_Animal_animal.remove(ani)
                        Ls_Animal_animal.append(mam)


    # Boutton supprimer pour supprimer un animal
    @pyqtSlot()
    def on_button_supprim_mammifere_clicked(self):
        """
        Méthode permettant de supprimer un objet instancier
        :return: None
        """
        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des oiseau
        verif_id = verifier_id_animal_liste(self.popupAnimal.lineEdit_id_animal.text())
        if verif_id == True:
            for ani in Ls_Animal_animal:
                if ani.Id_animal == self.popupAnimal.lineEdit_id_animal.text():
                    if Dict_animal[type(ani)] == "Mammifère":
                        Ls_Animal_animal.remove(ani)

        elif verif_id == False:
            self.label_err_general_mam.setText(
                                "<font color=\"#ff0000\">Aucun id ne correspond à celui entrée</font>")
            self.label_err_general_mam.setVisible(True)
    # Boutton sérialiser pour sauvegarder dans un fichier json
    @pyqtSlot()
    def on_button_serialiser_mammifere_clicked(self):
        """
        Méthode de boutton permettant de séréaliser un objet
        :return: None
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet mammifere et d'un enclos

        mam = Mammifere()




        # Entrée de donnée pour les attributs de l'objet mammifere
        mam.Id_animal = self.popupAnimal.lineEdit_id_animal.text()
        mam.Enclos = self.popupAnimal.comboBox_enclos_animal.currentText()
        mam.Nom_animal = self.popupAnimal.lineEdit_nom_animal.text()

        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des oiseau
        verif_id = verifier_id_animal_liste(self.popupAnimal.lineEdit_id_animal.text())

        if verif_id == True:

            for ani in Ls_Animal_animal:
                if ani.Id_animal == mam.Id_animal:
                    if Dict_animal[type(ani)] == "Mammifère":

                        # Séréaliser cet objet
                        result = ani.serialiser(f"{mam.Id_animal} - {mam.Nom_animal} .json")

                        # La séréalisation à fonctionner
                        if result == 0:
                            #Affiche le message de réussite
                            self.label_err_general_mam.setText("<font color=\"#13ee00\">Séréaliser réussie!</font>")
                            self.label_err_general_mam.setVisible(True)

                        elif result == 1:
                            self.label_err_general_mam.setText("<font color=\"#ff0000\">L'écriture du fichier à échouer</font>")
                            self.label_err_general_mam.setVisible(True)

                        elif result == 2:
                            self.label_err_general_mam.setText("<font color=\"#ff0000\">L'ouverture du fichier à échouer</font>")
                            self.label_err_general_mam.setVisible(True)


        else:

            self.label_err_general_mam.setText("<font color=\"#ff0000\">Le mammifère que vous essayer de séréaliser </span></p><p><span style=\" color:#ff0000;\"> ne fais pas partie de la liste</font>")
            self.label_err_general_mam.setVisible(True)
    # Boutton pour désérialiser le fichier json
    def on_button_deserialiser_mammifere_clicked(self):
        """
        Méthode du boutton deserialiser qui permet de desérialiser un fichier séréaliser
        :return: None
        """
        mamT = Mammifere()

        mamT.Id_animal = self.popupAnimal.lineEdit_id_animal.text()
        mamT.Nom_animal = self.popupAnimal.lineEdit_nom_animal.text()

        mamT.deserialiser(f"{mamT.Id_animal} - {mamT.Nom_animal} .json")

        self.spinBox_temps_gestation.setValue(mamT.Temps_de_gestation)
        self.comboBox_couleur_mammifere.setCurrentText(mamT.Couleur_mammifere)
        self.popupAnimal.lineEdit_id_animal.setText(mamT.Id_animal)
        self.popupAnimal.lineEdit_nom_animal.setText(mamT.Nom_animal)
        self.popupAnimal.lineEdit_poid_animal.setText(str(mamT.Poid_animal))
        self.popupAnimal.comboBox_enclos_animal.setCurrentText(mamT.Enclos)
        self.popupAnimal.comboBox_regime_animal.setCurrentText(mamT.Regime_animal)



    # Boutton quitter pour revenir au menu principale
    @pyqtSlot()
    def on_button_cancel_mammifere_clicked(self):
        """
        Méthode du bouton cancel pour fermer le popup
        :return: None
        """
        self.close()


#########################
### Test des méthodes ###
#########################

    Mam1 = Mammifere("1234567", 5, "Chien", "aw", "Carnivore", "Bleu", 15)

    #Test des set
    Mam1.Temps_de_gestation = -1
    Mam1.Couleur_mammifere = "blou"
    Mam1.Regime_animal = "carnivore"
    Mam1.Id_animal = "adw"
    Mam1.Poid_animal = -1
    Mam1.Nom_animal = 22

#Test de sérialisation
    # Mam1.serialiser("a")
    # # print(result)
    # Mam1.deserialiser("a", Enclos1)



