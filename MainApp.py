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
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



Builder.load_string("""
<MenuScreen>:
    canvas.before:
        Rectangle:
            pos: 0, 0
            size: 700, 480
            source: 'Images/BG.png'
            
    Button:
        text: 'Navigation'
        id: NAV
        pos: 20, 10
        size_hint: None, None
        size: 150, 40
        background_color: (0.5, 0.0, 0.0, 0.5)
        on_press: root.manager.current = 'nav'

    Button:
        text: 'Weather'
        id: WEATH
        pos: 190, 10
        size_hint: None, None
        size: 150, 40
        background_color: (0.5, 0.0, 0.0, 0.5)
        on_press: root.manager.current = 'wth'
    
    Button:
        text: 'Camera'
        id: CAM
        pos: 360, 10
        size_hint: None, None
        size: 150, 40
        background_color: (0.5, 0.0, 0.0, 0.5)
        on_press: root.manager.current = 'cam'
    
    Button:
        text: 'Engine Data'
        id: ENG
        pos: 530, 10
        size_hint: None, None
        size: 150, 40
        background_color: (0.5, 0.0, 0.0, 0.5)
        on_press: root.manager.current = 'eng'
        
    Button: 
        text: 'Exit'
        id: EXT
        pos: 590, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.9, 0.0, 0.0, 0.75)
        on_press: app.stop()

    Button: 
        text: 'Settings'
        id: STG
        pos: 10, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.18, 0.38, 0.70, 0.75)
        on_press: root.manager.current = 'set'


<SettingsScreen>:
    canvas.before:
        Rectangle:
            pos: 0, 0
            size: 700, 480
            source: 'Images/BG_Empty.png'
            
    Button: 
        text: 'Exit'
        id: EXT
        pos: 590, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.9, 0.0, 0.0, 0.75)
        on_press: app.stop()

    Button: 
        text: 'Back'
        id: STG
        pos: 10, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.18, 0.38, 0.70, 0.75)
        on_press: root.manager.current = 'menu'   


<NavigationScreen>:
    canvas.before:
        Rectangle:
            pos: 0, 0
            size: 700, 480
            source: 'Images/BG_Empty.png'
            
    canvas:
        Rectangle:
            pos: 10, 10
            size: 680, 415
            source: 'Images/Navigation_Example.png'
            
    TextInput:
        text: 'Destination'
        pos: 130, 430
        size_hint: None, None
        size: 400, 40
        
    Button: 
        text: '->'
        id: EXT
        pos: 530, 430
        size_hint: None, None
        size: 40, 40
        background_color: (0.0, 0.9, 0.0, 0.75)
        
        
            
    Button: 
        text: 'Exit'
        id: EXT
        pos: 590, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.9, 0.0, 0.0, 0.75)
        on_press: app.stop()

    Button: 
        text: 'Back'
        id: STG
        pos: 10, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.18, 0.38, 0.70, 0.75)
        on_press: root.manager.current = 'menu' 
        
<WeatherScreen>:
    canvas.before:
        Rectangle:
            pos: 0, 0
            size: 700, 480
            source: 'Images/BG_Empty.png'
    
    canvas:
        Rectangle:
            pos: 10, 70
            size: 680, 345
            source: 'Images/Weather_Example.png'
  
    Button: 
        text: 'Exit'
        id: EXT
        pos: 590, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.9, 0.0, 0.0, 0.75)
        on_press: app.stop()

    Button: 
        text: 'Back'
        id: STG
        pos: 10, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.18, 0.38, 0.70, 0.75)
        on_press: root.manager.current = 'menu' 
        
    TextInput:
        text: 'Location'
        pos: 130, 430
        size_hint: None, None
        size: 400, 40
        
    Button: 
        text: '->'
        id: EXT
        pos: 530, 430
        size_hint: None, None
        size: 40, 40
        background_color: (0.0, 0.9, 0.0, 0.75)   
        
    Label:
        text: '[b][size=32][color=000000] Buffalo, NY [/color][/size][/b]'
        markup: True
        pos: 0, -200
        
        
    Label:
        text: '[b][size=12][color=000000] [ May 12 2017 - May 21 2017 ] [/color][/size][/b]'
        markup: True
        pos: 0, -225
        
        
<CameraScreen>:
    canvas.before:
        Rectangle:
            pos: 0, 0
            size: 700, 480
            source: 'Images/BG_Empty.png'
            
    canvas:
        Rectangle:
            pos: 10, 10
            size: 680, 415
            source: 'Images/Camera_Example.png'
    
    Button: 
        text: 'Capture Image'
        id: CPT_I
        pos: 180, 430
        size_hint: None, None
        size: 110, 40
        background_color: (0.1, 0.1, 0.1, 0.75)
    
    Button: 
        text: 'Capture Video'
        id: CPT_V
        pos: 300, 430
        size_hint: None, None
        size: 110, 40
        background_color: (0.1, 0.1, 0.1, 0.75)
    
    Button: 
        text: 'Timelapse'
        id: CPT_TL
        pos: 420, 430
        size_hint: None, None
        size: 110, 40
        background_color: (0.1, 0.1, 0.1, 0.75)
          
            
    Button: 
        text: 'Exit'
        id: EXT
        pos: 590, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.9, 0.0, 0.0, 0.75)
        on_press: app.stop()

    Button: 
        text: 'Back'
        id: STG
        pos: 10, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.18, 0.38, 0.70, 0.75)
        on_press: root.manager.current = 'menu' 
        
<EngineScreen>:
    canvas.before:
        Rectangle:
            pos: 0, 0
            size: 700, 480
            source: 'Images/BG_Empty.png'
            
    Button: 
        text: 'Exit'
        id: EXT
        pos: 590, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.9, 0.0, 0.0, 0.75)
        on_press: app.stop()

    Button: 
        text: 'Back'
        id: STG
        pos: 10, 430
        size_hint: None, None
        size: 100, 40
        background_color: (0.18, 0.38, 0.70, 0.75)
        on_press: root.manager.current = 'menu' 
        
""")


class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class NavigationScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class EngineScreen(Screen):
    pass


Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '480')


# Create the screen manager
sm = ScreenManager(transition=FadeTransition())

sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='set'))
sm.add_widget(NavigationScreen(name='nav'))
sm.add_widget(WeatherScreen(name='wth'))
sm.add_widget(CameraScreen(name='cam'))
sm.add_widget(EngineScreen(name='eng'))

sm.current = 'menu'


class AutoApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    AutoApp().run()