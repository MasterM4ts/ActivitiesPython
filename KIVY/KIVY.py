import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class HelloWorld(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        tamanho = '80'
        self.label = Label(text = "Hello World !!", font_size = tamanho)
        button  = Button(text='Button', size_hint=(1,0.5))
        button.bind(on_press = self.on_button)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout
    
    def on_button(self, instance):
        logo = Image(source='Fundo.jpg') 
        return logo

if __name__ == '__main__':
    HelloWorld().run()