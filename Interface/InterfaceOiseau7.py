# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_oiseau.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 382)
        self.comboBox_couleur_oiseau = QtWidgets.QComboBox(Dialog)
        self.comboBox_couleur_oiseau.setGeometry(QtCore.QRect(20, 120, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(17)
        self.comboBox_couleur_oiseau.setFont(font)
        self.comboBox_couleur_oiseau.addItem("Bleu")
        self.comboBox_couleur_oiseau.addItem("Rouge")
        self.comboBox_couleur_oiseau.addItem("Jaune")
        self.comboBox_couleur_oiseau.addItem("Mauve")
        self.comboBox_couleur_oiseau.addItem("Noir")
        self.comboBox_couleur_oiseau.addItem("Orange")
        self.comboBox_couleur_oiseau.addItem("Rose")
        self.comboBox_couleur_oiseau.addItem("Gris")
        self.comboBox_couleur_oiseau.addItem("Vert")
        self.comboBox_couleur_oiseau.addItem("Brun")
        self.comboBox_couleur_oiseau.setObjectName("comboBox_couleur_oiseau")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_id_11 = QtWidgets.QLabel(Dialog)
        self.label_id_11.setGeometry(QtCore.QRect(20, 70, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_11.setFont(font)
        self.label_id_11.setObjectName("label_id_11")
        self.label_err_grandeur_ois = QtWidgets.QLabel(Dialog)
        self.label_err_grandeur_ois.setGeometry(QtCore.QRect(20, 310, 221, 41))
        self.label_err_grandeur_ois.setObjectName("label_err_grandeur_ois")
        self.label_err_id_ois = QtWidgets.QLabel(Dialog)
        self.label_err_id_ois.setGeometry(QtCore.QRect(230, 78, 291, 41))
        self.label_err_id_ois.setObjectName("label_err_id_ois")
        self.label_id_12 = QtWidgets.QLabel(Dialog)
        self.label_id_12.setGeometry(QtCore.QRect(20, 190, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_12.setFont(font)
        self.label_id_12.setObjectName("label_id_12")
        self.doubleSpinBox_grandeur_oiseau = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_grandeur_oiseau.setGeometry(QtCore.QRect(20, 270, 171, 41))
        self.doubleSpinBox_grandeur_oiseau.setObjectName("doubleSpinBox_grandeur_oiseau")
        self.button_ajout_ois = QtWidgets.QPushButton(Dialog)
        self.button_ajout_ois.setGeometry(QtCore.QRect(230, 120, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_ajout_ois.setFont(font)
        self.button_ajout_ois.setObjectName("button_ajout_ois")
        self.button_supprim_ois = QtWidgets.QPushButton(Dialog)
        self.button_supprim_ois.setGeometry(QtCore.QRect(230, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_supprim_ois.setFont(font)
        self.button_supprim_ois.setObjectName("button_supprim_ois")
        self.button_modif_ois = QtWidgets.QPushButton(Dialog)
        self.button_modif_ois.setGeometry(QtCore.QRect(230, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_modif_ois.setFont(font)
        self.button_modif_ois.setObjectName("button_modif_ois")
        self.button_oiseau_cancel = QtWidgets.QPushButton(Dialog)
        self.button_oiseau_cancel.setGeometry(QtCore.QRect(330, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_oiseau_cancel.setFont(font)
        self.button_oiseau_cancel.setObjectName("button_oiseau_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Oiseau"))
        self.label_7.setText(_translate("Dialog", "Création d\'un oiseau"))
        self.label_id_11.setText(_translate("Dialog", "Couleur du plumage"))
        self.label_err_grandeur_ois.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Doit être supérieure à zéro</span></p></body></html>"))
        self.label_err_id_ois.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Vous essayer d'écraser un animal</span></p><p><span style=\" color:#ff0000;\"> veuillez changer l'id ou appuyer sur le boutton modiffier</span></p></body></html>"))
        self.label_id_12.setText(_translate("Dialog", "<html><head/><body><p>Grandeur de</p><p>l\'oiseau (cm)</p><p><br/></p></body></html>"))
        self.button_ajout_ois.setText(_translate("Dialog", "Ajouter"))
        self.button_supprim_ois.setText(_translate("Dialog", "Supprimer"))
        self.button_modif_ois.setText(_translate("Dialog", "Modifier"))
        self.button_oiseau_cancel.setText(_translate("Dialog", "Cancel"))
