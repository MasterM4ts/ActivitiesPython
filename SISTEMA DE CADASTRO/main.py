from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.responsivelayout import MDResponsiveLayout



class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = App()


class App(MDApp):
    def build(self):
        self.dialog = None
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        
        Itens = ['MENU', 'Cadastrar', 'Editar', 'Excluir', 'Sair']
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "height": dp(55),
                "on_release": lambda x = f"Item {i}": self.munu_callback(),
             } for i in Itens 
        ]
        self.menu = MDDropdownMenu(
            items = menu_items,
            width_mult = 4,
        )
        
        return Builder.load_file('KIVY.kv')

    def Menu(self, button):
        self.menu.caller = button
        self.menu.open()
        
    
    def Mudar_Tela(self, screen_name):
        self.root.ids.screen_manager.current = screen_name


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


    def close_dialog(self, obj):
        self.dialog.dismiss()
    

if __name__ == '__main__':
    App().run()