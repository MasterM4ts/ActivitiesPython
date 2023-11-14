from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Game import MainMenu, AdivinheNumero


class AdivinheAPP(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenu(name='Menu_Principal'))
        screen_manager.add_widget(AdivinheNumero(name='Jogo'))
        return screen_manager


if __name__ == '__main__':
    AdivinheAPP().run()