from gpiozero import LED
from time import sleep


def N():
	led = LED(17)
	
	led.on()
	sleep(3)

	led.off()
	sleep(1)

	led.on()
	sleep(1)

	led.off()
	sleep(1)
