# Ceci est la lettre E
from gpiozero import LED
from time import sleep

led=LED(17)



led.on()
sleep(1)

led.off()
