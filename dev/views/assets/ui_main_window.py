# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.connexion_page = QtWidgets.QWidget()
        self.connexion_page.setObjectName("connexion_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.connexion_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(64, -1, -1, -1)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.connexion_page)
        self.label_3.setMinimumSize(QtCore.QSize(80, 64))
        self.label_3.setMaximumSize(QtCore.QSize(80, 64))
        self.label_3.setStyleSheet("QLabel {\n"
"    border: 1px solid  rgb(54, 149, 243);\n"
"   border-radius:  32px;\n"
"    margin-left: 16px;\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/svg/pythonUY1.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.connexion_page)
        self.label_4.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"   font-weight: bold;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_5 = QtWidgets.QLabel(self.connexion_page)
        self.label_5.setMouseTracking(True)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.username_line = QtWidgets.QLineEdit(self.connexion_page)
        self.username_line.setMinimumSize(QtCore.QSize(312, 42))
        self.username_line.setStyleSheet("QLineEdit {\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    border: 1px solid black;\n"
"    border-color: rgb(120, 124, 129) none none rgb(120, 124, 129);\n"
"}\n"
"\n"
"QLineEdit: hover\n"
"{\n"
"   border: 1px solid rgb(54, 149, 243);\n"
"}")
        self.username_line.setObjectName("username_line")
        self.verticalLayout_2.addWidget(self.username_line)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.connexion_page)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(312, 42))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    border: 1px solid black;\n"
"    border-color: rgb(120, 124, 129) none none rgb(120, 124, 129);\n"
"}\n"
"\n"
"QLineEdit: hover\n"
"{\n"
"   border: 1px solid rgb(54, 149, 243);\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.connexion_page)
        self.pushButton.setMinimumSize(QtCore.QSize(312, 42))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(54, 149, 243);\n"
"    border: none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.connexion_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.main_page)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
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
        self.actionPlein_ecran = QtWidgets.QAction(MainWindow)
        self.actionPlein_ecran.setObjectName("actionPlein_ecran")
        self.actionRaccourcis_clavier = QtWidgets.QAction(MainWindow)
        self.actionRaccourcis_clavier.setObjectName("actionRaccourcis_clavier")
        self.actionNouveau = QtWidgets.QAction(MainWindow)
        self.actionNouveau.setObjectName("actionNouveau")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionA_Propos = QtWidgets.QAction(MainWindow)
        self.actionA_Propos.setObjectName("actionA_Propos")
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAffichage.addAction(self.actionPlein_ecran)
        self.menuAide.addAction(self.actionRaccourcis_clavier)
        self.menuAide.addAction(self.actionA_Propos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "PYUY1"))
        self.label_4.setText(_translate("MainWindow", "Se connecter"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>La plateforme reservee aux membres de la communaute python de l\'universite de yaounde 1. Si vous faites parti de la communaute et ne parvenez pas a vous connecter, veuillez contacter <a href=\"htttps://pyuy1.com/register\"><span style=\" text-decoration: underline; color:#0000ff;\">htttps://pyuy1.com/register</span></a></p></body></html>"))
        self.username_line.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Acceder a mes cours"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuAffichage.setTitle(_translate("MainWindow", "Affichage"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionPlein_ecran.setText(_translate("MainWindow", "Plein ecran"))
        self.actionRaccourcis_clavier.setText(_translate("MainWindow", "Raccourcis clavier"))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionA_Propos.setText(_translate("MainWindow", "A Propos"))

from .icons_rc import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
