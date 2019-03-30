from gpiozero import LED
from time import sleep

def S():
	led = LED(17)
	led.on()
	sleep(1)
	led.off()
	sleep(1)
	led.on()
	sleep(1)
	led.off()
	sleep(1)
	led.on()
	sleep(1)
	led.off()
	sleep(3)

