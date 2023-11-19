import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
    duty_s = raw_input("Enter the brightness you want (0-100): ")
    duty = int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
    GPIO.output(led_pin, True)
    time.sleep(0.5)
    GPIO.output(led_pin, False)
    time.sleep(0.5)