from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.clock import Clock
from datetime import datetime

class AlarmClock(Widget):
    def hourplus(self):
        x = int(self.hlabel.text)
        if x > 11:
            x = 1
            self.hlabel.text = str(x)
        else:
            x += 1
            self.hlabel.text = str(x)
    
    def hourminus(self):
        x = int(self.hlabel.text)
        if x < 2:
            x = 12
            self.hlabel.text = str(x)
        else:
            x -= 1
            self.hlabel.text = str(x)
        
    def minplus(self):
        x = int(self.mlabel.text)
        if x >= 59:
            x = "00"
            self.mlabel.text = str(x)
        else:
            x += 1
            if 0 <= x <= 9:
                self.mlabel.text = "0" + str(x)
            else:
                self.mlabel.text = str(x)

    def minminus(self):
        x = int(self.mlabel.text)
        if x <= 0:
            x = "59"
            self.mlabel.text = str(x)
        else:
            x -= 1
            if 0 <= x <= 9:
                self.mlabel.text = "0" + str(x)
            else:
                self.mlabel.text = str(x)

    def ampm(self):
        if self.apbutton.text == "AM":
            self.apbutton.text = "PM"
        elif self.apbutton.text == "PM":
            self.apbutton.text = "AM"

    def start(self):
        if self.apbutton.text == "PM":
            self.hlabel.text = str(int(self.hlabel.text) + 12)
        while True:


            if (int(self.hlabel.text) == int(datetime.now().strftime("%H")) and int(self.mlabel.text) == int(datetime.now().strftime("%M"))):
                print("good stuff")
                break

class AlarmApp(App):
    def build(self):
        alarm = AlarmClock()
        return alarm


if __name__ == '__main__':
    AlarmApp().run()