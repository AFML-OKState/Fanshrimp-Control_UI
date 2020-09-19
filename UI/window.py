# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 212)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 311, 96))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.com_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.com_in.setObjectName("com_in")
        self.gridLayout.addWidget(self.com_in, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.meas_out = QtWidgets.QLabel(self.gridLayoutWidget)
        self.meas_out.setObjectName("meas_out")
        self.gridLayout.addWidget(self.meas_out, 2, 2, 1, 1)
        self.SP_in = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.SP_in.setDecimals(0)
        self.SP_in.setMaximum(4095.0)
        self.SP_in.setObjectName("SP_in")
        self.gridLayout.addWidget(self.SP_in, 1, 2, 1, 1)
        self.set_but = QtWidgets.QPushButton(Dialog)
        self.set_but.setGeometry(QtCore.QRect(180, 160, 75, 23))
        self.set_but.setObjectName("set_but")
        self.stop_but = QtWidgets.QPushButton(Dialog)
        self.stop_but.setGeometry(QtCore.QRect(270, 160, 75, 23))
        self.stop_but.setObjectName("stop_but")
        self.con_but = QtWidgets.QPushButton(Dialog)
        self.con_but.setGeometry(QtCore.QRect(90, 160, 75, 23))
        self.con_but.setObjectName("con_but")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Motor Control"))
        self.label_2.setText(_translate("Dialog", "Com Port"))
        self.label.setText(_translate("Dialog", "Frequency Setpoint"))
        self.label_3.setText(_translate("Dialog", "Frquency Measured"))
        self.meas_out.setText(_translate("Dialog", "TextLabel"))
        self.set_but.setText(_translate("Dialog", "Set"))
        self.stop_but.setText(_translate("Dialog", "Stop"))
        self.con_but.setText(_translate("Dialog", "Connect"))
