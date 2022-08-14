from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')
# Builder.load_string("""
# whatever.kv
# # optional way to import code straight, not recomended
# """)

class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # Prints it to screen
        print(f'hello {name} your favorite pizza is {pizza}, your favorite color is {color}')

        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''
    

class AwsomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    AwsomeApp().run()