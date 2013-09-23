import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class PeopScreen(GridLayout):
    def __init__(self, **kwargs):
        super(PeopScreen, self).__init__(**kwargs)
        for i in xrange(10):
            self.add_widget(Label(text='Hello%d' % i))
            self.add_widget(Label(text='World%d' % i))


class Peops(App):
    def build(self):
        return PeopScreen(cols=2, default_row_height=40)

    def on_touch_move(self, touch):
        print(touch.profile)
        return super(Peops, self).on_touch_move(touch)

    def on_touch_down(self, touch):
        print(touch.profile)
        return super(Peops, self).on_touch_move(touch)

if __name__ == '__main__':
    Peops().run()
