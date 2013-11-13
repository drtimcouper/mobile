import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import  Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput


class RootWidget(Screen):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.build_box()

    def build_box(self):
        grid = BoxLayout(orientation='vertical')

        for i in range(3):
            t = 'Label %d' % i
            t = t*(i+1)
            label = Button(text=t,
                                  color=[0,1,0,1],
                                  background_color=[1,0,0,1]
                                  )

            label.text_size=(700,None)


            grid.add_widget(label)

        self.add_widget(grid)


    def build_grid(self):
        grid = GridLayout(cols=2, row_default_height=100,
                                     col_default_width=10,
                                    )



        for i in range(3):
            t = 'Label %d' % i
            t = t*(i+1)
            label = Button(text=t,
                                  color=[0,1,0,1],
                                  background_color=[1,0,0,1]


                                  )
            print label.size
            label.text_size=(350,None)


            grid.add_widget(label)
            grid.add_widget(Button(background_color=[1,0,0,1]))

        self.add_widget(grid)


class MyGrid(App):
    def build(self):
        root = RootWidget()
        return root


if __name__ == '__main__':
    MyGrid().run()
