








from re import MULTILINE
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        
        self.inside.add_widget(Label(text="first name: "))
        self.name = TextInput(multiline= False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="last name: "))
        self.last_name = TextInput(multiline= False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline= False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press= self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.last_name.text
        email = self.email.text

        self.name.text = ""
        self.last_name.text = ""
        self.email.text = ""

        print("name: ", name, " last: ", last, " email: ", email)

class myApp(App): # create my app
    # automatic call for father construcor
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    #creates the app and runs it 
    myApp().run() 