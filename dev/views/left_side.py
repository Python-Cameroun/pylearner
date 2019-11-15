from PyQt5 import QtWidgets, QtCore
from .assets.utils import *
from .collapsible_box import *

class LeftSide(QtWidgets.QWidget):
    item_choosed = QtCore.pyqtSignal(str)
    def __init__(self, parent=None, content=[]):
        super(LeftSide, self).__init__(parent)
        self.setMinimumWidth(200)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 12, 0, 12)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        
        

        self.create_scroll_layout()

        self.somaire_label = QtWidgets.QLabel("Sommaire")
        self.somaire_label.setAlignment(QtCore.Qt.AlignCenter)
        self.somaire_label.setStyleSheet(TEXT_STYLE1)
        self.layout.addWidget(self.somaire_label)
        
        self.set_content(content)
        
    def create_scroll_layout(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.setContentsMargins(0, 12, 0, 12)        
    
    def set_content(self, content:list):
        old_lay = self.scroll_layout
        del old_lay
        self.create_scroll_layout()
        for c in content:
            tg = CollapsibleBox(self.scrollAreaWidgetContents)
            tg.set_content(c)
            tg.item_choosed.connect(lambda x: self.item_choosed.emit(x))
            self.scroll_layout.addWidget(tg)
        self.scroll_layout.setSizeConstraint(QtWidgets.QHBoxLayout.SetMinimumSize)
        
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scroll_area)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scroll_layout.addItem(spacerItem)        
        self.layout.setStretch(1, 0)        


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    collapse = LeftSide()
    collapse.show()
    sys.exit(app.exec_())