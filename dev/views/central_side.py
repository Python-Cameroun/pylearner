from PyQt5 import QtWidgets, QtMultimedia, QtMultimediaWidgets, QtCore

from .assets.central_side_ui import Ui_CentralSide



from .video_player import *
from .media_controler import *

class CentralSide(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(CentralSide, self).__init__(parent)
        self.ui = Ui_CentralSide()
        self.ui.setupUi(self)
        
        
        self.video_widget = VideoPlayer()
                
        self.frame_layout = QtWidgets.QVBoxLayout(self.ui.video_player_frame)
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_layout.setSpacing(0)
        
        self.media_controler = MediaControler()
        self.media_controler.setWindowFlag(Qt.Qt.ToolTip)        
        
        self.frame_layout.addWidget(self.video_widget)
        self.frame_layout.addWidget(self.media_controler)
        
        self.media_controler.play_clicked.connect(self.video_widget.play)
        #self.video_widget.clicked.connect(lambda : self.media_controler.set_state(QMediaPlayer.))
        
        self.media_controler.stop_clicked.connect(self.video_widget.stop)
        self.media_controler.full_screen_button.clicked.connect(self.video_widget.set_fullscreen)
        self.media_controler.volume_changed.connect(lambda x: self.video_widget.set_volume(x))
        self.video_widget.media_player.durationChanged.connect(self.media_controler.duration_changed)
        self.video_widget.media_player.positionChanged.connect(lambda: 
                                self.media_controler.update_time_label(self.video_widget.media_player.position()))
        
        self.media_controler.evolution_slider.valueChanged.connect(self.video_widget.update_position)
        
        self.video_widget.load_video("../snippets/video.mp4")
        
        
    def open_file(self, file_name):
        self.media_controler.stop()
        self.video_widget.load_video(file_name)
        self.media_controler.play()
        
        
        
        
if __name__=='__main__':
    
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    ui = CentralSide()
    ui.show()
    sys.exit(app.exec_())