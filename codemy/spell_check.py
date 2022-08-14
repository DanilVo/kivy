from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.spelling import Spelling

Builder.load_file('spell_check.kv')

class MyLayout(Widget):
    def press(self):
        # create instance of spelling
        s = Spelling()
        #select a language
        # s.select_language('en')
        #see the language options s.list_languages()
        #grab word from textbox
        print(s.list_languages())
        # word = self.ids.word_input.text

        # option = s.suggest(word)
        # self.ids.word_label.text = str(option)

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()