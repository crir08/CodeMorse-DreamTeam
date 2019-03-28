# Ceci est la lettre D
from gpiozero import LED
from time import sleep


def D():
    led=LED(17)
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



