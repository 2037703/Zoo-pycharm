# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_Mammifere.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mammifere(object):
    def setupUi(self, Mammifere):
        Mammifere.setObjectName("Mammifere")
        Mammifere.resize(628, 385)
        self.label_7 = QtWidgets.QLabel(Mammifere)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_id_11 = QtWidgets.QLabel(Mammifere)
        self.label_id_11.setGeometry(QtCore.QRect(20, 250, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_11.setFont(font)
        self.label_id_11.setObjectName("label_id_11")
        self.comboBox_couleur_mammifere = QtWidgets.QComboBox(Mammifere)
        self.comboBox_couleur_mammifere.setGeometry(QtCore.QRect(20, 300, 171, 41))
        self.comboBox_couleur_mammifere.setObjectName("comboBox_couleur_mammifere")
        self.label_id_12 = QtWidgets.QLabel(Mammifere)
        self.label_id_12.setGeometry(QtCore.QRect(20, 80, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_12.setFont(font)
        self.label_id_12.setObjectName("label_id_12")
        self.spinBox_temps_gestation = QtWidgets.QSpinBox(Mammifere)
        self.spinBox_temps_gestation.setGeometry(QtCore.QRect(20, 150, 171, 41))
        self.spinBox_temps_gestation.setObjectName("spinBox_temps_gestation")
        self.label_err_temps_gest_mam = QtWidgets.QLabel(Mammifere)
        self.label_err_temps_gest_mam.setGeometry(QtCore.QRect(20, 190, 221, 41))
        self.label_err_temps_gest_mam.setObjectName("label_err_temps_gest_mam")
        self.button_supprim_mammifere = QtWidgets.QPushButton(Mammifere)
        self.button_supprim_mammifere.setGeometry(QtCore.QRect(250, 290, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_supprim_mammifere.setFont(font)
        self.button_supprim_mammifere.setObjectName("button_supprim_mammifere")
        self.button_modif_mammifere = QtWidgets.QPushButton(Mammifere)
        self.button_modif_mammifere.setGeometry(QtCore.QRect(250, 220, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_modif_mammifere.setFont(font)
        self.button_modif_mammifere.setObjectName("button_modif_mammifere")
        self.button_serialiser_mammifere = QtWidgets.QPushButton(Mammifere)
        self.button_serialiser_mammifere.setGeometry(QtCore.QRect(430, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_serialiser_mammifere.setFont(font)
        self.button_serialiser_mammifere.setObjectName("button_serialiser_mammifere")
        self.button_cancel_mammifere = QtWidgets.QPushButton(Mammifere)
        self.button_cancel_mammifere.setGeometry(QtCore.QRect(430, 290, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_cancel_mammifere.setFont(font)
        self.button_cancel_mammifere.setObjectName("button_cancel_mammifere")
        self.button_deserialiser_mammifere = QtWidgets.QPushButton(Mammifere)
        self.button_deserialiser_mammifere.setGeometry(QtCore.QRect(430, 220, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_deserialiser_mammifere.setFont(font)
        self.button_deserialiser_mammifere.setObjectName("button_deserialiser_mammifere")
        self.button_ajout_mammifere = QtWidgets.QPushButton(Mammifere)
        self.button_ajout_mammifere.setGeometry(QtCore.QRect(250, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_ajout_mammifere.setFont(font)
        self.button_ajout_mammifere.setObjectName("button_ajout_mammifere")

        self.retranslateUi(Mammifere)
        QtCore.QMetaObject.connectSlotsByName(Mammifere)

    def retranslateUi(self, Mammifere):
        _translate = QtCore.QCoreApplication.translate
        Mammifere.setWindowTitle(_translate("Mammifere", "Mammifere"))
        self.label_7.setText(_translate("Mammifere", "Création d\'un mammifère"))
        self.label_id_11.setText(_translate("Mammifere", "Couleur du mammifère"))
        self.label_id_12.setText(_translate("Mammifere", "<html><head/><body><p>Temps de gestation </p><p>de l\'animal (Mois)</p><p><br/></p><p><br/></p></body></html>"))
        self.spinBox_temps_gestation.setToolTip(_translate("Mammifere", "<html><head/><body><p><br/></p></body></html>"))
        self.label_err_temps_gest_mam.setText(_translate("Mammifere", "<html><head/><body><p><span style=\" color:#ff0000;\">Doit être supérieure à zéro</span></p></body></html>"))
        self.button_supprim_mammifere.setText(_translate("Mammifere", "Supprimer"))
        self.button_modif_mammifere.setText(_translate("Mammifere", "Modifier"))
        self.button_serialiser_mammifere.setText(_translate("Mammifere", "Sérialiser"))
        self.button_cancel_mammifere.setText(_translate("Mammifere", "Cancel"))
        self.button_deserialiser_mammifere.setText(_translate("Mammifere", "Désérialiser"))
        self.button_ajout_mammifere.setText(_translate("Mammifere", "Ajouter"))