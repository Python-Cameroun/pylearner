#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import  QKeySequence, QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QDir, Qt, QUrl, QPoint, QTime, QProcess, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLineEdit,
                             QPushButton, QSlider, QMessageBox, QStyle, QVBoxLayout,  
                            QWidget, QShortcut, QMenu)
import sys
import os
import subprocess
from .media_controler import *
#QT_DEBUG_PLUGINS

class VideoPlayer(QVideoWidget):
   
   #doubleClicked = pyqtSignal()
   clicked = pyqtSignal()
   #keyPressed = pyqtSignal()
   #rtime_changed = pyqtSignal(str)
   #duration_changed = pyqtSignal(int)

   def __init__(self, parent=None):
      super(VideoPlayer, self).__init__(parent)
      
      self.playing = False
      self.full_screen = False
            
      self.media_player = QMediaPlayer()
      
      self.media_player.setVideoOutput(self)
      
      self.widescreen = True
      
      self.media_player.setVolume(0)
      
      
      
   def load_video(self, path):
      self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))      
      
   def play(self):
      if self.playing is False:
         self.media_player.play()
         self.playing = True
      else:
         self.media_player.pause()
         self.playing = False      
      
   def stop(self):
      self.media_player.stop()
      self.playing = False
      
   def set_volume(self, volume):
      self.media_player.setVolume(volume)
      
   def mousePressEvent(self, event):
      #self.play()
      self.clicked.emit()
      super(VideoPlayer, self).mousePressEvent(event)
      
      
   def update_position(self, position):
      self.media_player.setPosition(position)
      
      
   def set_postion(self, position):
      self.media_player.setPosition(position)

   
   def mouseDoubleClickEvent(self, event):
      self.set_fullscreen()
      
   def set_fullscreen(self):
      self.setFullScreen(not self.isFullScreen())
   
   def keyPressEvent(self, event):
      if event.key() == Qt.Qt.Key_Escape and self.isFullScreen():
         self.setFullScreen(False)         
         event.accept()
      else:
         super(VideoPlayer, self).keyPressEvent(event)
      
      
      