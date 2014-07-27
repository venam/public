#!/usr/bin/python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
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
    accordion = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SwitchScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.create()

    def viewitem(self, object, value):
        print(value)
        

    def create(self):
        self.accordion.bind(selected=self.viewitem)


class AccordionThing(Accordion):
    selected = StringProperty("")

    def __init__(self, **kwargs):
        super(AccordionThing, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.draw()

    def switch(self, object, boolean):
        if not boolean:
            self.selected = object.title
#            print(self.selected)

    def draw(self):
        global file
        inst = file
        blades = []
        for cat in inst.listCategories():
            blades.append(AccordionItem(title='%s' % cat))
            blades[-1].bind(collapse=self.switch)
            box = BoxLayout(orientation = 'vertical')
            subs = inst.listInsideCategories(cat)
            for sub in subs:
                box.add_widget(Label(text="%s" % sub))
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
