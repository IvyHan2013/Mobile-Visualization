from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.lang import Builder

Builder.load_string('''
<HomeScreen>:
    ScrollView:
        do_scroll_x: False
        do_scroll_y: False
''')

class HomeScreen(Screen):
    fullscreen = BooleanProperty(False)

    # def add_widget(self, *args):
    #     if 'content' in self.ids:
    #         return self.ids.content.add_widget(*args)
    #     return super(ShowcaseScreen, self).add_widget(*args)

from radio import RadioScreen
from connectivity import ConnectivityScreen
from dataplane import DataplaneScreen
from datavoice import DatavoiceScreen
from mobility import MobilityScreen
from theming import ThemingScreen

__all__ = ['RadioScreen', 'ConnectivityScreen', 'DataplaneScreen', 'DatavoiceScreen',\
            'MobilityScreen', 'ThemingScreen']
