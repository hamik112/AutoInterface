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

from kivy.lang import Builder
from kivy.properties import ObjectProperty  #@UnresolvedImport
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.garden.mapview import MapView, MapMarker  #@UnresolvedImport
from KivyCalendar import CalendarWidget
import pickle

from uuid import uuid4

import time
import sys
from threading import Thread
import webview
from weather import Weather
from kivy.core.window import Window
from kivy.clock import Clock

import geocoder
import pyowm

from functools import partial
import os.path
from kivy.config import Config

Config.set('graphics','borderless',1)
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', '1900')
Config.set('graphics', 'top', '100')

from kivy.core.window import Window
Window.size = (800, 480)
Window.top = 100
Window.left = 1900
#Window.rotation = 180

"""
    INITIALIZATION FUNCTIONS
"""



def initScreenManager():
    
    """
    Handle Screen Manager
    """
    global sm
    sm = ScreenManager(transition=FadeTransition())
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(MenuScreen2(name='menu2'))
    sm.add_widget(SettingsScreen(name='set'))
    sm.add_widget(NavigationScreen(name='nav'))
    sm.add_widget(WeatherScreen(name='wth'))
    sm.add_widget(CameraScreen(name='cam'))
    sm.add_widget(EngineScreen(name='eng'))
    sm.add_widget(MessagingScreen(name='msg'))
    sm.add_widget(CalendarScreen(name='cldr'))
    sm.add_widget(SportsScreen(name='sprts'))
    sm.add_widget(TasksScreen(name='tsks'))

    sm.current = 'menu'
    
    

"""
    KIVY MENU-SCREEN CLASSES
"""

class MenuScreen(Screen):
    
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.BackButton = Button(text='',
                                 pos=(10, 10),
                                 size_hint=(None, None),
                                 size=(65, 40),
                                 background_color=(0.5, 0.5, 0.5, 0.5))
        
        self.ForwardButton = Button(text='>',
                                 pos=(725, 10),
                                 size_hint=(None, None),
                                 size=(65, 40),
                                 background_color=(0.5, 0.5, 0.5, 0.5))
        self.ForwardButton.bind(on_press=self.openMenu2Screen)
        
        self.SettingsButton = Button(text='Settings',
                                     pos=(10, 430),
                                     size_hint=(None, None),
                                     size=(100, 40),
                                     background_color=(0.18, 0.38, 0.70, 0.75))
        self.SettingsButton.bind(on_press=self.openSettingsScreen)
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.NavigationButton = Button(text='Navigation',
                                       pos=(85, 10),
                                       size_hint=(None, None),
                                       size=(150, 40),
                                       background_color=(0.5, 0.0, 0.0, 0.5))
        self.NavigationButton.bind(on_press=self.openNavigationScreen)
        
        self.WeatherButton = Button(text='Weather',
                                    pos=(245, 10),
                                    size_hint=(None, None),
                                    size=(150, 40),
                                    background_color=(0.5, 0.0, 0.0, 0.5))
        self.WeatherButton.bind(on_press=self.openWeatherScreen)
        
        self.CameraButton = Button(text='Camera',
                                    pos=(405, 10),
                                    size_hint=(None, None),
                                    size=(150, 40),
                                    background_color=(0.5, 0.0, 0.0, 0.5))
        self.CameraButton.bind(on_press=self.openCameraScreen)
        
        self.EngineButton = Button(text='Engine Data',
                                    pos=(565, 10),
                                    size_hint=(None, None),
                                    size=(150, 40),
                                    background_color=(0.5, 0.0, 0.0, 0.5))
        self.EngineButton.bind(on_press=self.openEngineScreen)
        
        
        
        # Add all components to the screen
        self.add_widget(self.Background)
        self.add_widget(self.BackButton)
        self.add_widget(self.ForwardButton)
        self.add_widget(self.ExitButton)
        self.add_widget(self.NavigationButton)
        self.add_widget(self.WeatherButton)
        self.add_widget(self.CameraButton)
        self.add_widget(self.EngineButton)
        self.add_widget(self.SettingsButton)

    def exitApplication(self, *args):
        App.get_running_app().stop()    
        
    def openMenu2Screen(self, *args):
        sm.current = 'menu2'
    
    def openNavigationScreen(self, *args):
        sm.current = 'nav'
        
    def openWeatherScreen(self, *args):
        sm.current = 'wth'
        
    def openCameraScreen(self, *args):
        sm.current = 'cam'
        
    def openEngineScreen(self, *args):
        sm.current = 'eng'
        
    def openSettingsScreen(self, *args):
        sm.current = 'set'

class MenuScreen2(Screen):
    
    def __init__(self, **kwargs):
        super(MenuScreen2, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.SettingsButton = Button(text='Settings',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.SettingsButton.bind(on_press=self.openSettingsScreen)
        
        self.BackButton = Button(text='<',
                                 pos=(10, 10),
                                 size_hint=(None, None),
                                 size=(65, 40),
                                 background_color=(0.5, 0.5, 0.5, 0.5))
        self.BackButton.bind(on_press=self.openMenuScreen)
        
        self.ForwardButton = Button(text='',
                                 pos=(725, 10),
                                 size_hint=(None, None),
                                 size=(65, 40),
                                 background_color=(0.5, 0.5, 0.5, 0.5))
        
        self.MessagingButton = Button(text='Messaging',
                                      pos=(85, 10),
                                      size_hint=(None, None),
                                      size=(150, 40),
                                      background_color=(0.5, 0.0, 0.0, 0.5))
        self.MessagingButton.bind(on_press=self.openMessagingScreen)
        
        self.CalendarButton = Button(text='Calendar',
                                      pos=(245, 10),
                                      size_hint=(None, None),
                                      size=(150, 40),
                                      background_color=(0.5, 0.0, 0.0, 0.5))
        self.CalendarButton.bind(on_press=self.openCalendarScreen)
        
        self.SportsButton = Button(text='Sports',
                                   pos=(405, 10),
                                   size_hint=(None, None),
                                   size=(150, 40),
                                   background_color=(0.5, 0.0, 0.0, 0.5))
        self.SportsButton.bind(on_press=self.openSportsScreen)
        
        self.TasksButton = Button(text='Tasks',
                                   pos=(565, 10),
                                   size_hint=(None, None),
                                   size=(150, 40),
                                   background_color=(0.5, 0.0, 0.0, 0.5))
        self.TasksButton.bind(on_press=self.openTasksScreen)
        
        
        
        # Add all components to the Screen
        self.add_widget(self.Background )
        self.add_widget(self.ExitButton )
        self.add_widget(self.SettingsButton )
        self.add_widget(self.BackButton )
        self.add_widget(self.ForwardButton )
        self.add_widget(self.MessagingButton )
        self.add_widget(self.CalendarButton )
        self.add_widget(self.SportsButton )
        self.add_widget(self.TasksButton )

    def exitApplication(self, *args):
        App.get_running_app().stop()
        
    def openSettingsScreen(self, *args):
        sm.current = 'set'    
        
    def openMenuScreen(self, *args):
        sm.current = 'menu'
        
    def openMessagingScreen(self, *args):
        sm.current = 'msg'
        
    def openCalendarScreen(self, *args):
        sm.current = 'cldr'
        
    def openSportsScreen(self, *args):
        sm.current = 'sprts'
        
    def openTasksScreen(self, *args):
        sm.current = 'tsks'

class SettingsScreen(Screen):
    
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)

        # Add all components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
        
    def exitApplication(self, *args):
        App.get_running_app().stop()  
       
    def BackToMenu(self, *args):
        sm.current = 'menu'


"""
    MENU 1: SCREEN CLASSES
"""        
class NavigationScreen(Screen):
    
    def __init__(self, **kwargs):
        super(NavigationScreen, self).__init__(**kwargs)
        
        #self.size=(800, 480)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        
        self.Map = MapView(zoom=1,
                           lat=42.8982149,
                           lon=-78.8672276,
                           pos=(10, 10),
                           size_hint=(None, None),
                           size=(780, 415))
        
        
        self.Destination = TextInput(text='Destination',
                                     multiline=False,
                                     pos=(130, 430),
                                     size_hint=(None, None),
                                     size=(500, 40))
        self.Destination.bind(on_text_validate=self.SearchDestination)
        self.Destination.bind(on_double_tap=self.ClearDestination)
        

        self.SearchButton = Button(text='->',
                                   pos=(630, 430),
                                   size_hint=(None, None),
                                   size=(40, 40),
                                   background_color=(0.0, 0.9, 0.0, 0.75))
        self.SearchButton.bind(on_press=self.SearchDestination)
        
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color= (0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication) 
        
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint= (None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press= self.BackToMenu)
        
        
        self.ZoomInButton = Button(text='+',
                                   pos=(10,50),
                                   size_hint=(None, None),
                                   size=(40, 40),
                                   background_color=(0, 0, 0.90, 1))
        self.ZoomInButton.bind(on_press= self.ZoomIn)
        
        
        self.ZoomOutButton = Button(text='-',
                                   pos=(10,10),
                                   size_hint=(None, None),
                                   size=(40, 40),
                                   background_color=(0, 0, 0.90, 1))
        self.ZoomOutButton.bind(on_press= self.ZoomOut)
        
        self.GetLocationButton = Button(text='(@)',
                                        pos=(50, 10),
                                        size_hint=(None, None),
                                        size=(40, 40),
                                        background_color=(0, 0, 0.90, 1))
        self.GetLocationButton.bind(on_press= self.ZoomToCurrentLocation)
        
        self.PlaceNewMarkerButton = Button(text='^',
                                           pos=(90,10),
                                           size_hint=(None, None),
                                           size=(40, 40),
                                           background_color=(0, 0, 0.90, 1))
        self.PlaceNewMarkerButton.bind(on_press= self.PlaceMarker)
        
        
        #POPUP ERRORS
        self.popup_location_error = Popup(title='Location Error',
                                          content=Label(text='-Invalid location- \n Please try again!'),
                                          size_hint=(None, None), size=(500, 100))
        
        self.popup_bluetooth_error = Popup(title='Bluetooth Error',
                                          content=Label(text='-Could not connect to ODBII Device- \n Please Reconnect and try again!'),
                                          size_hint=(None, None), size=(500, 100))
        
        self.popup_gps_error = Popup(title='GPS Error',
                                          content=Label(text='-Invalid location- \n Please try again!'),
                                          size_hint=(None, None), size=(500, 100))
        
        
        
        #LOCATION DATA
        self.MyCurrentLocation = (42.8982149, -78.8672276)
        self.PlaceNewMarker = False
        #Add location lock for synchronization 
        
        
        #MAP MARKERS LIST
        self.MapMarkers = []
        
        
        #Add Objects to the Screen
        self.add_widget(self.Background)
        self.add_widget(self.Map)
        self.add_widget(self.Destination)
        self.add_widget(self.SearchButton)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
        self.add_widget(self.ZoomInButton)
        self.add_widget(self.ZoomOutButton)
        self.add_widget(self.GetLocationButton)
        self.add_widget(self.PlaceNewMarkerButton)                           

    def BackToMenu(self, *args):
        sm.current = 'menu'
        
    def exitApplication(self, *args):
        App.get_running_app().stop() 
        
    def PlaceMarker(self, *args):
        x = self.Map.width/2
        y = self.Map.height/2
        newLoc = self.Map.get_latlon_at(x,y)
        CurMarker = MapMarker(lat=newLoc[0], lon=newLoc[1])
        self.MapMarkers.append(CurMarker)
        self.Map.add_marker(CurMarker)
        
    
    def SearchDestination(self, *args):
        location_text = self.Destination.text
        g = geocoder.google(location_text)
        if(g.status=='OK'):
            print(g.json)
            print(g.latlng)
            self.Map.center_on(g.latlng[0],g.latlng[1])
            self.Destination.text = ''
            self.Map.zoom = 16
            self.ClearAllMapMarkers()
            CurMarker = MapMarker(lat=g.latlng[0], lon=g.latlng[1])
            self.MapMarkers.append(CurMarker)
            self.Map.add_marker(CurMarker)
            #self.SetPlaceText(g)
        
        else:
            self.popup_location_error.open()
    
    def ClearDestination(self, *args):
        self.Destination.text = ''  
        
    def ClearAllMapMarkers(self, *args):
        for marker in self.MapMarkers:
            self.Map.remove_marker(marker)
        
    def ZoomOut(self, *args):
        if(self.Map.zoom>0):
            self.Map.zoom-=1
            print('Map Zoom Level: ' + str(self.Map.zoom))
        
    def ZoomIn(self, *args):
        if(self.Map.zoom<19):
            self.Map.zoom+=1
            print('Map Zoom Level: ' + str(self.Map.zoom))
            
    def ZoomToCurrentLocation(self, *args):
        newloc = self.MyCurrentLocation
        self.Map.center_on(newloc[0],newloc[1])
        self.ClearAllMapMarkers()
        self.Map.zoom = 16
        CurMarker = MapMarker(lat=newloc[0], lon=newloc[1])
        self.MapMarkers.append(CurMarker)
        self.Map.add_marker(CurMarker)
                
    def GetCurrentLocation(self, *args):
        #Define Mechanism to grab GPS coordinates from USB device
        lat = 42.8982149
        lon = -78.8672276
        #AQUIRE LOCK WHEN IMPLEMENTED
        self.MyCurrentLocation = (lat, lon)
        #RELEASE LOCK
        #ERASE LAST MARKER
        #ADD NEW MARKER
        print(self.MyCurrentLocation)
                
class WeatherScreen(Screen):
    
    def __init__(self, **kwargs):
        super(WeatherScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.WeatherImage = Image(source='Images/Weather_Example.png',
                                  pos=(10, 70),
                                  size_hint=(None, None),
                                  size=(780, 345))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)
        
        self.Location = TextInput(text='Location',
                                  multiline=False,
                                  pos=(130, 430),
                                  size_hint=(None, None),
                                  size=(500,40))
        self.Location.bind(on_double_tap=self.ClearLocation)
        self.Location.bind(on_text_validate=self.SearchLocation)
        
        self.SearchButton = Button(text='->',
                                   pos=(630, 430),
                                   size_hint=(None, None),
                                   size=(40, 40),
                                   background_color=(0.0, 0.9, 0.0, 0.75))
        self.SearchButton.bind(on_press=self.SearchLocation)
        
        self.LocationText = Label(text='[b][size=32][color=000000] Buffalo, NY [/color][/size][/b]',
                                  markup=True,
                                  pos=(0, -200))
        
        self.DateRangeText = Label(text='[b][size=12][color=000000] [ May 12 2017 - May 21 2017 ] [/color][/size][/b]',
                                   markup=True,
                                   pos=(0, -225))
        
        
        #MY API KEY
        #Must replace in git repo
        self.control = pyowm.OWM('a2a355015a6ec9a5abf8f6ccb11fbb50')
        
        
        # ADD ALL COMPONENTS TO SCREEN
        self.add_widget(self.Background)
        self.add_widget(self.WeatherImage)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
        self.add_widget(self.Location)
        self.add_widget(self.SearchButton)
        self.add_widget(self.LocationText)
        self.add_widget(self.DateRangeText)
    
    def exitApplication(self, *args):
        App.get_running_app().stop() 
               
    def ClearLocation(self, *args):
        self.Location.text=''
        
    def SearchLocation(self, *args):
        print(self.control.daily_forecast(self.Location.text))
    
    def SetDefaultLocation(self, *args):
        pass
        
    def BackToMenu(self, *args):
        sm.current = 'menu'
                   
    def Search(self):
        print(self.location.text)
               
class CameraScreen(Screen):
    
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.CameraImage = AsyncImage(source='http://www.thruway.ny.gov/webcams/captures/img4ni00144n.jpg?%s.jpg' % uuid4().hex,
                                  pos=(10, 10),
                                  allow_stretch=True,
                                  nocache=True,
                                  size_hint=(None, None),
                                  size=(780, 415))
        
        self.CaptureImageButton = Button(text='Capture Image',
                                    pos=(130, 430),
                                    size_hint=(None, None),
                                    size=(110, 40),
                                    background_color=(0.1, 0.1, 0.1, 0.75))
        self.CaptureImageButton.bind(on_press=self.CaptureImage)
        
        self.CaptureVideoButton = Button(text='Capture Video',
                                    pos=(250, 430),
                                    size_hint=(None, None),
                                    size=(110, 40),
                                    background_color=(0.1, 0.1, 0.1, 0.75))
        self.CaptureVideoButton.bind(on_press=self.CaptureVideo)
        
        self.CaptureTimelapseButton = Button(text='Capture Timelapse',
                                    pos=(370, 430),
                                    size_hint=(None, None),
                                    size=(110, 40),
                                    background_color=(0.1, 0.1, 0.1, 0.75))
        self.CaptureTimelapseButton.bind(on_press=self.CaptureTimelapse)
        
        self.LiveButton = ToggleButton(text='IMAGE',
                                    pos=(490, 430),
                                    size_hint=(None, None),
                                    size=(110, 40),
                                    background_color=(0.1, 0.1, 0.1, 0.75))
        self.LiveButton.bind(on_press=self.StartCam)
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)
        
        
        #CAMERA CONTROL VARIABLES
        self.CameraStarted = False
        #self.UpdateThread = Thread(target=self.CamUpdate)
        self.CameraUpdateEvent = None
        
        # Add all Components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.CameraImage)
        self.add_widget(self.CaptureImageButton)
        self.add_widget(self.CaptureVideoButton)
        self.add_widget(self.CaptureTimelapseButton)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
        self.add_widget(self.LiveButton)
    
    def exitApplication(self, *args):
        App.get_running_app().stop() 
        
    def BackToMenu(self, *args):
        sm.current = 'menu'    
    
    def StartCam(self, *args):
        #source = 'https://i.ytimg.com/vi/rRlHBeg7KoU/maxresdefault.jpg'
        #print(source)
        self.CameraStarted = not self.CameraStarted
        
        """
        if(self.CameraStarted == True and not self.UpdateThread.isAlive()):
            self.UpdateThread.start()
        """
        
        if(self.CameraStarted == True):
            self.LiveButton.text='LIVE'
            self.CameraUpdateEvent = Clock.schedule_interval(self.CamUpdate,4)
            
        else:
            self.LiveButton.text='IMAGE'
            self.CameraUpdateEvent.cancel()
        
    def CaptureImage(self, *args):
        pass
    
    def CaptureVideo(self, *args):
        pass
        
    def CaptureTimelapse(self, *args):
        pass
        
    def CamUpdate(self, *args):
        if(self.CameraStarted):
            self.CameraImage.reload()
            #print('RELOADED')
            #time.sleep(4)
             
class EngineScreen(Screen):
    
    def __init__(self, **kwargs):
        super(EngineScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)

        # Add all components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
    
    def exitApplication(self, *args):
        App.get_running_app().stop() 
        
    def BackToMenu(self, *args):
        sm.current = 'menu'  

           
"""
    MENU 2: SCREEN CLASSES
"""           
class MessagingScreen(Screen):
    def __init__(self, **kwargs):
        super(MessagingScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)

        # Add all components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
       
    def exitApplication(self, *args):
        App.get_running_app().stop() 
       
    def BackToMenu(self, *args):
        sm.current = 'menu2'     

class CalendarScreen(Screen):

    def __init__(self, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty_Dark.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)
        
        
        self.NewEvent = Button(text='New Event',
                               pos=(240, 430),
                               size_hint=(None, None),
                               size=(100, 40),
                               background_color=(0.75, 0.75, 0.75, 1))
        
        
        self.DeleteEvent = Button(text='Delete Event',
                               pos=(350, 430),
                               size_hint=(None, None),
                               size=(100, 40),
                               background_color=(0.75, 0.75, 0.75, 1))
        
        
        self.SyncEvents = Button(text='Sync Calendar',
                               pos=(460, 430),
                               size_hint=(None, None),
                               size=(100, 40),
                               background_color=(0.75, 0.75, 0.75, 1))
        
        
        
        
        self.CalendarView = CalendarWidget(pos=(20, 20),
                                           size_hint=(None, None),
                                           size=(400,400))

        self.EventView = ScrollView(pos=(440, 20), 
                                    size_hint=(None, None), 
                                    size=(350, 350))
        
        self.CurrentDateLabel = Label(text='[size=16] Wednesday May 24th, 2017 [/size]',
                                      pos=(215,160),
                                      markup=True)
        
        
        self.Events = CalendarEvents()
        self.Events.bind(minimum_height=self.Events.setter('height'))
        self.EventView.add_widget(self.Events)
        
        
        # Add all components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
        self.add_widget(self.CalendarView)
        self.add_widget(self.EventView)
        self.add_widget(self.CurrentDateLabel)
        self.add_widget(self.NewEvent)
        self.add_widget(self.DeleteEvent)
        self.add_widget(self.SyncEvents)
        
        
        
       
    def exitApplication(self, *args):
        App.get_running_app().stop() 
    
    def BackToMenu(self, *args):
        sm.current = 'menu2'  

class CalendarEvents(GridLayout):
    
    def __init__(self, **kwargs):
        super(CalendarEvents, self).__init__(**kwargs)
        
        
        self.size_hint_y=None
        self.cols=2
        self.row_default_height = '30dp'
        self.row_force_default = True
        self.spacing = (0, 0)
        self.padding = (0, 0)
        
        
        self.TimeDic = {}
        

        cur_time = Button(text='DAY', size_hint_x=None, width=80)
        cur_event = Label(text='-')
        
        self.TimeDic['DAY']= cur_event
        
        self.add_widget(cur_time)
        self.add_widget(cur_event)
            
        for n in range(18):
            Time1 = str(6+n)+':00'
            Time2 = str(6+n)+':30'
            
            cur_time_1 = Button(text=Time1, size_hint_x=None, width=80)
            cur_event_1 = Label(text='-')
            cur_time_2 = Button(text=Time2, size_hint_x=None, width=80 )
            cur_event_2= Label(text='-')
        
            self.TimeDic[Time1] = cur_event_1
            self.TimeDic[Time2] = cur_event_2
        
            self.add_widget(cur_time_1)
            self.add_widget(cur_event_1)
            self.add_widget(cur_time_2)
            self.add_widget(cur_event_2)
                 
class SportsScreen(Screen):

    def __init__(self, **kwargs):
        super(SportsScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)

        # Add all components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
       
    def exitApplication(self, *args):
        App.get_running_app().stop() 
        
    def BackToMenu(self, *args):
        sm.current = 'menu2'  
               
class TasksScreen(Screen):
    
    def __init__(self, **kwargs):
        super(TasksScreen, self).__init__(**kwargs)
        
        self.Background = Image(source='Images/BG_Empty_Dark.png',
                                pos=(0, 0),
                                size_hint=(None, None),
                                size=(800, 480))
        
        self.ExitButton = Button(text='Exit',
                                 pos=(690, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.9, 0.0, 0.0, 0.75))
        self.ExitButton.bind(on_press=self.exitApplication)
        
        self.BackButton = Button(text='Back',
                                 pos=(10, 430),
                                 size_hint=(None, None),
                                 size=(100, 40),
                                 background_color=(0.18, 0.38, 0.70, 0.75))
        self.BackButton.bind(on_press=self.BackToMenu)
        
        
        self.newTaskText = TextInput(text='New Task',
                                     multiline=False,
                                     pos=(130, 430),
                                     size_hint=(None, None),
                                     size=(500, 40))
        self.newTaskText.bind(on_text_validate=self.addNewTask)
        self.newTaskText.bind(on_double_tap=self.clearTaskText)
        

        self.addButton = Button(text='+',
                                   pos=(630, 430),
                                   size_hint=(None, None),
                                   size=(40, 40),
                                   background_color=(0.0, 0.9, 0.0, 0.75))
        self.addButton.bind(on_press=self.addNewTask)
        
        
        
        self.TaskViewActive = ScrollView(pos=(20, 20), 
                                    size_hint=(None, None), 
                                    size=(350, 350))
        
        self.TaskViewComplete = ScrollView(pos=(420, 20), 
                                    size_hint=(None, None), 
                                    size=(350, 350))
        
        self.ActiveLabel = Label(text='[size=22] ACTIVE [/size]',
                                 markup=True,
                                 pos=(-200, 150))
        
        self.CompleteLabel = Label(text='[size=22] COMPLETE [/size]',
                                 markup=True,
                                 pos=(200, 150))
        
        self.TaskActive = ActiveTasks()
        self.TaskActive.bind(minimum_height=self.TaskActive.setter('height'))
        self.TaskViewActive.add_widget(self.TaskActive)
        
        self.TaskComplete = CompleteTasks()
        self.TaskComplete.bind(minimum_height=self.TaskComplete.setter('height'))
        self.TaskViewComplete.add_widget(self.TaskComplete)
        
        self.TaskActive.setCompleteTaskRef(self.TaskComplete)
        self.TaskComplete.setActiveTaskRef(self.TaskActive)
        
    

        # Add all components to Screen
        self.add_widget(self.Background)
        self.add_widget(self.ExitButton)
        self.add_widget(self.BackButton)
        self.add_widget(self.TaskViewActive)
        self.add_widget(self.TaskViewComplete)
        self.add_widget(self.ActiveLabel)
        self.add_widget(self.CompleteLabel)
        self.add_widget(self.newTaskText)
        self.add_widget(self.addButton)
       
    def exitApplication(self, *args):
        App.get_running_app().stop()    
    
    def BackToMenu(self, *args):
        sm.current = 'menu2'  
        
    def addNewTask(self, *args):
        if(self.newTaskText.text.strip() != ''):
            self.TaskActive.addTaskAndSave(self.newTaskText.text)
        self.newTaskText.text=''
        self.newTaskText.select_all()
           
    def clearTaskText(self, *args):
        self.newTaskText.text=''

class ActiveTasks(GridLayout):
    
    def __init__(self, **kwargs):
        super(ActiveTasks, self).__init__(**kwargs)
        
        self.size_hint_y=None
        self.cols=3
        self.row_default_height = '30dp'
        self.row_force_default = True
        self.spacing = (0, 0)
        self.padding = (0, 0)
        
        self.TaskDic = {}
        
        self.CompleteTaskRef = None
        
        self.loadActiveTasks()
    
    def loadActiveTasks(self):
        if(os.path.isfile("Pickles/ActiveTasks.p")):
            with open('Pickles/ActiveTasks.p', 'rb') as handle:
                task_list = pickle.load(handle)
            
                for stringvalue in task_list:
                    self.addTask(stringvalue)
    
    def saveActiveTasks(self):
        with open('Pickles/ActiveTasks.p', 'wb') as handle:
            pickle.dump(list(self.TaskDic.keys()), handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def setCompleteTaskRef(self, Complete):
        self.CompleteTaskRef = Complete
        
    def addTaskAndSave(self, tasktext):
        self.addTask(tasktext)
        self.saveActiveTasks()
        
    def addTask(self, tasktext):
        check = CheckBox(size_hint_x=None, width=30)
        check.bind(active=partial(self.completeTask, tasktext))
        
        task = TextInput(text=tasktext, multiline=True)
        #task.do_cursor_movement('cursor_home',control=True, alt=False)
        
        delete = Button(text='X', size_hint_x=None, width=30)
        delete.bind(on_press=partial(self.removeTask, tasktext))
        
        if(tasktext not in self.TaskDic):
            self.TaskDic[tasktext]=[check, task, delete]
        
            self.add_widget(check)
            self.add_widget(task)
            self.add_widget(delete)
    

    def removeTask(self, *args):
        #print('Trying to remove task: ' + args[0])
        widgets= self.TaskDic[args[0]]
        self.TaskDic.pop(args[0])
        self.remove_widget(widgets[0])
        self.remove_widget(widgets[1])
        self.remove_widget(widgets[2])
        
        self.saveActiveTasks()
                
    def completeTask(self, *args):
        #print('Trying to complete task: ' + args[0])
        widgets= self.TaskDic[args[0]]
        self.TaskDic.pop(args[0])
        self.CompleteTaskRef.addTaskAndSave(widgets[1].text)
        self.remove_widget(widgets[0])
        self.remove_widget(widgets[1])
        self.remove_widget(widgets[2])
        
        self.saveActiveTasks()
    
class CompleteTasks(GridLayout):
    
    def __init__(self, **kwargs):
        super(CompleteTasks, self).__init__(**kwargs)
        
        self.size_hint_y=None
        self.cols=3
        self.row_default_height = '30dp'
        self.row_force_default = True
        self.spacing = (0, 0)
        self.padding = (0, 0)
        
        self.TaskDic = {}
        
        self.ActiveTaskRef = None
        
        self.loadCompleteTasks()
        
    def loadCompleteTasks(self):
        if(os.path.isfile("Pickles/CompleteTasks.p")):
            with open('Pickles/CompleteTasks.p', 'rb') as handle:
                task_list = pickle.load(handle)
            
                for stringvalue in task_list:
                    self.addTask(stringvalue)
    
    def saveCompleteTasks(self):
        with open('Pickles/CompleteTasks.p', 'wb') as handle:
            pickle.dump(list(self.TaskDic.keys()), handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def setActiveTaskRef(self, Active):
        self.ActiveTaskRef = Active
    
    def addTaskAndSave(self, tasktext):
        self.addTask(tasktext)
        self.saveCompleteTasks()
        
    def addTask(self, tasktext):
        check = CheckBox(size_hint_x=None, width=30, active=True)
        check.bind(active=partial(self.reactivateTask, tasktext))
        
        task = TextInput(text=tasktext, multiline=True)
        #task.do_cursor_movement('cursor_home',control=True, alt=False)
        task.disabled=True
        
        delete = Button(text='X', size_hint_x=None, width=30)
        delete.bind(on_press=partial(self.removeTask, tasktext))
        
        self.TaskDic[tasktext]=[check, task, delete]
        
        self.add_widget(check)
        self.add_widget(task)
        self.add_widget(delete)

        
    def removeTask(self, *args):
        #print('Trying to remove task: ' + args[0])
        widgets= self.TaskDic[args[0]]
        self.TaskDic.pop(args[0])
        self.remove_widget(widgets[0])
        self.remove_widget(widgets[1])
        self.remove_widget(widgets[2])
        self.saveCompleteTasks()
        
    def reactivateTask(self, *args):
        widgets= self.TaskDic[args[0]]
        self.TaskDic.pop(args[0])
        self.ActiveTaskRef.addTaskAndSave(args[0])
        self.remove_widget(widgets[0])
        self.remove_widget(widgets[1])
        self.remove_widget(widgets[2])
        self.saveCompleteTasks()

"""
    MAIN APPLICATION
"""

class AutoApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    #configureGraphics()
    initScreenManager()
    AutoApp().run()
    