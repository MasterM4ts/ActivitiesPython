from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Telas import MainMenu, Cliente, Passagem, Tripulacao, Aviao, Voo


class AeroportoAPP(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenu(name='Menu_Principal'))
        screen_manager.add_widget(Cliente(name='Cliente'))
        screen_manager.add_widget(Passagem(name='Passagem'))
        screen_manager.add_widget(Tripulacao(name='Tripulação'))
        screen_manager.add_widget(Aviao(name='Avião'))
        screen_manager.add_widget(Voo(name='Voo'))
        return screen_manager


if __name__ == '__main__':
    AeroportoAPP().run()