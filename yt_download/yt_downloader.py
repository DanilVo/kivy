from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import requests
import json

Builder.load_file('yt_downloader.kv')

class MyLayout(Widget):
    def download(self):
        url_dw = self.ids.link.text



        url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

        querystring = {"id":"UxxajLWwzqY","geo":"DE"}

        headers = {
        	"X-RapidAPI-Key": "45f67ff11dmshb9159dcbe37c0ecp1b0068jsna0e855c575e8",
        	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(json.loads(response.text).keys())


class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()