# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.connexion_page = QtWidgets.QWidget()
        self.connexion_page.setObjectName("connexion_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.connexion_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.connexion_page)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/svg/pythonUY1.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.connexion_page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(32)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.connexion_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(80, 64))
        self.label_3.setMaximumSize(QtCore.QSize(80, 64))
        self.label_3.setStyleSheet("QLabel {\n"
"    border: 1px solid  rgb(54, 149, 243);\n"
"    border-radius:  32px;\n"
"    margin-left: 16px;\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/svg/telegram.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.connexion_page)
        self.label_4.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.connexion_page)
        self.label_5.setMouseTracking(False)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_line = QtWidgets.QLineEdit(self.connexion_page)
        self.username_line.setMinimumSize(QtCore.QSize(292, 36))
        self.username_line.setStyleSheet("QLineEdit {\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    border: 1px solid black;\n"
"    border-color: rgb(120, 124, 129) none none rgb(120, 124, 129);\n"
"}\n"
"\n"
"QLineEdit: hover\n"
"{\n"
"    border: 1px solid rgb(54, 149, 243);\n"
"}")
        self.username_line.setObjectName("username_line")
        self.verticalLayout.addWidget(self.username_line)
        self.password_line = QtWidgets.QLineEdit(self.connexion_page)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setMinimumSize(QtCore.QSize(292, 36))
        self.password_line.setStyleSheet("QLineEdit {\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    border: 1px solid black;\n"
"    border-color: rgb(120, 124, 129) none none rgb(120, 124, 129);\n"
"}\n"
"\n"
"QLineEdit: hover\n"
"{\n"
"    border: 1px solid rgb(54, 149, 243);\n"
"}")
        self.password_line.setObjectName("password_line")
        self.verticalLayout.addWidget(self.password_line)
        self.pushButton = QtWidgets.QPushButton(self.connexion_page)
        self.pushButton.setMinimumSize(QtCore.QSize(292, 36))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(54, 149, 243);\n"
"    border: none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.connexion_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.main_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuAffichage = QtWidgets.QMenu(self.menubar)
        self.menuAffichage.setObjectName("menuAffichage")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionPlein_Ecran = QtWidgets.QAction(MainWindow)
        self.actionPlein_Ecran.setObjectName("actionPlein_Ecran")
        self.actionRacourcis_clavier = QtWidgets.QAction(MainWindow)
        self.actionRacourcis_clavier.setObjectName("actionRacourcis_clavier")
        self.actionA_Propos = QtWidgets.QAction(MainWindow)
        self.actionA_Propos.setObjectName("actionA_Propos")
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAffichage.addAction(self.actionPlein_Ecran)
        self.menuAide.addAction(self.actionRacourcis_clavier)
        self.menuAide.addAction(self.actionA_Propos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())        
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "PYUY1"))
        self.label_4.setText(_translate("MainWindow", "Se connecter"))
        self.label_5.setText(_translate("MainWindow", "         La plateforme reservee aux membres de la communaute python de l\'universite de yaounde 1. Si vous faites parti de la communaute et ne parvenez pas a vous connecter, veuillez contacter htttps://pyuy1.com/register"))
        self.username_line.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password_line.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Acceder a mes cours"))
        
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuAffichage.setTitle(_translate("MainWindow", "Affichage"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionPlein_Ecran.setText(_translate("MainWindow", "Plein Ecran"))
        self.actionRacourcis_clavier.setText(_translate("MainWindow", "Racourcis clavier"))
        self.actionA_Propos.setText(_translate("MainWindow", "A Propos"))        


from icons_rc import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
