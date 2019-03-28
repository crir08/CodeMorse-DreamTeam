# Ceci est la lettre D
from gpiozero import LED
from time import sleep

led=LED(17)
def D():
    led.on()
    sleep(3)

    led.off()
    sleep(1)

    led.on()
    sleep(1)
    led.off()
    sleep(1)

    led.on()
    sleep(1)

    led.off()



