from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('update_label.kv')

class MyLayout(Widget):
    def press(self):
        # Create variable for our widget
        name = self.ids.name_input.text
        # Update the Label
        self.ids.name_label.text = name
        # Clear input box
        self.ids.name_input.text = ''

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()