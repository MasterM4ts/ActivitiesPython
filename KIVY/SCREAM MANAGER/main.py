from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class APP(App):
    def build(self):
        SM = ScreenManager()
        
        
        return SM
    
if __name__=='__main__':
    APP().run()