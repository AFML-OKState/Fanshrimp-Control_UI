# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 214)
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shrimp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 194))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
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
        self.gridLayout.addWidget(self.SP_in, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.stop_but = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stop_but.setObjectName("stop_but")
        self.gridLayout.addWidget(self.stop_but, 5, 3, 1, 1)
        self.con_but = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.con_but.setObjectName("con_but")
        self.gridLayout.addWidget(self.con_but, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.set_but = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.set_but.setObjectName("set_but")
        self.gridLayout.addWidget(self.set_but, 5, 2, 1, 1)
        self.Boards = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.Boards.setObjectName("Boards")
        self.gridLayout.addWidget(self.Boards, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.com_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_in.sizePolicy().hasHeightForWidth())
        self.com_in.setSizePolicy(sizePolicy)
        self.com_in.setObjectName("com_in")
        self.gridLayout.addWidget(self.com_in, 0, 3, 1, 1)
        self.status_out = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_out.setText("")
        self.status_out.setAlignment(QtCore.Qt.AlignCenter)
        self.status_out.setObjectName("status_out")
        self.gridLayout.addWidget(self.status_out, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Motor Control"))
        self.label_3.setText(_translate("Dialog", "Selected Com Port"))
        self.label.setText(_translate("Dialog", "Frequency Setpoint [Hz]"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.stop_but.setText(_translate("Dialog", "Stop"))
        self.con_but.setText(_translate("Dialog", "Connect"))
        self.label_2.setText(_translate("Dialog", "Add Com Port"))
        self.set_but.setText(_translate("Dialog", "Set"))
        self.label_5.setText(_translate("Dialog", "Available Com Port"))
        self.label_6.setText(_translate("Dialog", "Status"))
