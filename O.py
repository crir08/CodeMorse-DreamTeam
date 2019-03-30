from gpiozero import LED
from time import sleep


def O():
	led = LED(17)

	led.on()
	sleep(3)

	led.off()
	sleep(1)

	led.on()
	sleep(3)

	led.off()
	sleep(1)

	led.on()
	sleep(3)

	led.off()
	sleep(3)
