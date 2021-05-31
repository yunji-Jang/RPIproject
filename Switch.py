import RPi.GPIO as GPIO
import I2C_driver as LCD
import time

mylcd = LCD.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED=12
Switch= 10

GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, pull_up_down =  GPIO.PUD_DOWN)

while True:
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was Pushed! Switch ON")
        GPIO.output(LED, GPIO.HIGH)
        mylcd.lcd_display_string("LED ON",1)
    else:
        print("Button was not Pushed! Switch OFF")
        GPIO.output(LED, GPIO.LOW)
        mylcd.lcd_display_string("LED OFF",2)
        time.sleep(1)
 
