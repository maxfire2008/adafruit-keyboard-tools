import time
##from adafruit_circuitplayground.express import cpx
import board
import neopixel
import digitalio
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

STACKABLES_WAIT = 601

_discord_dank_memer_wait_times = {
    "pls beg": 46,
    "pls hunt": 41,
    "pls fish": 41,
    "pls dig": 41,
    "pls dep all": STACKABLES_WAIT,
    "pls sell boar all": STACKABLES_WAIT,
    "pls sell cookie all": STACKABLES_WAIT,
    "pls sell dear all": STACKABLES_WAIT,    
    "pls sell duck all": STACKABLES_WAIT,
    "pls sell fish all": STACKABLES_WAIT,
    "pls sell junk all": STACKABLES_WAIT,
    "pls sell rabbit all": STACKABLES_WAIT,
    "pls sell seaweed all": STACKABLES_WAIT,
    "pls sell skunk all": STACKABLES_WAIT,
    "pls sell work all": STACKABLES_WAIT,
}
_discord_dank_memer_wait_times_randomised = _discord_dank_memer_wait_times
_discord_dank_memer_prev_action = {}

def discord_dank_memer():
    global _discord_dank_memer_wait_times
    global _discord_dank_memer_wait_times_randomised
    global _discord_dank_memer_prev_action
    time_int = int(time.time())
    for action in _discord_dank_memer_wait_times:
        if action not in _discord_dank_memer_prev_action:
            _discord_dank_memer_prev_action[action] = random.randint(int(time.time()-30),int(time.time()+30))
        if _discord_dank_memer_prev_action[action]+_discord_dank_memer_wait_times_randomised[action] < time_int and max(_discord_dank_memer_prev_action.values())+(random.randint(1000,3000)/1000) < time_int:
            print(action)
            layout.write(action)
            kbd.send(Keycode.ENTER)
            _discord_dank_memer_prev_action[action] = time_int
            _discord_dank_memer_wait_times_randomised[action] = _discord_dank_memer_wait_times[action]+(random.randint(2000,8000)/1000)
    if time_int % 5 == 0:
        print(_discord_dank_memer_wait_times_randomised)

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
buttonA.pull = digitalio.Pull.DOWN
buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

current_app = 0
running_app = False
while True:
    current_app %= len(apps)
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
            running_app = True
            time.sleep(2)
        elif buttonA.value:
            time.sleep(2)
            if buttonA.value and buttonB.value:
                running_app = True
                time.sleep(2)
            else:
                current_app -= 1
                time.sleep(1)
        elif buttonB.value:
            time.sleep(2)
            if buttonA.value and buttonB.value:
                running_app = True
                time.sleep(2)
            else:
                current_app += 1
                time.sleep(1)
