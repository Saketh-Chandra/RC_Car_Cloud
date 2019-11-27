import BlynkLib
import network
import machine

def wificon():
    WIFI_SSID = 'saketh 1+6t'
    WIFI_PASS = 'Saketh 1+@6T'

    BLYNK_AUTH = '0CSfBwP0llBuor4SC3XvEJtJWwxk3Euy'

    print("Connecting to WiFi...")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASS)
    while not wifi.isconnected():
        pass

    print('IP:', wifi.ifconfig()[0])

    print("Connecting to Blynk...")
    blynk = BlynkLib.Blynk(BLYNK_AUTH)

    @blynk.on("connected")
    def blynk_connected(ping):
        print('Blynk ready. Ping:', ping, 'ms')
