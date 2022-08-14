from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Builder.load_file('box.kv')

class MyLayout(Widget):
    
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    
    def submite(self):
        name = self.name.text
        pizza = self.pizza.text
        print(f"hello {name}, eat some {pizza}")

    def clear(self):     
        self.name.text = ''
        self.pizza.text = ''

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()