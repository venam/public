#!/usr/bin/python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty
from getpass import getuser
from socket import gethostname


class TitleBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TitleBar, self).__init__(**kwargs)
        self.orientation = 'vertical'


class Prompt(Label):

    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        self.text = getuser() + "@" + gethostname()


class SwitchScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(SwitchScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'


class AccordionThing(Accordion):

    def __init__(self, **kwargs):
        super(AccordionThing, self).__init__(**kwargs)
        self.orientation = 'vertical'
        for x in range(5):
            item = AccordionItem(title='title %d' % x)
            item.add_widget(Label(text="Very Big Content\n" * 10))
            self.add_widget(item)

class ButtonBar(BoxLayout):

    def __init__(self, **kwargs):
        super(ButtonBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'


class Splitter(Widget):
    pass


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        titleb = TitleBar()
        switch = SwitchScreen()
        splitr = Splitter()
        self.add_widget(titleb)
        self.add_widget(splitr)
        self.add_widget(switch)


class RiceApp(App):

    def build(self):
        win = MainScreen()
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return win


if __name__ == '__main__':
  RiceApp().run()
