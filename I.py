# Ceci est la lettre I
from gpiozero import LED
from time import sleep


def I():
	led=LED(17)
    led.on()
    sleep(1)
    led.off()
    sleep(1)

    led.on()
    sleep(1)
    led.off()





