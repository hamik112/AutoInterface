'''

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| |A|U|T|O|M|O|T|I|V|E| |I|N|T|E|R|F|A|C|E| |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

@author: Joseph Hanson
@version: 0.10
@since: 3/31/17

'''

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import webview
from threading import Thread
from kivy.loader import Loader
import sys
import time


class Camera(Widget):

    def __init__(self):
        super(Camera, self).__init__()

        self.CameraImage = Loader.image('http://192.168.42.1/mjpeg/amba.jpg')
        """self.CameraImage.size=(800, 600)"""
        self.CameraImage.pos=(0, 0)

        self.exitbutton = Button(text='exit',
                                 size=(40, 40),
                                 pos=(10, 10))
        self.exitbutton.bind(on_press=self.Exit)

        self.add_widget(self.CameraImage)
        self.add_widget(self.exitbutton)

    def Exit(self, *args):
        sys.exit(0)


class CameraApp(App):
    def build(self):
        return Camera()


if __name__ == '__main__':
    CameraApp().run()
