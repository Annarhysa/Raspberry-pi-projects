import RPi.GPIO as GPIO
import time
A1 = 17
A2 = 18
B1 = 22
B2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(A1, GPIO.OUT)
GPIO.steup(A2, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)

forward_sequence = ['1010', '0110', '0101', '1001']
reverse_sequence = list(reversed(forward_sequence))

direction = input("Enter forward of reverse: ")
num_steps = int(input("Enter the number of steps: "))

if direction == 'forward':
    sequence = forward_sequence
elif direction == 'reverse':
    sequence = reverse_sequence
else:
    print("Invalid direction. Please enter forward or reverse: ")
    GPIO.cleanup()
    exit()


for _ in range(num_steps):
    for step in sequence:
        GPIO.output(A1, int(step[0]))
        GPIO.output(A2, int(step[1]))
        GPIO.output(B1, int(step[2]))
        GPIO.output(B2, int(step[3]))
        time.sleep(0.5)

GPIO.cleanup()