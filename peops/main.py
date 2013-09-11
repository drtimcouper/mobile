import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label

class Peops(App):
    def build(self):
        return Label(text='Peops!')

if __name__ == '__main__':
    Peops().run()
