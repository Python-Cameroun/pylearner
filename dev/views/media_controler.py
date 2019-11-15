from PyQt5.QtWidgets import QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QSlider, QStyle, QLabel, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtMultimedia import QMultimedia, QMediaPlayer, QAudio
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import qRound, pyqtSignal, QTime
from PyQt5 import Qt



class MediaControler(QFrame):
    
    play_clicked = pyqtSignal()
    stop_clicked = pyqtSignal()
    mute_clicked = pyqtSignal()
    volume_changed = pyqtSignal(int)
    position_changed = pyqtSignal(int)
    
    
    def __init__(self, parent=None):
        super(MediaControler, self).__init__(parent)
        
        self.state = QMediaPlayer.State()
        self.muted = False        
        
        self.layout = QVBoxLayout(self)
        
        self.up_layout = QHBoxLayout(self)
        
        self.remaining_time_label = QLabel(self)
        self.remaining_time_label.setText("--:--")
        self.up_layout.addWidget(self.remaining_time_label)
        
        self.evolution_slider = QSlider(Qt.Qt.Horizontal, self)
        self.evolution_slider.setRange(0, 100)
        self.up_layout.addWidget(self.evolution_slider)        
        
        self.total_time_label = QLabel(self)
        self.total_time_label.setText("--:--")
        self.up_layout.addWidget(self.total_time_label)    
        
        self.layout.addLayout(self.up_layout)
        
        self.sub_layout = QHBoxLayout(self)
        
        
        self.play_button = QToolButton(self)
        self.play_button.setMinimumSize(36, 36)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.sub_layout.addWidget(self.play_button)        
        
               
        
        self.backward_button = QToolButton(self)
        self.backward_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.sub_layout.addWidget(self.backward_button)        
        
        
        self.stop_button = QToolButton(self)
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.sub_layout.addWidget(self.stop_button)         
        
        self.forward_button = QToolButton(self)
        self.forward_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.sub_layout.addWidget(self.forward_button) 
        
        self.full_screen_button = QToolButton(self)
        #self.full_screen_button.setCheckable(True)
        self.full_screen_button.setToolTip("Afficher en mode plein ecran")
        self.full_screen_button.setIcon(self.style().standardIcon(QStyle.SP_DesktopIcon))
        self.sub_layout.addWidget(self.full_screen_button)        
        
        self.mute_button = QToolButton(self)
        self.mute_button.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.sub_layout.addWidget(self.mute_button)    
        
        
        self.volume_slider = QSlider(Qt.Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.setMaximumWidth(100)
        self.sub_layout.addWidget(self.volume_slider)    
        
        self.volume_label = QLabel(self)
        self.volume_label.setText("0%")
        self.sub_layout.addWidget(self.volume_label)
        
        spacerItem = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.sub_layout.addItem(spacerItem)
        
        self.layout.addLayout(self.sub_layout)
        
        self.setStyleSheet(
        """
        QFrame
        {
        background-color: beige;
        border: 1px solid grey;
        }
        """
        )
        
        self.setMaximumHeight(80)
        
        
        self.play_button.clicked.connect(self.play)
        self.stop_button.clicked.connect(self.stop)
        self.volume_slider.valueChanged.connect(self.update_volume)
        self.mute_button.clicked.connect(self.set_muted)
        
        
        
    def set_state(self, state):
        
        if state == QMediaPlayer.StoppedState:
            self.stop_button.setEnabled(False)
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        elif state == QMediaPlayer.PlayingState:
            self.stop_button.setEnabled(True)
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        elif state == QMediaPlayer.PausedState:
            self.stop_button.setEnabled(True)
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        
        self.state = state
    
    
    def volume(self):
        linear_volume = QAudio.convertVolume(self.volume_slider.value()/100,
                                             QAudio.LogarithmicVolumeScale,
                                             QAudio.LinearVolumeScale)
        
        return qRound(linear_volume * 100)
        
        
    
    def set_volume(self, volume):
        log_volume = QAudio.convertVolume(volume / 100, 
                                          QAudio.LinearVolumeScale,
                                          QAudio.LogarithmicVolumeScale)
        
    def update_volume(self):
        vol = self.volume()
        self.volume_changed.emit(vol)
        self.volume_label.setText("{}%".format(vol))
        
        
    def position_changed(self, position):
        self.evolution_slider.setValue(position)
        
    def update_position(self):
        pass
    
    
    def update_times(self, duration):
        print("Je vais mettre a jour le temps avec {}".format(duration))
        
    
    def duration_changed(self, duration):
        self.evolution_slider.setRange(0, duration)
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(duration)
        self.total_time_label.setText(mtime.toString())
        
    def update_time_label(self, position):
        #self.lbl.clear()
        mtime = QTime(0,0,0,0)
        self.time = mtime.addMSecs(position)
        self.remaining_time_label.setText(self.time.toString())
        self.evolution_slider.setValue(position)
        
        
    def set_muted(self):
        muted = self.muted
        icon = QStyle.SP_MediaVolumeMuted if muted else QStyle.SP_MediaVolume
        self.mute_button.setIcon(self.style().standardIcon(icon))
        self.muted = not self.muted
        

            
    def play(self):
        if self.state == QMediaPlayer.PlayingState:
            self.set_state(QMediaPlayer.PausedState)
        else:
            self.set_state(QMediaPlayer.PlayingState)
        self.play_clicked.emit()
        
    def stop(self):
        if self.state == QMediaPlayer.PlayingState:
            self.set_state(QMediaPlayer.StoppedState)
            self.stop_clicked.emit()
            
    
    
    
    
    
if __name__=='__main__':
    
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    control = MediaControler()
    control.show()
    sys.exit(app.exec_())
        