# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from . import issueKey, viewKeys, viewUsers
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 477)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 521, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUI/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 10, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 361, 361))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 190, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("#toolButton {\n"
"    background-color: rgb(255, 105, 105)\n"
"}")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(720, 190, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("#toolButton_2 {\n"
"    background-color: rgb(0, 173, 84)\n"
"}")
        self.toolButton_2.setCheckable(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(510, 360, 381, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Mods
        self.bindButtons()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowFilePath(_translate("MainWindow", "D:\\Windows\\Downloads\\Docusafe\\images\\logo.png"))
        self.label_2.setText(_translate("MainWindow", "Administrative Panel"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Issue a license key and link a document to it."))
        self.pushButton.setText(_translate("MainWindow", "Issue License Key"))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "View all the keys in circulation."))
        self.pushButton_3.setText(_translate("MainWindow", "View Keys"))
        self.pushButton_2.setStatusTip(_translate("MainWindow", "View all the fingerprints in the database and their posessions."))
        self.pushButton_2.setText(_translate("MainWindow", "View Users"))
        self.toolButton.setStatusTip(_translate("MainWindow", "Stop the running server"))
        self.toolButton.setText(_translate("MainWindow", "STOP"))
        self.toolButton_2.setStatusTip(_translate("MainWindow", "Start the stopped server."))
        self.toolButton_2.setText(_translate("MainWindow", "START"))
        self.label_3.setText(_translate("MainWindow", "Server Status:"))
        self.label_4.setText(_translate("MainWindow", "Stopped"))
    
    #Function that binds all buttons to the dialog box
    def bindButtons(self):
        self.pushButton.clicked.connect(self.open_issueKey)
        self.pushButton_3.clicked.connect(self.open_viewKey)
        self.pushButton_2.clicked.connect(self.open_viewUsers)
        self.toolButton.setDisabled(True)
    
    #Open up the issueKey dialog box
    def open_issueKey(self): 
        Dialog = QtWidgets.QDialog()
        ui = issueKey.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
    
    #Open up the viewKeys dialog box
    def open_viewKey(self):
        Dialog = QtWidgets.QDialog()
        ui = viewKeys.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    #Open up the viewUsers dialog box
    def open_viewUsers(self):
        Dialog = QtWidgets.QDialog()
        ui = viewUsers.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()