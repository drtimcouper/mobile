import kivy
kivy.require('1.7.2')

import weakref

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window



HEIGHT=100
name_width, tel_width = 400,270#253,149


class RootWidget(ScrollView):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.build_grid()


    def get_names(self):
        names = []

        for i in range(40):
            if i ==2:
                name = 'a very long name so there'
            else:
                name = 'Name %d' % i
            tel = '01582 123 45%d' % i
            names.append((name,tel))

        return names

    def build_grid(self):

        grid = GridLayout(cols=3,size_hint_y=None,
                                        row_force_default=True, row_default_height=HEIGHT,
                                        )
        grid.bind(minimum_height=grid.setter('height'))
        for name, tel in self.get_names()[:4]:
            nbtn = NameButton(text=name, size_hint_x=None, width=name_width)
            grid.add_widget(nbtn)
            tbtn = TelButton(text=tel, size_hint_x=None, width=tel_width)
            grid.add_widget(tbtn)
            cb = CheckBox(size_hint_x=None, width=HEIGHT)  # so it's square
            grid.add_widget(cb)
            nbtn.cb = tbtn.cb = weakref.ref(cb)

        self.add_widget(grid)


class NameButton(Button):
    pressed = ListProperty([0, 0])


    def __init__(self, **kwargs):
        super(NameButton, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        super(NameButton, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        # Show the notes:
        popup=MyPopup(title='Notes: %s' % self.text, anchor_y='top',
                                    size_hint=(.8,.5))
        popup.build(self.text)
        popup.open()

STORAGE={}

class MyPopup(Popup):

    def build(self, name):
        self.name = name
        s=STORAGE.get(self.name, '')
        self.tx = TextInput(text=s)
        self.content = self.tx

    def on_dismiss(self):
        STORAGE[self.name] = self.tx.text
        Window.release_keyboard()
        super(MyPopup,self).on_dismiss()


class TelButton(Button):
    pressed = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super(TelButton, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        super(TelButton, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        # dial the number
        cb = self.cb()
        cb.active = not cb.active



class PTel(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    p = PTel(size_hint=(120, None))#, size=(100,200))
    p.run()
