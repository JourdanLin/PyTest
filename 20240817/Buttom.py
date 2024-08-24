
#http://stupidpythonideas.blogspot.com/2013/10/why-your-gui-app-freezes.html

from gpiozero import Button

button = Button(pin=18)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button no pressed")
