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
        cacher_labels_erreur(self)
        """
        Méthode du bouton creer pour créer et ajouter un poisson à la liste view
        :return:
        """
        poiss = Poisson()

        success = True
        # Entrée de donnée pour les attributs de l'objet mammifere


        poiss.Longueur_poisson = self.doubleSpinBox_longueur_poisson.value()


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


    #button modifier pour modifier un objet
    @pyqtSlot()
    def on_button_modif_poisson_clicked(self):
        cacher_labels_erreur(self)
        """
        Méthode du bouton modifier pour modifier un objet
        :return: None
        """
        poiss = Poisson()

        success = True
        # Entrée de donnée pour les attributs de l'objet mammifere


        poiss.Longueur_poisson = self.doubleSpinBox_longueur_poisson.value()

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


        if verif_id == False:
            success = False
            self.label_err_general_poiss.setText(
                                "<font color=\"#ff0000\">Aucun id ne correspond à celui entrée</font>")

        # Ajouter l'objet instancié modifié à la liste des enclos et enleve l'ancien
        elif verif_id == True:
            for ani in Ls_Animal_animal:
                if ani.Id_animal == poiss.Id_animal:
                    if success == True:
                        Ls_Animal_animal.remove(ani)
                        Ls_Animal_animal.append(poiss)




    # Boutton supprimer pour supprimer un animal
    @pyqtSlot()
    def on_button_supprim_poisson_clicked(self):
        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des oiseau
        verif_id = verifier_id_animal_liste(self.popupPoisson.lineEdit_id_animal.text())
        if verif_id == True:
            for ani in Ls_Animal_animal:
                if ani.Id_animal == self.popupPoisson.lineEdit_id_animal.text():
                    if Dict_animal[type(ani)] == "Poisson":
                        Ls_Animal_animal.remove(ani)

        elif verif_id == False:
            self.label_err_general_poiss.setText(
                                "<font color=\"#ff0000\">Aucun id ne correspond à celui entrée</font>")

    # Boutton séréaliser pour transformer objet en json
    @pyqtSlot()
    def on_button_serialiser_poisson_clicked(self):
        """
                Méthode de boutton permettant de séréaliser un objet
                :return: None
                """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet mammifere et d'un enclos

        poiss = Poisson()

        print("début")
        # Entrée de donnée pour les attributs de l'objet mammifere
        poiss.Id_animal = self.popupAnimal.lineEdit_id_animal.text()
        poiss.Enclos = self.popupAnimal.comboBox_enclos_animal.currentText()
        poiss.Nom_animal = self.popupAnimal.lineEdit_nom_animal.text()

        # Booleen qui nous informe si le numéro d'id existe ou pas dans la liste des oiseau
        verif_id = verifier_id_animal_liste(self.popupAnimal.lineEdit_id_animal.text())

        if verif_id == True:

            for ani in Ls_Animal_animal:
                if ani.Id_animal == poiss.Id_animal:
                    if Dict_animal[type(ani)] == "Mammifère":

                        # Séréaliser cet objet
                        result = ani.serialiser(f"{poiss.Id_animal} - {poiss.Nom_animal} .json")

                        # La séréalisation à fonctionner
                        if result == 0:
                            # Affiche le message de réussite
                            self.label_err_general_poiss.setText("<font color=\"#13ee00\">Séréaliser réussie!</font>")
                            self.label_err_general_poiss.setVisible(True)

                        elif result == 1:
                            self.label_err_general_poiss.setText(
                                "<font color=\"#ff0000\">L'écriture du fichier à échouer</font>")
                            self.label_err_general_mam.setVisible(True)

                        elif result == 2:
                            self.label_err_general_poiss.setText(
                                "<font color=\"#ff0000\">L'ouverture du fichier à échouer</font>")
                            self.label_err_general_mam.setVisible(True)


        else:

            self.label_err_general_poiss.setText(
                "<font color=\"#ff0000\">Le mammifère que vous essayer de séréaliser </span></p><p><span style=\" color:#ff0000;\"> ne fais pas partie de la liste</font>")


    # Boutton pour désérialiser le fichier json
    def on_button_deserialiser_mammifere_clicked(self):
        """
        Méthode du boutton deserialiser qui permet de desérialiser un fichier séréaliser
        :return: None
        """
        poissT = Poisson()

        poissT.Id_animal = self.popupAnimal.lineEdit_id_animal.text()
        poissT.Nom_animal = self.popupAnimal.lineEdit_nom_animal.text()

        poissT.deserialiser(f"{poissT.Id_animal} - {poissT.Nom_animal} .json")

        self.doubleSpinBox_longueur_poisson.setValue(poissT.Longueur_poisson)
        self.comboBox_machoire_poisson.setCurrentText(poissT.Machoire_dente)
        self.popupAnimal.lineEdit_id_animal.setText(poissT.Id_animal)
        self.popupAnimal.lineEdit_nom_animal.setText(poissT.Nom_animal)
        self.popupAnimal.lineEdit_poid_animal.setText(str(poissT.Poid_animal))
        self.popupAnimal.comboBox_enclos_animal.setCurrentText(poissT.Enclos)
        self.popupAnimal.comboBox_regime_animal.setCurrentText(poissT.Regime_animal)


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

