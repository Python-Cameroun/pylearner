from PyQt5 import QtWidgets, QtCore, QtGui
from views.left_side import LeftSide
from views.central_side import CentralSide
from views.right_side import RightSide
from views.assets.ui_main_window import Ui_MainWindow
from course_index import *

class MainWindow(QtWidgets.QMainWindow):
    item_choosed = QtCore.pyqtSignal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400, 300)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menubar.hide()
        self.layout = QtWidgets.QHBoxLayout(self.ui.main_page)
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.left_side = LeftSide()
        self.splitter.addWidget(self.left_side)
        self.central_side = CentralSide()
        self.splitter.addWidget(self.central_side)
        self.right_side = RightSide()
        self.splitter.addWidget(self.right_side)
        self.layout.addWidget(self.splitter)
        self.ui.pushButton.clicked.connect(self.connexion)
        self.ui.actionOuvrir.triggered.connect(self.open_file)
        self.ui.actionPlein_ecran.triggered.connect(self.full_screen)
        self.ui.actionQuitter.triggered.connect(lambda: self.close())
        self.ui.actionNouveau.triggered.connect(self.create_index_file)
        self.left_side.item_choosed.connect(self.load_video)
        
        


    def connexion(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.menubar.show()
        
        
    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Index file",
                                                  QtCore.QDir.homePath(), "Text FIle(*.json)")    
        if fileName:
            self.loader = CourseInderLoader(fileName)
            self.left_side.set_content(self.loader.get_parts())
        
        self.base_dir = fileName.replace("index.json", "")
            
    def load_video(self, rpath):
        self.central_side.open_file(self.base_dir+rpath)
            
            
    def full_screen(self):
        self.central_side.video_widget.set_fullscreen()
        
        
    def create_index_file(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", QtCore.QDir.homePath())
        if folder:
            gen = CourseIndexGenerator(base_folder=folder)
            gen.load_courses_folder()
            gen.build_all_courses()
            gen.save_all()
        
        
if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
