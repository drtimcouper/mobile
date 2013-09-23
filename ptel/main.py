import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
#import pygame.font
HEIGHT=100

def pix_width(s):
    "return the representation of s in the current font and size"
    lbl = Label(text='')
    fo = pygame.font.SysFont(lbl.font_name, int(lbl.font_size))
    total = 0
    for metric in fo.metrics(s):
        total+=metric[1] + metric[4]
    #print '%s = %d' % (s,total)
    return total
cbs={}

class RootWidget(ScrollView):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        names = []
        #name_width = tel_width = 0
        for i in range(40):
            if i ==2:
                name = 'a very long name so there'
            else:
                name = 'Name %d' % i
            tel = '01582 123 45%d' % i
            names.append((name,tel))
        #     name_width = max(name_width, pix_width(name))
        #     tel_width = max(tel_width, pix_width(tel))
        # print name_width, tel_width
        name_width, tel_width = 400,270#253,149
        layout = GridLayout(cols=3,size_hint_y=None,
                                        row_force_default=True, row_default_height=HEIGHT,
                                        )
        layout.bind(minimum_height=layout.setter('height'))
        for name, tel in names:
            nbtn = NameButton(text=name, size_hint_x=None, width=name_width)
            layout.add_widget(nbtn)
            tbtn = TelButton(text=tel, size_hint_x=None, width=tel_width)
            layout.add_widget(tbtn)
            cb = CheckBox(size_hint_x=None, width=HEIGHT)  # so it's square
            layout.add_widget(cb)
            nbtn.cb = cb
        self.add_widget(layout)

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
        self.cb.active = not self.cb.active

class TelButton(Button):
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
        pass



class PTel(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    p = PTel(size_hint=(120, None))#, size=(100,200))
    p.run()
