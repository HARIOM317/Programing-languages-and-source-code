from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MinAPP(MDApp):
    def build(self):
        return MDLabel(text="My first android app", halign="center")

if __name__ == '__main__':
    MinAPP().run()
