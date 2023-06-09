import network
import machine
import time
wlan= network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("**WIFI_ISMINIZ**","**SIFRENIZ**")
print(wlan.isconnected())

while wlan.isconnected():
    led = machine.Pin('LED', machine.Pin.OUT)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
    
