import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(3,GPIO.OUT)

try:
    while True:
        i = GPIO.input(11)
        if i ==0:
            print("No intruders", i)
            GPIO.output(3, 0)
            time.sleep(1)
        
        else:
            print("Intruders detected", i)
            GPIO.output(3,1)
            time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()