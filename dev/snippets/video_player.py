from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimedia, QtMultimediaWidgets

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        
        #self.frame = QtWidgets.QFrame()
        self.setMinimumSize(600, 400)
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.player = QtMultimedia.QMediaPlayer(self)
        self.player.setAudioRole(QtMultimedia.QAudio.VideoRole)
        
        self.playlist = QtMultimedia.QMediaPlaylist(self.player)
        self.playlist.addMedia(QtMultimedia.QMediaContent(self.playlist, QtCore.QUrl("video.mp4")))
        
        self.video_widget = QtMultimediaWidgets.QVideoWidget(self)
        self.player.setVideoOutput(self.video_widget)
        
        self.layout.addWidget(self.video_widget)
        
        self.video_widget.show()
        self.playlist.setCurrentIndex(1)
        self.player.play()
    
        
        
        
if __name__=="__main__":
    
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    vidp = VideoPlayer()
    vidp.show()
    
    sys.exit(app.exec_())