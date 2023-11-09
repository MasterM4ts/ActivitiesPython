from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup



class MainMenu(Screen):
    def __init__(self, **kw):
        super(MainMenu, self).__init__(**kw)
        layout = BoxLayout(orientation = 'vertical')
        grid_buttons = GridLayout(cols = 2)
        
        self.text = Label(text = 'Bem Vindo Ao Sitema de Cadastros do Aeroporto',
                                font_size = 35, size_hint_y = None, height = 50)
        
        self.image = Image(source = 'IMG_Aeroporto.jpg', fit_mode = 'fill')
        
        self.cliente = Button(text = 'CLIENTE', font_size = 20, size_hint = (0.5, 1), 
                              border = (0, 5, 0, 5), background_color = (0, 1, 0, 1))
        
        self.passagem = Button(text = 'PASSAGEM', font_size = 20, size_hint = (0.5, 1), 
                               border = (0, 5, 0, 5), background_color = (0, 1, 0, 1))
        
        self.aviao = Button(text = 'AVIÃO', font_size = 20, size_hint = (0.5, 1), 
                            border = (0, 5, 0, 5), background_color = (0, 1, 0, 1))
        
        self.tripulacao = Button(text = 'TRIPULAÇÃO', font_size = 20, size_hint = (0.5, 1), 
                                 border = (0, 5, 0, 5), background_color = (0, 1, 0, 1))
        
        self.voo = Button(text = 'VOO', font_size = 20, size_hint = (0.5, 1), 
                          border = (0, 5, 0, 5), background_color = (0, 1, 0, 1))
        
        self.sair = Button(text = 'SAIR', font_size = 20, size_hint = (0.5, 1), 
                           border = (0, 5, 0, 5), background_color = (1, 1, 1, 1))

        self.cliente.bind(on_press = self.Cliente)
        self.passagem.bind(on_press = self.Passagem)
        self.aviao.bind(on_press = self.Aviao)
        self.tripulacao.bind(on_press = self.Tripulacao)
        self.voo.bind(on_press = self.Voo)
        self.sair.bind(on_press = App.get_running_app().stop)
        
        grid_buttons.add_widget(self.cliente)
        grid_buttons.add_widget(self.passagem)
        grid_buttons.add_widget(self.aviao)
        grid_buttons.add_widget(self.tripulacao)
        grid_buttons.add_widget(self.voo)
        grid_buttons.add_widget(self.sair)
        
        layout.add_widget(self.text)
        layout.add_widget(self.image)
        layout.add_widget(grid_buttons)
        
        self.add_widget(layout)
        
        
    def Cliente(self, *args):
        text = Button(text='Close me!', size_hint_y = None, height = 50)
        content = Button(text='Close me!', size_hint_y = None, height = 50)
        popup = Popup(content=content, auto_dismiss = False)
        content.bind(on_press=popup.dismiss)
        popup.open()
        self.manager.current = 'Cliente'
        
    
    def Passagem(self, *args):
        self.manager.current = 'Passagem'
        
    
    def Aviao(self, *args):
        self.manager.current = 'Avião'  
        
    
    def Tripulacao(self, *args):
        self.manager.current = 'Tripulação'
        
        
    def Voo(self, *args):
        self.manager.current = 'Voo'


#/////////////////////////////////////////////////////////////////////////////////#

class Cliente(Screen):
    def __init__(self, **kw):
        super(Cliente, self).__init__(**kw)
        layout = BoxLayout(orientation = 'vertical')
        
        
        
    
#/////////////////////////////////////////////////////////////////////////////////#
class Passagem(Screen):
    def __init__(self, **kw):
        super(Passagem, self).__init__(**kw)
        pass
    
#/////////////////////////////////////////////////////////////////////////////////#
class Aviao(Screen):
    def __init__(self, **kw):
        super(Aviao, self).__init__(**kw)
        pass

#/////////////////////////////////////////////////////////////////////////////////#
class Tripulacao(Screen):
    def __init__(self, **kw):
        super(Tripulacao, self).__init__(**kw)
        pass

#/////////////////////////////////////////////////////////////////////////////////#
class Voo(Screen):
    def __init__(self, **kw):
        super(Voo, self).__init__(**kw)
        pass