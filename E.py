# Ceci est la lettre E
from gpiozero import LED
from time import sleep



def E():
	led=LED(17)
    led.on()
    sleep(1)

    led.off()
