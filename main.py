import BlynkLib
import machine
import wificonnect as wi  # connecting to wifi ssid and password
import main_esp8266 as co
import sys

print("main")
wi.wificon()

print("back to main")

h = 0
v = 0
sp = 100
""""

In your Blynk App project:
  Add a Slider widget,
  bind it to Virtual Pin V3.
  Run the App (green triangle in the upper right corner)
It will automagically call v3_write_handler.
In the handler, you can use args[0] to get current slider value.

"""

BLYNK_AUTH = 'alhUz-99UwqC-KHrW_p9s7tAHOu1dQTC'  # authentication key

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
print("auth done")

blynk = BlynkLib.Blynk(BLYNK_AUTH)


# Register virtual pin handler
@blynk.on("V3")
def v3_write_handler(value):
    # print('Current slider value: {},vertical'.format(value[0]))
    global v
    v = int(value[0])
    # print(value,)


@blynk.on("V2")
def v2_write_handle(value):
    # print('Current slider value: {},horizontal'.format(value[0]))
    global h
    h = int(value[0])
    # print(value)


@blynk.on("V1")
def v2_write_handle(value):
    global sp
    sp = int(value[0])


def runLoop():
    while True:
        blynk.run()
        global h, sp, v
        co.cont(h, v, sp)
        machine.idle()


print("loop started")
runLoop()
