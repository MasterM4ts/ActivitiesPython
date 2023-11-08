from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

from random import randint


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        layout_button = BoxLayout(orientation = 'horizontal')
        
        self.image = Image(source = 'Image_Adivinha.jpeg', size_hint = (1, 6))
        self.iniciar = Button(text =' Jogar', font_size = 20, size_hint = (0.5, 1))
        self.iniciar.bind(on_press = self.Iniciar_Jogo)
        self.sair = Button(text = 'Sair', font_size = 20, size_hint = (0.5, 1))
        self.sair.bind(on_press = App.get_running_app().stop)
        
        layout_button.add_widget(self.iniciar)
        layout_button.add_widget(self.sair)
        
        layout.add_widget(self.image)
        layout.add_widget(layout_button)
        
        self.add_widget(layout)


    def Iniciar_Jogo(self, *args):
        self.manager.current = 'Jogo'


class AdivinheNumero(Screen):
    def __init__(self, **kwargs):
        super(AdivinheNumero, self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        layout_button = BoxLayout(orientation = 'horizontal')
        
        self.label_resultado = Label(text = 'Digite um número entre 1 e 100',
                                  font_size = 20, size_hint_y = None, height = 50)
        self.input_text = TextInput(multiline = False, font_size = 20)
        self.enviar = Button(text = 'Adivinhar', font_size = 20)
        self.enviar.bind(on_press = self.Checar_NumAdivinha)
        self.resetar = Button(text = 'Resetar Jogo', font_size = 20)
        self.resetar.bind(on_press = self.Resetar_NumAdivinha)
        
        self.voltar_menu = Button(text = 'Voltar para o Menu', font_size = 20)
        self.voltar_menu.bind(on_press = self.Voltar_Menu)  
        
        layout_button.add_widget(self.enviar)
        layout_button.add_widget(self.resetar)
        layout_button.add_widget(self.voltar_menu)
        
        layout.add_widget(self.label_resultado)
        layout.add_widget(self.input_text)
        layout.add_widget(layout_button)
         
        self.add_widget(layout)
        self.Resetar_NumAdivinha()  


    def Voltar_Menu(self, *args):  
        self.manager.current = 'Menu_Principal'
        
        
    def Resetar_NumAdivinha(self, *args):
        self.numero = randint(1, 100)
        self.label_resultado.text = 'Digite um número entre 1 e 100'
        self.input_text.text = ''


    def Checar_NumAdivinha(self, instance):
        try:
            num_adivinha = int(self.input_text.text)
            
            if num_adivinha == self.numero:
                self.label_resultado.text = 'Parabéns! Você acertou!'
                
            elif num_adivinha < self.numero:
                self.label_resultado.text = 'O número é maior que >%d<'%num_adivinha
                
            elif num_adivinha > self.numero:
                self.label_resultado.text = 'O número é menor que >%d<'%num_adivinha
                
        except ValueError:
            self.label_resultado.text = 'Por favor, insira um número válido.'