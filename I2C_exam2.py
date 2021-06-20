import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *

mylcd = LCD.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED1 = 12
LED2 = 10
Switch1 = 16
Switch2 = 18

GPIO.setup(LED1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Switch1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Switch2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if GPIO.input(Switch1) == GPIO.HIGH:
        GPIO.output(LED1, GPIO.HIGH)
        print("Button was Pushed!! Switch ON")
        mylcd.lcd_display_string("LED1 ON",1)

    elif GPIO.input(Switch2) == GPIO.HIGH:
        GPIO.output(LED2, GPIO.HIGH)
        print("Button was pushed!! Switch ON")
        mylcd.lcd_display_string("LED2 ON",1)
    
    else:
        print("Button was not Pushed!! Switch OFF")
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.LOW)
        mylcd.lcd_display_string("LED OFF",2)
        sleep(1)
        mylcd.lcd_clear()
sleep(3)



