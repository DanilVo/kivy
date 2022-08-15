from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import requests
import json
from urllib.parse import urlparse, parse_qs

Builder.load_file('yt_downloader.kv')

class MyLayout(Widget):

    def get_yt_video_id(url):
        global res
        # url = self.ids.link.text

        if url.startswith(('youtu', 'www')):
            url = 'http://' + url

        query = urlparse(url)

        if 'youtube' in query.hostname:
            if query.path == '/watch':
                res = parse_qs(query.query)['v'][0]
                return res
            elif query.path.startswith(('/embed/', '/v/')):
                res = query.path.split('/')[2]
                return res
        elif 'youtu.be' in query.hostname:
            res = query.path[1:]
            return res
        else:
            raise ValueError

    def download(self):

        MyLayout.get_yt_video_id(self.ids.link.text)
        
        url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

        querystring = {"id":f"{res}","geo":"DE"}

        headers = {
        	"X-RapidAPI-Key": "45f67ff11dmshb9159dcbe37c0ecp1b0068jsna0e855c575e8",
        	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_res = json.loads(response.text) 
        print(json.dumps(json_res,indent=1))
        
class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()