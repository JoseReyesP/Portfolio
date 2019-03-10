# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuckNorrisEncoder.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 452)
        self.input = QtWidgets.QTextEdit(Dialog)
        self.input.setGeometry(QtCore.QRect(10, 40, 481, 141))
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 17))
        self.label.setObjectName("label")
        self.pushButtonEncode = QtWidgets.QPushButton(Dialog)
        self.pushButtonEncode.setGeometry(QtCore.QRect(10, 200, 89, 25))
        self.pushButtonEncode.setObjectName("pushButtonEncode")
        self.output = QtWidgets.QTextEdit(Dialog)
        self.output.setEnabled(True)
        self.output.setGeometry(QtCore.QRect(10, 240, 481, 141))
        self.output.setObjectName("output")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 400, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButtonDecode = QtWidgets.QPushButton(Dialog)
        self.pushButtonDecode.setGeometry(QtCore.QRect(130, 200, 89, 25))
        self.pushButtonDecode.setObjectName("pushButtonDecode")

        self.retranslateUi(Dialog)
        self.pushButton.pressed.connect(self.output.selectAll)
        self.pushButton.released.connect(self.output.copy)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ChuckNorris Encoder"))
        self.label.setText(_translate("Dialog", "Introdusca su mensaje"))
        self.pushButtonEncode.setText(_translate("Dialog", "Encode"))
        self.pushButton.setText(_translate("Dialog", "Copiar"))
        self.pushButtonDecode.setText(_translate("Dialog", "Decode"))


