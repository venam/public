#!/usr/bin/python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, ObjectProperty
from getpass import getuser
from socket import gethostname
import JsonInfoReader, State, Outputer
import time


file = JsonInfoReader.JsonInfoReader("info.json", None)

class TitleBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TitleBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'


class Prompt(Label):

    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        self.text = getuser() + "@" + gethostname()


class SwitchScreen(BoxLayout):
    global file
    inst = file
    accordion = ObjectProperty(None)
    scrollinfo = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SwitchScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.create()
#        self.scrollinfo.add_widget(InfoScreen(self.inst.listCategories()[0]))

    def viewitem(self, object, value):
        self.scrollinfo.clear_widgets()
        self.scrollinfo.add_widget(InfoScreen(value))

    def create(self):
        self.accordion.bind(selected=self.viewitem)


class InfoScreen(BoxLayout):

    def __init__(self, value, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        global file
        inst = file
#        self.padding = [0.9, 0.2]

        self.add_widget(Label(text = value, font_size = "28sp"))
#        for sub in inst.listInsideCategories(value):
#            l = (Label(text = sub)) #, halign="center", size_hint=(None, None)))
#            l.bind(texture_size=l.setter('size'))
#            self.add_widget(l)

        wid = Widget(size_hint_y = 0.9)
        inf = inst.getInfo(value)
        l2= (Label(text = inf, halign="center")) #, size_hint=(None, 0.05)))
#        l2.bind(texture_size=l.setter('size'))
        wid.add_widget(l2)
        self.add_widget(wid)


class AccordionThing(Accordion):
    selected = StringProperty("")

    def __init__(self, **kwargs):
        super(AccordionThing, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.draw()

    def switch(self, object):
        self.selected = object.text
#            print(self.selected)

    def draw(self):
        global file
        inst = file
        blades = []
        for cat in inst.listCategories():
            blades.append(AccordionItem(title = cat))
#            blades[-1].bind(collapse = self.switch)
            box = BoxLayout(orientation = 'vertical')
            subs = inst.listInsideCategories(cat)
            for sub in subs:
                butt = Button(text = sub, background_color = [0.35, 0.35, 0.35, 1])
                butt.bind(on_press = self.switch)
                box.add_widget(butt)
            blades[-1].add_widget(box)
            self.add_widget(blades[-1])
        blades[-1].collapse = True
        blades[0].collapse = False


class ButtonBar(BoxLayout):

    def __init__(self, **kwargs):
        super(ButtonBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        titleb = TitleBar()
        switch = SwitchScreen()
        self.add_widget(titleb)
        self.add_widget(switch)


class RiceApp(App):

    def build(self):
        win = MainScreen()
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return win


if __name__ == '__main__':
  RiceApp().run()
