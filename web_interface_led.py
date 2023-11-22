from bottle import route, run
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led_pins = [18, 23, 24]
led_states = [0, 0, 0]
switch_pin = 25
GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(led_pins[2], GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def switch_status():
    state = GPIO.input(switch_pin)
    if state:
        return 'Up'
    else:
        return 'Down'
def html_for_led(led):
    l = str(led)
    result = " <input type='button' onClick='changed(" + l + ")' value='LED " + l + "'/>"
    return result
def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pins[i], value)
@route('/')
@route('/<led>')
def index(led):
    if led >= '0' and led <= '9':
        led_num = int(led)
        led_states[led_num] = not led_states[led_num]
        update_leds()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "  window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>Annarhysa Albert (RA2111047010144) Raspberry Pi Mini Project</h1>'
    response += '<h2>Button Status = ' + switch_status() + '</h2>'
    response += '<h2>LEDs Buttons</h2>'
    response += html_for_led(0) 
    response += html_for_led(1) 
    response += html_for_led(2) 
    return response
try:
    run(host='localhost',port=7000,debug=True)
finally:
    print('\nCleaning up')
    GPIO.cleanup()
