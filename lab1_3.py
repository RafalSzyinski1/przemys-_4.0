import RPi.GPIO as GPIO
import time

RED = 40
GPIO.setwarnings( False )
GPIO.setmode(GPIO.BOARD )
sleep_time = 0.5
GPIO.setup(26 , GPIO.IN , pull_up_down = GPIO.PUD_UP )
GPIO.setup(RED, GPIO.OUT )
flaga = 0
GPIO.output(RED, GPIO.LOW)
while True:
    if GPIO.input(26) == 0:
        print(" button pressed !")
        if flaga == 0:
            GPIO.output(RED, GPIO.HIGH )
            flaga = 1
            time.sleep(sleep_time)
        else:
            GPIO.output(RED, GPIO.LOW)
            flaga = 0
            time.sleep(sleep_time)

GPIO.cleanup ()