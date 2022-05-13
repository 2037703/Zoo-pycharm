# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_Poisson.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 387)
        self.button_ajout_poisson = QtWidgets.QPushButton(Dialog)
        self.button_ajout_poisson.setGeometry(QtCore.QRect(210, 130, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_ajout_poisson.setFont(font)
        self.button_ajout_poisson.setObjectName("button_ajout_poisson")
        self.button_supprim_poisson = QtWidgets.QPushButton(Dialog)
        self.button_supprim_poisson.setGeometry(QtCore.QRect(210, 270, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_supprim_poisson.setFont(font)
        self.button_supprim_poisson.setObjectName("button_supprim_poisson")
        self.comboBox_machoire_poisson = QtWidgets.QComboBox(Dialog)
        self.comboBox_machoire_poisson.setGeometry(QtCore.QRect(20, 130, 171, 41))
        self.comboBox_machoire_poisson.setObjectName("comboBox_machoire_poisson")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_id_11 = QtWidgets.QLabel(Dialog)
        self.label_id_11.setGeometry(QtCore.QRect(20, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_11.setFont(font)
        self.label_id_11.setObjectName("label_id_11")
        self.label_err_longueur_poisson = QtWidgets.QLabel(Dialog)
        self.label_err_longueur_poisson.setGeometry(QtCore.QRect(20, 310, 221, 41))
        self.label_err_longueur_poisson.setObjectName("label_err_longueur_poisson")
        self.label_id_12 = QtWidgets.QLabel(Dialog)
        self.label_id_12.setGeometry(QtCore.QRect(20, 200, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_12.setFont(font)
        self.label_id_12.setObjectName("label_id_12")
        self.button_modif_poisson = QtWidgets.QPushButton(Dialog)
        self.button_modif_poisson.setGeometry(QtCore.QRect(210, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_modif_poisson.setFont(font)
        self.button_modif_poisson.setObjectName("button_modif_poisson")
        self.doubleSpinBox_longueur_poisson = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_longueur_poisson.setGeometry(QtCore.QRect(20, 280, 171, 41))
        self.doubleSpinBox_longueur_poisson.setObjectName("doubleSpinBox_longueur_poisson")
        self.button_cancel_poisson = QtWidgets.QPushButton(Dialog)
        self.button_cancel_poisson.setGeometry(QtCore.QRect(390, 270, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_cancel_poisson.setFont(font)
        self.button_cancel_poisson.setObjectName("button_cancel_poisson")
        self.button_deserialiser_animal = QtWidgets.QPushButton(Dialog)
        self.button_deserialiser_animal.setGeometry(QtCore.QRect(390, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_deserialiser_animal.setFont(font)
        self.button_deserialiser_animal.setObjectName("button_deserialiser_animal")
        self.button_serialiser_animal = QtWidgets.QPushButton(Dialog)
        self.button_serialiser_animal.setGeometry(QtCore.QRect(390, 130, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_serialiser_animal.setFont(font)
        self.button_serialiser_animal.setObjectName("button_serialiser_animal")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Poisson"))
        self.button_ajout_poisson.setText(_translate("Dialog", "Ajouter"))
        self.button_supprim_poisson.setText(_translate("Dialog", "Supprimer"))
        self.label_7.setText(_translate("Dialog", "Création d\'un poisson"))
        self.label_id_11.setText(_translate("Dialog", "Machoire dentée "))
        self.label_err_longueur_poisson.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Doit être supérieure à zéro</span></p></body></html>"))
        self.label_id_12.setText(_translate("Dialog", "<html><head/><body><p>Longueur du</p><p>poisson (po)</p></body></html>"))
        self.button_modif_poisson.setText(_translate("Dialog", "Modifier"))
        self.button_cancel_poisson.setText(_translate("Dialog", "Cancel"))
        self.button_deserialiser_animal.setText(_translate("Dialog", "Désérialiser"))
        self.button_serialiser_animal.setText(_translate("Dialog", "Sérialiser"))
