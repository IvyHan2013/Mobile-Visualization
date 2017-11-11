# -*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty,NumericProperty,StringProperty,ListProperty
from kivy.uix.image import Image

from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
import screens

from kivy.clock import Clock
import random

class MobileInsightApp(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "MobileInsight"

    index = NumericProperty(1)
    current_title = StringProperty()
    screen_names = ListProperty([])
    rvalue1 = NumericProperty(40)
    rvalue2 = NumericProperty(40)
    rvalue3 = NumericProperty(40)

    def callback(self,dt):
        self.rvalue1 =round(random.random()*100,2)
        self.rvalue2 =round(random.random()*100,2)
        self.rvalue3 =round(random.random()*100,2)
           # print self.rvalue
    def on_rvalue1(self,instance,value):
        pass
    def on_rvalue2(self,instance,value):
        pass
    def on_rvalue3(self,instance,value):
        pass

    def build(self):
        
        Clock.schedule_interval(self.callback, 1)
        self.screens = {}
        self.available_screens = screens.__all__
        self.screen_names = self.available_screens
        for i in range(len(self.available_screens)):
            self.screens[i] = getattr(screens, self.available_screens[i])()
        self.root.ids.scr_mngr.switch_to(self.screens[0])
        #main_widget = Builder.load_string(main_widget_kv)
        #main_widget = Builder.load_string("mobileinsight.kv")
        # self.theme_cls.theme_style = 'Dark'

        # main_widget.ids.text_field_error.bind(
        #     on_text_validate=self.set_error_message,
        #     on_focus=self.set_error_message)
        # return main_widget
    def go_screen(self, idx):
        #print self.index
        self.index = idx
        self.root.ids.scr_mngr.switch_to(self.load_screen(idx), direction='left')
    
    def load_screen(self, index):
        return self.screens[index]
        # if index in self.screens:
        #     return self.screens[index]
        # print index
        # print self.available_screens[index]
        # screen = getattr(screens, self.available_screens[index])()
        # self.screens[index] = screen
        # return screen

    def get_time_picker_data(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        self.time_dialog = MDTimePicker()
        self.time_dialog.bind(time=self.get_time_picker_data)
        if self.root.ids.time_picker_use_previous_time.active:
            try:
                self.time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        self.time_dialog.open()

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.root.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        if self.root.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


if __name__ == '__main__':
    MobileInsightApp().run()
