import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    # print("user push the buttom")
    led.toggle() # on to off or off to on
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)

    if led.is_lit:
        print("Led is on")
    else:
        print("led is off")

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25)
    #print(button)
    signal.pause()
    