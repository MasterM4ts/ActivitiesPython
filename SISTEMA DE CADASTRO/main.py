from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.responsivelayout import MDResponsiveLayout




class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = App()


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class App(MDApp):
    def build(self):
        self.dialog = None
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('KIVY.kv')
        

    def Sair(self):
        self.stop()


    def Mensagem_Concluido(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Cadastro concluído com sucesso!",
                buttons=[
                    MDRaisedButton(
                        text="Fechar", on_release=self.close_dialog
                    )
                ],
            )
        self.dialog.open()

    def Mudar_Tela(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def close_dialog(self, obj):
        self.dialog.dismiss()
    

if __name__ == '__main__':
    App().run()
    