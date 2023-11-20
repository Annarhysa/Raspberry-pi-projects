import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)

while True:
    button_state = GPIO.input(23)
    if button_state == True:
        GPIO.output(24, True)
        print("Button pressed...")
        time.sleep(0.2)
    else:
        GPIO.output(24, False)