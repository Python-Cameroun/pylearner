from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
import icons_rc 
import random
from right_side import RightSide
from ui_main_window import Ui_MainWindow


SAMPLE_COMMENTS = """
    Hmm. We’re having trouble finding that site.\n
We can’t connect to the server at fr.wikipedia.org.\n
If that address is correct, here are three other things you can try:\n
    Try again later.\n
    Check your network connection.\n    
    If you are connected but behind a firewall, check that Firefox has permission to access the Web.
    But you should know that i don't give a fuck about what they think about me
    I am a though nigga and I can shit everybody for your love
    Je ne sais meme plus quoi ecrire mais je veux juste remplir les lignes
    Ce motherfucker texte me fiche deje les jetons. J'en ai marre
    Aparement je dois continuer d'ecrire je ne sais quoi
    Mais il faut quand meme que je continue
    Je ne sais pas si tout va bien mais ca ira sans aucun doute
    Je suis sure que tout ira bien
    Je ne sais pas qui est Malcomn X
    Davido est un chanteur Africain et Chris Brown un Americain

    Drake est mon meilleur rappeur US. J'aime pratiquement tous ces sons
    Je ne suis pas un musicien de quel que sorte que ce soit car je sne suis pas talentueux
    Je pourrai bien entrainer mes enfants plus tard a jouer des instruments car c'est bien pour ameliorer leur QI
    
"""

TEXT_STYLE1 = """QLabel\n
        {\n
               font-weight: bold;\n
        }"""

TEXT_STYLE2 = """QLabel\n
        {\n
               font-weight: bold;\n
               font-size: 18px;\n
        }"""

FRAME_STYLE = """QFrame\n
        {\n
               background-color: #28d;\n
        }"""

FRAME_STYLE1 = """QFrame\n
        {\n
               background-color: #6fd;\n
        }"""














class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400, 600)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.layout = QtWidgets.QHBoxLayout(self.ui.main_page)
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.left_side = LeftSide()
        self.splitter.addWidget(self.left_side)
        self.central_side = CentralSide()
        self.splitter.addWidget(self.central_side)
        self.right_side = RightSide()
        self.splitter.addWidget(self.right_side)
        self.layout.addWidget(self.splitter)



class MediaControl(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MediaControl, self).__init__(parent)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setMinimumSize(QtCore.QSize(0, 48))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 48))
        self.frame.setStyleSheet(FRAME_STYLE)

        self.frame_layout = QtWidgets.QHBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(12, 0, 12, 0)
        self.frame_layout.setSpacing(6)

        spacerItem = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_layout.addItem(spacerItem)

        self.forward_label = QtWidgets.QLabel(self.frame)
        self.forward_label.setPixmap(QtGui.QPixmap(":/svg/md-skip-forward.svg"))

        self.pause_label = QtWidgets.QLabel(self.frame)
        self.pause_label.setText("||")
        #self.icon_label.setPixmap(QtGui.QPixmap(":/svg/angle-arrow-down.svg"))

        self.backward_label = QtWidgets.QLabel(self.frame)
        self.backward_label.setPixmap(QtGui.QPixmap(":/svg/md-skip-backward.svg"))

        for label in (self.backward_label, self.pause_label, self.forward_label):
            label.setScaledContents(True)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setMaximumSize(QtCore.QSize(18,18))
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.frame_layout.addWidget(label)

        spacerItem2 = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frame_layout.addItem(spacerItem2)

        self.layout.addWidget(self.frame)



class CentralSide(QtWidgets.QWidget):
    f_number = 0
    s_number = 0
    title = ""
    def __init__(self, f_number=0, s_number=0, title="TItle", parent=None):
        super(CentralSide, self).__init__(parent)
        self.f_number = f_number
        self.s_number = s_number
        self.title = title

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 32, 0, 0)
        
        self.title_label = QtWidgets.QLabel(self)
        self.title_label.setStyleSheet(TEXT_STYLE2)
        self.title_label.setText("{}.{} {}".format(self.f_number, self.s_number, self.title))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setStyleSheet(TEXT_STYLE2)        

        self.media_player_frame = QtWidgets.QFrame(self)
        self.media_player_frame.setStyleSheet(FRAME_STYLE1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.media_player_frame.sizePolicy().hasHeightForWidth())
        self.media_player_frame.setSizePolicy(sizePolicy)        
        self.media_player_frame.setMinimumSize(QtCore.QSize(500, 500))
        self.media_player_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))        

        self.media_layout = QtWidgets.QVBoxLayout(self.media_player_frame)
        self.media_layout.setContentsMargins(0,0,0,0)
        
        self.media_player = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        
        
        self.media_controler = MediaControl()        

        self.media_layout.addWidget(self.video_widget)
        self.media_layout.addWidget(self.media_controler)
        
        
        self.scroll_text = QtWidgets.QScrollArea(self)
        size_policy =  QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.scroll_text.sizePolicy().hasHeightForWidth())
        self.scroll_text.setSizePolicy(size_policy)
        self.scroll_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_text.setWidgetResizable(True)
        self.comment_layout = QtWidgets.QVBoxLayout(self.scroll_text)
        self.comment_title_label = QtWidgets.QLabel(self)
        self.comment_title_label.setText("Comments title:")
        self.comment_title_label.setStyleSheet(TEXT_STYLE1)
        self.comment_layout.addWidget(self.comment_title_label)

        self.comment_content_label = QtWidgets.QLabel()
        self.comment_content_label.setWordWrap(True)
        self.comment_content_label.setText(SAMPLE_COMMENTS)
        self.comment_layout.addWidget(self.comment_content_label)
        
        self.layout.addWidget(self.title_label)
        #self.layout.addLayout(self.media_layout)
        self.layout.addWidget(self.media_player_frame)
        self.layout.addWidget(self.scroll_text)
        self.layout.setStretch(1,1)
        self.layout.setStretch(1, 3)
        

        



if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    collapse = CentralSide()
    collapse.show()
    sys.exit(app.exec_())
    





