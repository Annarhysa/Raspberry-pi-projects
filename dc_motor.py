import RPi.GPIO as GPIO
import time
relay = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

for i in range(4):
    GPIO.output(relay, GPIO.LOW)
    print("Relay Switched on")
    GPIO.output(relay, GPIO.HIGH)
    print("Relay Switched off")
    time.sleep(1)