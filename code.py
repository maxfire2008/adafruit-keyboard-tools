import time
##from adafruit_circuitplayground.express import cpx
import board
import neopixel
import digitalio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

_discord_dank_memer_previous_times = {
    "beg": 0,
    "hunt": 0,
    "fish": 0,
    "dig": 0,
    "dep all": 0,
}

_discord_dank_memer_wait_times = {
    "beg": 46,
    "hunt": 41,
    "fish": 41,
    "dig": 41,
    "dep all": 300,
}

def discord_dank_memer():
##    global _discord_dank_memer_previous_times
##    global _discord_dank_memer_wait_times
##    layout.write('pls bal')
##    kbd.send(Keycode.ENTER)
    print("dmemer")

def test_print():
    print("app run")

apps = [
    {
        "app_func": discord_dank_memer,
        "app_colour": [255,0,0]
    },
    {
        "app_func": test_print,
        "app_colour": [0,0,255]
    }
]

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.UP
buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.UP

current_app = 0
running_app = False
while True:
    current_app %= len(apps)
    print(current_app)
    print(time.time())
    if running_app:
        apps[current_app]["app_func"]()
        current_led_running = int(time.time())
        current_led_running %= len(pixels)
        for i in range(len(pixels)):
            pixels[i] = [0,0,0]
            pixels[current_led_running] = apps[current_app]["app_colour"]
            pixels.show()
    else:
        for i in range(len(pixels)):
            pixels[i] = apps[current_app]["app_colour"]
            pixels.show()
        if buttonA.value and buttonB.value:
            print("start")
            running_app = True
        elif buttonA.value:
            current_app -= 1
        elif buttonB.value:
            current_app += 1
