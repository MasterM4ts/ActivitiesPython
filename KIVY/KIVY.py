import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class HelloWorld(App):
    def build(self):
        self.layout = BoxLayout(orientation = 'vertical')
        self.tamanho = '100'
        self.label = Label(text = "Hello World !!", font_size = self.tamanho)
        self.button  = Button(text='Button', size_hint=(1,0.5))
        self.button.bind(on_press = self.on_button)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout
    
    def on_button(self, instance):
        self.label_IMG = Image(source='Fundo.jpg', size_hint = (1, 0.5))
        return self.layout.add_widget(self.label_IMG) 
       

if __name__ == '__main__':
    HelloWorld().run()