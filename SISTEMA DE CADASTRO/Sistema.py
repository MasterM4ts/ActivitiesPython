from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
ScreenManager:
    Screen:
        name: 'screen1'

        MDTopAppBar:
            title: "Tela 1"

        MDIconButton:
            icon: 'android'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.change_screen('screen2')

    Screen:
        name: 'screen2'

        MDTopAppBar:
            title: "Tela 2"

        MDIconButton:
            icon: 'apple'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.change_screen('screen1')
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name

TestApp().run()

