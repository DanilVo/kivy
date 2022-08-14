from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call GridLayOut constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # First gridlayout 
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=100
        # Second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100)
        self.top_grid.cols = 2
        # Add input box
        self.top_grid.add_widget(Label(text='name'))
        self.name = TextInput(multiline = False)
        self.top_grid.add_widget(self.name)
        # Add input box
        self.top_grid.add_widget(Label(text='pizza'))
        self.pizza = TextInput(multiline = False)
        self.top_grid.add_widget(self.pizza)
        # Add input box
        self.top_grid.add_widget(Label(text='color'))
        self.color = TextInput(multiline = False)
        self.top_grid.add_widget(self.color)
        #Add new top_grid to app
        self.add_widget(self.top_grid)

        #Create a submit button
        self.submit = Button(text= 'submit',
            font_size=32,
            size_hint_y=None,
            height=50,
            size_hint_x=None,
            width=200)
        #Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # Prints it to screen
        self.add_widget(Label(text=f'hello {name}m your favorite pizza is {pizza}, your favorite color is {color}'))

        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''
    

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()