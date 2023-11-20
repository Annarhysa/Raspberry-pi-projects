import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

global positive_edge
positive_edge = 0

global negative_edge
negative_edge = 0

def ISRL2H():
    global positive_edge
    positive_edge += 1
    print("Number of positive edge occurences: ", positive_edge)
    GPIO.output(18,1)
    time.sleep(1)
    GPIO.output(18,0)
    time.sleep(2)

def ISRH2L():
    global negative_edge
    negative_edge += 1
    print("Number of negative edge occurences: ", negative_edge)
    GPIO.output(23,1)
    time.sleep(1)
    GPIO.output(23,0)
    time.sleep(2)

while True:
    GPIO.output(18,1)
    time.sleep(2)
    GPIO.output(23,1)
    time.sleep(2)
    GPIO.output(18,0)
    time.sleep(2)
    GPIO.output(23,0)
    time.sleep(2)

    ch = input("enter 1 if there is a positive edge and o if there is a negative edge: ")
    if ch == '1':
        ISRL2H()
    elif ch == '0':
        ISRH2L()
    
    ip = input("enter yes f you want to exit the program: ")

    if ip == 'yes':
        break

