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
        
        self.image = Image(source = 'Image_Adivinha.jpeg', size_hint = (1, 0.5))
        self.iniciar = Button(text =' Jogar', font_size = 20)
        self.iniciar.bind(on_press = self.Iniciar_Jogo)
        self.sair = Button(text = 'Sair', font_size = 20)
        self.sair.bind(on_press = App.get_running_app().stop)
        
        layout.add_widget(self.image)
        layout.add_widget(self.iniciar)
        layout.add_widget(self.sair)
        
        self.add_widget(layout)

    def Iniciar_Jogo(self, *args):
        self.manager.current = 'Jogo'


class AdivinheNumero(Screen):
    def __init__(self, **kwargs):
        super(AdivinheNumero, self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        
        self.label_resultado = Label(text = 'Digite um número entre 1 e 100',
                                  font_size = 20, size_hint_y = None, height = 50)
        self.input_text = TextInput(multiline = False, font_size = 20)
        self.enviar = Button(text = 'Adivinhar', font_size = 20)
        self.enviar.bind(on_press = self.check_guess)
        self.resetar = Button(text = 'Resetar Jogo', font_size = 20)
        self.resetar.bind(on_press = self.reset_game)
        
        self.voltar_menu = Button(text = 'Voltar para o Menu', font_size = 20)
        self.voltar_menu.bind(on_press = self.switch_to_menu)  
        
        layout.add_widget(self.label_resultado)
        layout.add_widget(self.input_text)
        layout.add_widget(self.enviar)
        layout.add_widget(self.resetar)
        layout.add_widget(self.voltar_menu) 
         
        self.add_widget(layout)
        self.reset_game()  

    def switch_to_menu(self, *args):  
        self.manager.current = 'Menu_Principal'
        
    def reset_game(self, *args):
        self.number = randint(1, 100)
        self.label_resultado.text = 'Digite um número entre 1 e 100'
        self.input_text.text = ''

    def check_guess(self, instance):
        try:
            guess = int(self.input_text.text)
            if guess == self.number:
                self.label_resultado.text = 'Parabéns! Você acertou!'
            elif guess < self.number:
                self.label_resultado.text = 'O número é maior'
            elif guess > self.number:
                self.label_resultado.text = 'O número é menor'
        except ValueError:
            self.label_resultado.text = 'Por favor, insira um número válido.'