import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class First_Botao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1)
        self.text_input = TextInput(text = 'Type Your Name: ')
        grid.add_widget(self.text_input)
        
        button1 = Button(text = 'Login')
        button1.bind(on_press = self.ChageName)
        grid.add_widget(button1)
        
        button2 = Button(text = 'Cancelar')
        grid.add_widget(button2)
        
        layout.add_widget(grid)
        
        return layout
    
    def ChageName(self, button):
        if self.text_input == 'Senhor':
            self.text_input.text = 'Jesus Cristo é o Senhor'
        
        else:
            self.text_input.text = 'Type Your Name: '
        
        
if __name__=="__main__":
    First_Botao().run()