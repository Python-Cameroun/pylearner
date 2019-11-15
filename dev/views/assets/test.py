# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuAffichage.setTitle(_translate("MainWindow", "Affichage"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionPlein_Ecran.setText(_translate("MainWindow", "Plein Ecran"))
        self.actionRacourcis_clavier.setText(_translate("MainWindow", "Racourcis clavier"))
        self.actionA_Propos.setText(_translate("MainWindow", "A Propos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
