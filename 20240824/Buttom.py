from gpiozero import Button

button = Button(pin=18)

    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")