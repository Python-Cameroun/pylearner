from PyQt5 import QtWidgets, QtCore, QtGui
import webbrowser
from .assets.ui_right_side import Ui_RightSide
from .assets import icons_rc
from .config import *

class RightSide(QtWidgets.QWidget):
    see_code = QtCore.pyqtSignal()
    ask_question = QtCore.pyqtSignal()
    goto_site = QtCore.pyqtSignal()
    goto_github = QtCore.pyqtSignal()
    goto_telegram = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(RightSide, self).__init__(parent)
        self.ui = Ui_RightSide()
        self.ui.setupUi(self)
        self.ui.code_frame.clicked.connect(self.see_code)
        self.ui.question_frame.clicked.connect(self.ask_question)
        self.ui.telegram_frame.clicked.connect(self.goto_telegram_clicked)
        self.ui.python_frame.clicked.connect(self.goto_site_clicked)
        self.ui.github_frame.clicked.connect(self.goto_github_clicked)

    
    def see_code(self):
        webbrowser.open(GITHUB_ACCOUNT)
    
    def ask_question(self):
        webbrowser.open(TELEGRAM_GROUP)
    
    def goto_site_clicked(self):
        webbrowser.open(PYCM_SITE)
    
    def goto_telegram_clicked(self):
        webbrowser.open(TELEGRAM_GROUP)
    
    def goto_github_clicked(self):
        webbrowser.open(GITHUB_ACCOUNT)





if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rs = RightSide()
    rs.show()
    sys.exit(app.exec_())