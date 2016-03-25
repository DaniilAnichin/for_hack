#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

to_output = "staff"

def blink():
    global to_output
    to_output += '1'
    return to_output


class FinfthApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(text='default',
                      font_size=150,
                      size_hint_y=None,
                      height=200)

        f = FloatLayout()
        s = Scatter()
        global to_output
        l = Label(text=to_output,
                  font_size=150)

        t.bind(text=l.setter('text'))
        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(f)
        b.add_widget(t)
        return b


if __name__ == "__main__":
    FinfthApp().run()
