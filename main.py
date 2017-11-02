# -*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
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

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
#:import Toolbar kivymd.toolbar.Toolbar

#:import MapSource mapview.MapSource

NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "MobileInsight"
        NavigationDrawerIconButton:
            icon: 'radio-tower'
            text: "Radio"
            on_release: app.root.ids.scr_mngr.current = 'radio'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'database'
            text: "Data-plane Statistics"
            on_release: app.root.ids.scr_mngr.current = 'dataplane'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'lan-connect'
            text: "Connectivity Information"
            on_release: app.root.ids.scr_mngr.current = 'connectivity'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'phone'
            text: "Mobility Information"
            on_release: app.root.ids.scr_mngr.current = 'mobility'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'voice'
            text: "Data/Voice Service"
            on_release: app.root.ids.scr_mngr.current = 'datavoice'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Cards"
            on_release: app.root.ids.scr_mngr.current = 'card'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Labels"
            on_release: app.root.ids.scr_mngr.current = 'labels'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Lists"
            on_release: app.root.ids.scr_mngr.current = 'list'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Navigation Drawer Widgets"
            on_release: app.root.ids.scr_mngr.current = 'nav_drawer'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Progress bars"
            on_release: app.root.ids.scr_mngr.current = 'progressbars'; app.root.ids.toolbar.title = self.text
        NavigationDrawerIconButton:
            icon: 'settings'
            text: "Change Themes"
            on_release: app.root.ids.scr_mngr.current = 'theming'; app.root.ids.toolbar.title = self.text
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            id: toolbar
            title: 'Radio'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items: [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
        ScreenManager:
            id: scr_mngr
            Screen:
                name: 'radio'
                MDTabbedPanel:
                    id: tab_panel
                    tab_display_mode:'text'
                    MDTab:
                        name: 'data'
                        text: 'Data'
                        ScrollView:
                            do_scroll_x: False
                            BoxLayout:
                                orientation:'vertical'
                                size_hint_y: None
                                height: dp(408)
                                MDLabel:
                                    text: 'Link Capacity: 23'
                                    theme_text_color: 'Primary'
                                    font_style:"Body2"
                                    size_hint_y: None
                                    halign: 'center'
                                MDSeparator:
                                    height: dp(1)
                                MDLabel:
                                    text: 'Signal Strength'
                                    theme_text_color: 'Primary'
                                    font_style:"Body2"
                                    size_hint_y: None
                                    halign: 'center'
                                BoxLayout:
                                    size_hint_y: None
                                    MDLabel:
                                        text: 'RSSI'
                                        theme_text_color: 'Primary'
                                        font_style:"Caption"
                                        size_hint_y: None
                                        halign: 'center'
                                        height: self.texture_size[1] + dp(64)
                                    MDLabel:
                                        text: 'RSRP'
                                        theme_text_color: 'Primary'
                                        font_style:"Caption"
                                        size_hint_y: None
                                        halign: 'center'
                                        height: self.texture_size[1] + dp(64)
                                    MDLabel:
                                        text: 'RSRQ'
                                        theme_text_color: 'Primary'
                                        font_style:"Caption"
                                        size_hint_y: None
                                        halign: 'center'
                                        height: self.texture_size[1] + dp(64)
                                BoxLayout:
                                    size_hint_y: None
                                    MDLabel:
                                        text: 'RSCP'
                                        theme_text_color: 'Primary'
                                        font_style:"Caption"
                                        size_hint_y: None
                                        halign: 'center'
                                        height: self.texture_size[1] + dp(64)
                                    MDLabel:
                                        text: 'EcNOc'
                                        theme_text_color: 'Primary'
                                        font_style:"Caption"
                                        size_hint_y: None
                                        halign: 'center'
                                        height: self.texture_size[1] + dp(64)
                                MDSeparator:
                                    height: dp(1)
                                MDLabel:
                                    text: 'Power Meas'
                                    theme_text_color: 'Primary'
                                    font_style:"Body2"
                                    size_hint_y: None
                                    halign: 'center'
                                MDSeparator:
                                    height: dp(1)
                                MDLabel:
                                    text: 'Modulation Coding Scheme'
                                    theme_text_color: 'Primary'
                                    font_style:"Body2"
                                    size_hint_y: None
                                    halign: 'center'
                                MDSeparator:
                                    height: dp(1)
                                MDLabel:
                                    text: 'Channel Quality'
                                    theme_text_color: 'Primary'
                                    font_style:"Body2"
                                    size_hint_y: None
                                    halign: 'center'
                                MDSeparator:
                                    height: dp(1)
                                MDLabel:
                                    text: 'Radio Configurations'
                                    theme_text_color: 'Primary'
                                    font_style:"Body2"
                                    size_hint_y: None
                                    halign: 'center'
                                MDSeparator:
                                    height: dp(1)
                    MDTab:
                        name: 'map'
                        text: 'Map'

                        MapView:
                            id: mapview
                            lat: 50.6394
                            lon: 3.057
                            zoom: 8
                            #size_hint: .5, .5
                            #pos_hint: {"x": .25, "y": .25}

                            #on_map_relocated: mapview2.sync_to(self)
                            #on_map_relocated: mapview3.sync_to(self)

                            MapMarker:
                                lat: 50.6394
                                lon: 3.057

                            MapMarker
                                lat: -33.867
                                lon: 151.206

                        Toolbar:
                            id: maptoolbar
                            md_bg_color: app.theme_cls.primary_color
                            background_palette: 'Primary'
                            background_hue: '500'
                            title: 'None'

                            MDLabel:
                                text: "Longitude: {}".format(mapview.lon)
                                theme_text_color: 'Primary'
                                font_style:"Body2"
                                height: self.texture_size[1] + dp(40)
                            MDLabel:
                                text: "Latitude: {}".format(mapview.lat)
                                theme_text_color: 'Primary'
                                font_style:"Body2"
                                height: self.texture_size[1] + dp(40)
                                
            Screen:
                name: 'dataplane'
            Screen:
                name: 'connectivity'
            Screen:
                name: 'mobility'
            Screen:
                name: 'datavoice'
            Screen:
                name: 'card'
                MDCard:
                    size_hint: None, None
                    size:     dp(320), dp(180)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                MDCard:
                    size_hint: None, None
                    size: dp(320), dp(180)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'Title'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        MDLabel:
                            text: 'Body'
                            theme_text_color: 'Primary'
            Screen:
                name: 'labels'
                ScrollView:
                    do_scroll_x: False
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(1000)
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Primary'
                                text: "Body1 label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body2'
                                theme_text_color: 'Primary'
                                text: "Body2 label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body2'
                                theme_text_color: 'Primary'
                                text: "Body2 label"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Caption'
                                theme_text_color: 'Primary'
                                text: "Caption label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Subhead'
                                theme_text_color: 'Primary'
                                text: "Subhead label"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Title'
                                theme_text_color: 'Primary'
                                text: "Title label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Headline'
                                theme_text_color: 'Primary'
                                text: "Headline label"
                                halign: 'center'
                        MDLabel:
                            font_style: 'Display1'
                            theme_text_color: 'Primary'
                            text: "Display1 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display2'
                            theme_text_color: 'Primary'
                            text: "Display2 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display3'
                            theme_text_color: 'Primary'
                            text: "Display3 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display4'
                            theme_text_color: 'Primary'
                            text: "Display4 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Primary'
                                text: "Primary color"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Secondary'
                                text: "Secondary color"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Hint'
                                text: "Hint color"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Error'
                                text: "Error color"
                                halign: 'center'
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Custom'
                            text_color: (0,1,0,.4)
                            text: "Custom"
                            halign: 'center'

            Screen:
                name: 'list'
                ScrollView:
                    do_scroll_x: False
                    MDList:
                        id: ml
                        OneLineListItem:
                            text: "One-line item"
                        TwoLineListItem:
                            text: "Two-line item"
                            secondary_text: "Secondary text here"
                        ThreeLineListItem:
                            text: "Three-line item"
                            secondary_text: "This is a multi-line label where you can fit more text than usual"
                        OneLineAvatarListItem:
                            text: "Single-line item with avatar"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        TwoLineAvatarListItem:
                            type: "two-line"
                            text: "Two-line item..."
                            secondary_text: "with avatar"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        ThreeLineAvatarListItem:
                            type: "three-line"
                            text: "Three-line item..."
                            secondary_text: "...with avatar..." + '\\n' + "and third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        OneLineIconListItem:
                            text: "Single-line item with left icon"
                            IconLeftSampleWidget:
                                id: li_icon_1
                                icon: 'star-circle'
                        TwoLineIconListItem:
                            text: "Two-line item..."
                            secondary_text: "...with left icon"
                            IconLeftSampleWidget:
                                id: li_icon_2
                                icon: 'comment-text'
                        ThreeLineIconListItem:
                            text: "Three-line item..."
                            secondary_text: "...with left icon..." + '\\n' + "and third line!"
                            IconLeftSampleWidget:
                                id: li_icon_3
                                icon: 'sd'
                        OneLineAvatarIconListItem:
                            text: "Single-line + avatar&icon"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
                        TwoLineAvatarIconListItem:
                            text: "Two-line item..."
                            secondary_text: "...with avatar&icon"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
                        ThreeLineAvatarIconListItem:
                            text: "Three-line item..."
                            secondary_text: "...with avatar&icon..." + '\\n' + "and third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
            Screen:
                name: 'progressbars'
                BoxLayout:
                    orientation:'vertical'
                    padding: '8dp'

                    MDSlider:
                        id:progress_slider
                        min:0
                        max:100
                        value: 40

                    MDProgressBar:
                        value: progress_slider.value
                    MDProgressBar:
                        reversed: True
                        value: progress_slider.value

                    BoxLayout:
                        MDProgressBar:
                            orientation:"vertical"
                            reversed: True
                            value: progress_slider.value

                        MDProgressBar:
                            orientation:"vertical"
                            value: progress_slider.value
            Screen:
                name: 'textfields'
                ScrollView:
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(48)
                        spacing: 10
                        MDTextField:
                            hint_text: "No helper text"
                        MDTextField:
                            hint_text: "Helper text on focus"
                            helper_text: "This will disappear when you click off"
                            helper_text_mode: "on_focus"
                        MDTextField:
                            hint_text: "Persistent helper text"
                            helper_text: "Text is always here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            id: text_field_error
                            hint_text: "Helper text on error (Hit Enter with two characters here)"
                            helper_text: "Two is my least favorite number"
                            helper_text_mode: "on_error"
                        MDTextField:
                            hint_text: "Max text length = 10"
                            max_text_length: 10
                        MDTextField:
                            hint_text: "required = True"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            multiline: True
                            hint_text: "Multi-line text"
                            helper_text: "Messages are also supported here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            hint_text: "color_mode = \'accent\'"
                            color_mode: 'accent'
                        MDTextField:
                            hint_text: "color_mode = \'custom\'"
                            color_mode: 'custom'
                            helper_text_mode: "on_focus"
                            helper_text: "Color is defined by \'line_color_focus\' property"
                            line_color_focus: self.theme_cls.opposite_bg_normal  # This is the color used by the textfield
                        MDTextField:
                            hint_text: "disabled = True"
                            disabled: True

            Screen:
                name: 'theming'
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(80)
                    center_y: self.parent.center_y
                    MDRaisedButton:
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        center_x: self.parent.center_x
                        text: 'Change theme'
                        on_release: MDThemePicker().open()
                        opposite_colors: True
                        pos_hint: {'center_x': 0.5}
                    MDLabel:
                        text: "Current: " + app.theme_cls.theme_style + ", " + app.theme_cls.primary_palette
                        theme_text_color: 'Primary'
                        pos_hint: {'center_x': 0.5}
                        halign: 'center'
            Screen:
                name: 'nav_drawer'
                HackedDemoNavDrawer:
                    # NavigationDrawerToolbar:
                    #     title: "Navigation Drawer Widgets"
                    NavigationDrawerIconButton:
                        icon: 'checkbox-blank-circle'
                        text: "Badge text ---->"
                        badge_text: "99+"
                    NavigationDrawerIconButton:
                        active_color_type: 'accent'
                        text: "Accent active color"
                    NavigationDrawerIconButton:
                        active_color_type: 'custom'
                        text: "Custom active color"
                        active_color: [1, 0, 1, 1]
                    NavigationDrawerIconButton:
                        use_active: False
                        text: "Use active = False"
                    NavigationDrawerIconButton:
                        text: "Different icon"
                        icon: 'alarm'
                    NavigationDrawerDivider:
                    NavigationDrawerSubheader:
                        text: "NavigationDrawerSubheader"
                    NavigationDrawerIconButton:
                        text: "NavigationDrawerDivider \/"
                    NavigationDrawerDivider:

'''


class HackedDemoNavDrawer(MDNavigationDrawer):
    # DO NOT USE
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            # widget.bind(on_release=lambda x: self.panel.toggle_state())
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class KitchenSink(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "MobileInsight"

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        # self.theme_cls.theme_style = 'Dark'

        main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)
        return main_widget

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
    KitchenSink().run()
