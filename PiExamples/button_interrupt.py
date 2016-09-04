import RPi.GPIO as GPIO
import time

def button_event(channel):
    print('Button press detected')

button_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(button_pin, GPIO.FALLING,
                      callback=button_event, bouncetime=100)

while True:
    # Do whatever else you need to do here
    time.sleep(10)
    print('I am alive')

GPIO.cleanup()
