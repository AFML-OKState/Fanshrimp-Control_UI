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
        Dialog.resize(370, 143)
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shrimp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 96))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.com_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_in.sizePolicy().hasHeightForWidth())
        self.com_in.setSizePolicy(sizePolicy)
        self.com_in.setObjectName("com_in")
        self.gridLayout.addWidget(self.com_in, 0, 2, 1, 1)
        self.status_out = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_out.setText("")
        self.status_out.setAlignment(QtCore.Qt.AlignCenter)
        self.status_out.setObjectName("status_out")
        self.gridLayout.addWidget(self.status_out, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.SP_in = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SP_in.sizePolicy().hasHeightForWidth())
        self.SP_in.setSizePolicy(sizePolicy)
        self.SP_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SP_in.setAlignment(QtCore.Qt.AlignCenter)
        self.SP_in.setDecimals(0)
        self.SP_in.setMaximum(4095.0)
        self.SP_in.setObjectName("SP_in")
        self.gridLayout.addWidget(self.SP_in, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_but = QtWidgets.QPushButton(Dialog)
        self.set_but.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.set_but.setObjectName("set_but")
        self.stop_but = QtWidgets.QPushButton(Dialog)
        self.stop_but.setGeometry(QtCore.QRect(280, 110, 75, 23))
        self.stop_but.setObjectName("stop_but")
        self.con_but = QtWidgets.QPushButton(Dialog)
        self.con_but.setGeometry(QtCore.QRect(100, 110, 75, 23))
        self.con_but.setObjectName("con_but")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Motor Control"))
        self.label_3.setText(_translate("Dialog", "Status"))
        self.label.setText(_translate("Dialog", "Frequency Setpoint [Hz]"))
        self.label_2.setText(_translate("Dialog", "Com Port"))
        self.set_but.setText(_translate("Dialog", "Set"))
        self.stop_but.setText(_translate("Dialog", "Stop"))
        self.con_but.setText(_translate("Dialog", "Connect"))
