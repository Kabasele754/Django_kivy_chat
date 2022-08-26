import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import requests
from kivy.clock import Clock
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp


#recycle view for home screen
class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        store = requests.get('http://127.0.0.1:8000/').json()

        list_data = []
        for item in store:
            list_data.append({'text': item['name']})

        self.data = list_data


class AddMessage(Widget):
    text_input = ObjectProperty(None)
    input = StringProperty('')

    def submit_input(self):
        self.input = self.text_input.text
        post = requests.post('http://127.0.0.1:8000/create', json={'name': self.input})

        self.input = ''


class HomeScreen(Screen):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file("main.kv")


Test().run()
