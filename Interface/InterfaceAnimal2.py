# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_Animal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 650)
        self.label_id_6 = QtWidgets.QLabel(Dialog)
        self.label_id_6.setGeometry(QtCore.QRect(260, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_6.setFont(font)
        self.label_id_6.setObjectName("label_id_6")
        self.label_id_8 = QtWidgets.QLabel(Dialog)
        self.label_id_8.setGeometry(QtCore.QRect(30, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_8.setFont(font)
        self.label_id_8.setObjectName("label_id_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_id_5 = QtWidgets.QLabel(Dialog)
        self.label_id_5.setGeometry(QtCore.QRect(30, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_id_5.setFont(font)
        self.label_id_5.setObjectName("label_id_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_err_id_animal = QtWidgets.QLabel(Dialog)
        self.label_err_id_animal.setGeometry(QtCore.QRect(30, 200, 221, 41))
        self.label_err_id_animal.setObjectName("label_err_id_animal")
        self.comboBox_Animal = QtWidgets.QComboBox(Dialog)
        self.comboBox_Animal.setGeometry(QtCore.QRect(260, 150, 171, 41))
        self.comboBox_Animal.setObjectName("comboBox_regime_animal_3")
        self.comboBox_enclos_animal = QtWidgets.QComboBox(Dialog)
        self.comboBox_enclos_animal.setGeometry(QtCore.QRect(30, 320, 171, 41))
        self.comboBox_enclos_animal.setObjectName("comboBox_enclos_animal")
        self.lineEdit_id_animal_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_id_animal_2.setGeometry(QtCore.QRect(30, 150, 171, 41))
        self.lineEdit_id_animal_2.setObjectName("lineEdit_id_animal_2")
        self.label_err_enclos_animal = QtWidgets.QLabel(Dialog)
        self.label_err_enclos_animal.setGeometry(QtCore.QRect(30, 370, 221, 41))
        self.label_err_enclos_animal.setObjectName("label_err_enclos_animal")
        self.button_supprim_animal = QtWidgets.QPushButton(Dialog)
        self.button_supprim_animal.setGeometry(QtCore.QRect(260, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_supprim_animal.setFont(font)
        self.button_supprim_animal.setObjectName("button_supprim_animal")
        self.button_modif_animal = QtWidgets.QPushButton(Dialog)
        self.button_modif_animal.setGeometry(QtCore.QRect(260, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_modif_animal.setFont(font)
        self.button_modif_animal.setObjectName("button_modif_animal")
        self.button_ajout_animal = QtWidgets.QPushButton(Dialog)
        self.button_ajout_animal.setGeometry(QtCore.QRect(260, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_ajout_animal.setFont(font)
        self.button_ajout_animal.setObjectName("button_ajout_animal")
        self.button_serialiser_animal = QtWidgets.QPushButton(Dialog)
        self.button_serialiser_animal.setGeometry(QtCore.QRect(420, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_serialiser_animal.setFont(font)
        self.button_serialiser_animal.setObjectName("button_serialiser_animal")
        self.button_deserialiser_animal = QtWidgets.QPushButton(Dialog)
        self.button_deserialiser_animal.setGeometry(QtCore.QRect(420, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_deserialiser_animal.setFont(font)
        self.button_deserialiser_animal.setObjectName("button_deserialiser_animal")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(30, 420, 531, 192))
        self.listView.setObjectName("listView")
        self.button_quitter_animal = QtWidgets.QPushButton(Dialog)
        self.button_quitter_animal.setGeometry(QtCore.QRect(420, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(16)
        self.button_quitter_animal.setFont(font)
        self.button_quitter_animal.setObjectName("button_quitter_animal")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Animal"))
        self.label_id_6.setText(_translate("Dialog", "Choix de l\'animal"))
        self.label_id_8.setText(_translate("Dialog", "Enclos "))
        self.pushButton.setText(_translate("Dialog", "Choisir"))
        self.label_id_5.setText(_translate("Dialog", "Numéro de l\'animal"))
        self.label_7.setText(_translate("Dialog", "ANIMAL"))
        self.label_err_id_animal.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Longueur de l\'id de l\'animal doit être égal à 7 </span></p><p><span style=\" color:#ff0000;\">et composée seulement de numéro</span></p></body></html>"))
        self.label_err_enclos_animal.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Vous devez créer un enclos</span></p><p><br/></p></body></html>"))
        self.button_supprim_animal.setText(_translate("Dialog", "Supprimer"))
        self.button_modif_animal.setText(_translate("Dialog", "Modifier"))
        self.button_ajout_animal.setText(_translate("Dialog", "Ajouter"))
        self.button_serialiser_animal.setText(_translate("Dialog", "Sérialiser"))
        self.button_deserialiser_animal.setText(_translate("Dialog", "Désérialiser"))
        self.button_quitter_animal.setText(_translate("Dialog", "Menu principale"))
