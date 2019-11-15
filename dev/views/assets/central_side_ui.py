# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\central_side.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CentralSide(object):
    def setupUi(self, CentralSide):
        CentralSide.setObjectName("CentralSide")
        CentralSide.resize(600, 544)
        self.verticalLayout = QtWidgets.QVBoxLayout(CentralSide)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.title_label = QtWidgets.QLabel(CentralSide)
        self.title_label.setStyleSheet("QLabel\n"
"{\n"
"     font-weight: bold;\n"
"     font-size: 18px;\n"
"}")
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.video_player_frame = QtWidgets.QFrame(CentralSide)
        self.video_player_frame.setMinimumSize(QtCore.QSize(600, 248))
        self.video_player_frame.setStyleSheet("QFrame\n"
"{\n"
"    border: 2px solid grey;\n"
"    background-color: black;\n"
"\n"
"}")
        self.video_player_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_player_frame.setObjectName("video_player_frame")
        self.verticalLayout.addWidget(self.video_player_frame)
        self.scrollArea = QtWidgets.QScrollArea(CentralSide)
        self.scrollArea.setStyleSheet("QScrollArea\n"
"{\n"
"    border: none;\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 583, 310))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comment_title_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.comment_title_label.setStyleSheet("QLabel\n"
"{\n"
"  font-weight: bold;\n"
"}")
        self.comment_title_label.setObjectName("comment_title_label")
        self.verticalLayout_2.addWidget(self.comment_title_label)
        self.comment_content_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.comment_content_label.setObjectName("comment_content_label")
        self.verticalLayout_2.addWidget(self.comment_content_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(CentralSide)
        QtCore.QMetaObject.connectSlotsByName(CentralSide)

    def retranslateUi(self, CentralSide):
        _translate = QtCore.QCoreApplication.translate
        CentralSide.setWindowTitle(_translate("CentralSide", "Form"))
        self.title_label.setText(_translate("CentralSide", "Title"))
        self.comment_title_label.setText(_translate("CentralSide", "Commentaires:"))
        self.comment_content_label.setText(_translate("CentralSide", "If that address is correct, here are three other things you can try:\n"
"\n"
"    Try again later.\n"
"\n"
"    Check your network connection.\n"
"    \n"
"    If you are connected but behind a firewall, check that Firefox has permission to access the Web.\n"
"    But you should know that i don\'t give a fuck about what they think about me\n"
"    I am a though nigga and I can shit everybody for your love\n"
"    Je ne sais meme plus quoi ecrire mais je veux juste remplir les lignes\n"
"    Ce motherfucker texte me fiche deje les jetons. J\'en ai marre\n"
"    Aparement je dois continuer d\'ecrire je ne sais quoi\n"
"    Mais il faut quand meme que je continue\n"
"    Je ne sais pas si tout va bien mais ca ira sans aucun doute\n"
"    Je suis sure que tout ira bien\n"
"    Je ne sais pas qui est Malcomn X\n"
"    Davido est un chanteur Africain et Chris Brown un Americain\n"
"\n"
"    Drake est mon meilleur rappeur US. J\'aime pratiquement tous ces sons\n"
"    Je ne suis pas un musicien de quel que sorte que ce soit car je sne suis pas talentueux\n"
"    Je pourrai bien entrainer mes enfants plus tard a jouer des instruments car c\'est bien pour ameliorer leur QI"))


from .icons_rc import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CentralSide = QtWidgets.QWidget()
    ui = Ui_CentralSide()
    ui.setupUi(CentralSide)
    CentralSide.show()
    sys.exit(app.exec_())
