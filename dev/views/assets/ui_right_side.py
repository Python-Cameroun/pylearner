# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'right_side.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from .utils import CustomFrame

class Ui_RightSide(object):
    def setupUi(self, RightSide):
        RightSide.setObjectName("RightSide")
        RightSide.resize(159, 467)
        RightSide.setMaximumSize(QtCore.QSize(200, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(RightSide)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.code_frame = CustomFrame(RightSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.code_frame.sizePolicy().hasHeightForWidth())
        self.code_frame.setSizePolicy(sizePolicy)
        self.code_frame.setMinimumSize(QtCore.QSize(0, 38))
        self.code_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.code_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.code_frame.setStyleSheet("QFrame\n"
"{\n"
"    border-width: 1px 0px 0px 0px; \n"
"    border-style: solid; \n"
"    border-color: grey transparent grey transparent; \n"
"}")
        self.code_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.code_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.code_frame.setObjectName("code_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.code_frame)
        self.horizontalLayout_8.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.code_icon_label = QtWidgets.QLabel(self.code_frame)
        self.code_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.code_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.code_icon_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.code_icon_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.code_icon_label.setText("")
        self.code_icon_label.setPixmap(QtGui.QPixmap(":/svg/code.svg"))
        self.code_icon_label.setScaledContents(True)
        self.code_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.code_icon_label.setObjectName("code_icon_label")
        self.horizontalLayout_8.addWidget(self.code_icon_label)
        self.code_text_label = QtWidgets.QLabel(self.code_frame)
        self.code_text_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.code_text_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.code_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.code_text_label.setObjectName("code_text_label")
        self.horizontalLayout_8.addWidget(self.code_text_label)
        ##self.verticalLayout.addWidget(self.code_frame)
        self.question_frame = CustomFrame(RightSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_frame.sizePolicy().hasHeightForWidth())
        self.question_frame.setSizePolicy(sizePolicy)
        self.question_frame.setMinimumSize(QtCore.QSize(0, 38))
        self.question_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.question_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.question_frame.setStyleSheet("QFrame\n"
"{\n"
"    background: transparent;\n"
"    border-width:  1px 0px 0px 0px; \n"
"    border-style: solid; \n"
"    border-color: grey transparent grey transparent; \n"
"}")
        self.question_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.question_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.question_frame.setObjectName("question_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.question_frame)
        self.horizontalLayout_7.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.question_icon_label = QtWidgets.QLabel(self.question_frame)
        self.question_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.question_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.question_icon_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.question_icon_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.question_icon_label.setText("")
        self.question_icon_label.setPixmap(QtGui.QPixmap(":/svg/question-mark.svg"))
        self.question_icon_label.setScaledContents(True)
        self.question_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_icon_label.setObjectName("question_icon_label")
        self.horizontalLayout_7.addWidget(self.question_icon_label)
        self.question_text_label = QtWidgets.QLabel(self.question_frame)
        self.question_text_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.question_text_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.question_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_text_label.setObjectName("question_text_label")
        self.horizontalLayout_7.addWidget(self.question_text_label)
        self.verticalLayout.addWidget(self.question_frame)
        self.github_frame = CustomFrame(RightSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.github_frame.sizePolicy().hasHeightForWidth())
        self.github_frame.setSizePolicy(sizePolicy)
        self.github_frame.setMinimumSize(QtCore.QSize(0, 38))
        self.github_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.github_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.github_frame.setStyleSheet("QFrame\n"
"{\n"
"    background: transparent;\n"
"    border-width:  1px 0px 1px 0px;\n"
"    border-style: solid; \n"
"    border-color: grey transparent grey transparent; \n"
"}")
        self.github_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.github_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.github_frame.setObjectName("github_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.github_frame)
        self.horizontalLayout_6.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.github_icon_label = QtWidgets.QLabel(self.github_frame)
        self.github_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.github_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.github_icon_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.github_icon_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.github_icon_label.setText("")
        self.github_icon_label.setPixmap(QtGui.QPixmap(":/svg/github.svg"))
        self.github_icon_label.setScaledContents(True)
        self.github_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.github_icon_label.setObjectName("github_icon_label")
        self.horizontalLayout_6.addWidget(self.github_icon_label)
        self.github_text_label = QtWidgets.QLabel(self.github_frame)
        self.github_text_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.github_text_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.github_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.github_text_label.setObjectName("github_text_label")
        self.horizontalLayout_6.addWidget(self.github_text_label)
        self.verticalLayout.addWidget(self.github_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.python_frame = CustomFrame(RightSide)
        self.python_frame.setMinimumSize(QtCore.QSize(0, 72))
        self.python_frame.setMaximumSize(QtCore.QSize(16777215, 64))
        self.python_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.python_frame.setStyleSheet("QFrame\n"
"{\n"
"    background: transparent;\n"
"    border-width:  1px 0px 0px 0px;\n"
"    border-style: solid; \n"
"    border-color: grey transparent grey transparent; \n"
"}")
        self.python_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.python_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.python_frame.setObjectName("python_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.python_frame)
        self.horizontalLayout_4.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.python_icon_label = QtWidgets.QLabel(self.python_frame)
        self.python_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.python_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.python_icon_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.python_icon_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.python_icon_label.setText("")
        self.python_icon_label.setPixmap(QtGui.QPixmap(":/svg/pythonUY1.svg"))
        self.python_icon_label.setScaledContents(True)
        self.python_icon_label.setObjectName("python_icon_label")
        self.horizontalLayout_4.addWidget(self.python_icon_label)
        self.python_text_label = QtWidgets.QLabel(self.python_frame)
        self.python_text_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.python_text_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.python_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.python_text_label.setObjectName("python_text_label")
        self.horizontalLayout_4.addWidget(self.python_text_label)
        self.verticalLayout.addWidget(self.python_frame)
        self.telegram_frame = CustomFrame(RightSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.telegram_frame.sizePolicy().hasHeightForWidth())
        self.telegram_frame.setSizePolicy(sizePolicy)
        self.telegram_frame.setMinimumSize(QtCore.QSize(0, 38))
        self.telegram_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.telegram_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.telegram_frame.setStyleSheet("QFrame\n"
"{\n"
"    background: transparent;\n"
"    border-width:  1px 0px 1px 0px;\n"
"    border-style: solid; \n"
"    border-color: grey transparent grey transparent; \n"
"}")
        self.telegram_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.telegram_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.telegram_frame.setObjectName("telegram_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.telegram_frame)
        self.horizontalLayout_5.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.telegram_icon_label = QtWidgets.QLabel(self.telegram_frame)
        self.telegram_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.telegram_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.telegram_icon_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.telegram_icon_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.telegram_icon_label.setText("")
        self.telegram_icon_label.setPixmap(QtGui.QPixmap(":/svg/telegram.svg"))
        self.telegram_icon_label.setScaledContents(True)
        self.telegram_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.telegram_icon_label.setObjectName("telegram_icon_label")
        self.horizontalLayout_5.addWidget(self.telegram_icon_label)
        self.telegram_text_label = QtWidgets.QLabel(self.telegram_frame)
        self.telegram_text_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.telegram_text_label.setStyleSheet("QLabel\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.telegram_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.telegram_text_label.setObjectName("telegram_text_label")
        self.horizontalLayout_5.addWidget(self.telegram_text_label)
        self.verticalLayout.addWidget(self.telegram_frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(RightSide)
        QtCore.QMetaObject.connectSlotsByName(RightSide)

    def retranslateUi(self, RightSide):
        _translate = QtCore.QCoreApplication.translate
        RightSide.setWindowTitle(_translate("RightSide", "Form"))
        self.code_text_label.setText(_translate("RightSide", "Code source"))
        self.question_text_label.setText(_translate("RightSide", "Poser un probleme"))
        self.github_text_label.setText(_translate("RightSide", "Voir sur Github"))
        self.python_text_label.setText(_translate("RightSide", "By PYUY1 2019"))
        self.telegram_text_label.setText(_translate("RightSide", "Voir sur telegram"))


from . import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RightSide = QtWidgets.QWidget()
    ui = Ui_RightSide()
    ui.setupUi(RightSide)
    RightSide.show()
    sys.exit(app.exec_())
