# Ceci est la lettre G
from gpiozero import LED
from time import sleep



def G():
	led=LED(17)
    led.on()
    sleep(3)
    led.off()
    sleep(1)

    led.on()
    sleep(3)
    led.off()
    sleep(1)

    led.on()
    sleep(1)
    led.off()



