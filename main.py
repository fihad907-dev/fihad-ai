from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FihadAIApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.add_widget(Label(text="=== FIHAD AI ASSISTANT ===", font_size=24, color=(1, 1, 0, 1)))
        self.add_widget(Label(text="Enter Your Name:", font_size=18))
        
        self.name_input = TextInput(multiline=False, font_size=18)
        self.add_widget(self.name_input)
        
        btn1 = Button(text="1. Mood Check", background_color=(0, 0.5, 1, 1), font_size=18)
        btn1.bind(on_press=self.mood_check)
        self.add_widget(btn1)
        
        btn2 = Button(text="2. Farm Check", background_color=(0, 0.7, 0.3, 1), font_size=18)
        btn2.bind(on_press=self.farm_check)
        self.add_widget(btn2)
        
        self.result_label = Label(text="AI is waiting for your input...", font_size=16)
        self.add_widget(self.result_label)
        
    def mood_check(self, instance):
        name = self.name_input.text if self.name_input.text else "Friend"
        self.result_label.text = f"AI: Hello {name}!\nNo matter how hard life gets,\nyou will go very far!"

    def farm_check(self, instance):
        name = self.name_input.text if self.name_input.text else "Friend"
        murgi = 50
        dam = 450
        mot = murgi * dam
        self.result_label.text = f"AI: Mr. {name},\nTotal price of 50 chickens is:\n{mot} Taka."

class MainApp(App):
    def build(self):
        return FihadAIApp()

if __name__ == '__main__':
    MainApp().run()
