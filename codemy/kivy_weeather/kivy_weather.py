import http.client
import urllib.parse
import requests
from requests import get
import json

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

BASE_URL_WEATHER = "http://api.positionstack.com/v1/"
API_KEY_WEATHER = "1353ad9c7af9a94f3f41d52e1c656a22abdba01ba8094ab0cfe3609c7385cc92"

URL_LOCATION = "https://api.ambeedata.com/weather/latest/by-lat-lng"
API_KEY_LOCATION = "05fe4fc8294f68ce34f808282d69b31f"


Builder.load_file('kivy_weather.kv')

class MyLayout(Widget):
    def press(self):
        conn = http.client.HTTPConnection('api.positionstack.com')
        params = urllib.parse.urlencode({
            'access_key': f'{API_KEY_LOCATION}',
            'query': f'{self.ids.city_input.text}',
            'limit': 1,
            'output': 'json'
        })
        conn.request('GET', f'/v1/forward?{params}')   
        res = conn.getresponse().read()
        dec = res.decode()
        ajson = json.loads(dec)
        # print(((ajson["data"][0]["label"][0])))
        if len(ajson["data"]) > 0:
            lat = ajson['data'][0]['latitude']
            lng = ajson['data'][0]['longitude']
            country_name = ajson["data"][0]["label"]
            # print(lat,',',lng)

        querystring = {"lat": f"{lat}", "lng": f"{lng}"}
        headers = {
            'x-api-key': f'{API_KEY_WEATHER}',
            'Content-type': "application/json"
        }
        response = requests.request(
            "GET", URL_LOCATION, headers=headers, params=querystring).json()
        res = round(((response['data']['apparentTemperature'])-32)*5/9)
        summary = response['data']['summary']
        condition =  f'{res} celcius, {summary}'
        self.ids.result.text = f'Weather in {country_name}, {condition}'

class AwsomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwsomeApp().run()