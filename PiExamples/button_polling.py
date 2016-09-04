import RPi.GPIO as GPIO
import time

button_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button_pin)

    if input_state is False:
        print('Button Press Detected')
        time.sleep(0.2)

GPIO.cleanup()
