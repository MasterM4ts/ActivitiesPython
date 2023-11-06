import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


class First_Image(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1)
        
        
        layout_IMG = BoxLayout(orientation = 'horizontal')
        self.image1 = Image(source = 'Gato.jpeg', opacity = 0)
        self.image2 = Image(source = 'Cachorro.jfif', opacity = 0)
        
        layout_IMG.add_widget(self.image1)
        layout_IMG.add_widget(self.image2)
        grid.add_widget(layout_IMG)
        
        
        layout_button = BoxLayout(orientation = 'horizontal')
        self.button1 = Button(text = 'Gato')
        self.button2 = Button(text = 'Cachorro')
        self.button1.bind(on_press = self.Image_UM)
        self.button2.bind(on_press = self.Image_DOIS)
        
        layout_button.add_widget(self.button1)
        layout_button.add_widget(self.button2)
        grid.add_widget(layout_button)
        
        
        layout.add_widget(grid)
        
        return layout
    
    
    def Image_UM(self, button):
        self.image1.opacity = 100
        self.image2.opacity = 0
    
    
    def Image_DOIS(self, button):
        self.image1.opacity = 0
        self.image2.opacity = 100  
       
 
if __name__ == '__main__':
    First_Image().run()       