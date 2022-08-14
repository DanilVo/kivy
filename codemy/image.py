from curses import window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image

Builder.load_file('image.kv')

class MyLayout(Widget):
    pass

class AwsomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1) #BACKGROUND COLOR
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()