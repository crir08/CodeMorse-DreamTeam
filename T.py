from gpiozero import LED
from time import sleep

led = LED(17)

def T():
	led.on()
	sleep(3)
	led.off()


