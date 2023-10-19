import RPi.GPIO as GPIO
import time

RED = 40
YELLOW = 38
GREEN = 36

GPIO.setwarnings( False )
GPIO.setmode(GPIO.BOARD )
GPIO.setup(RED, GPIO.OUT )
GPIO.setup(YELLOW, GPIO.OUT )
GPIO.setup(GREEN, GPIO.OUT )
sleep_time = 1

for i in range(0 , 10) :
    GPIO.output(RED, GPIO.HIGH )
    GPIO.output(YELLOW, GPIO.LOW )
    GPIO.output(GREEN, GPIO.LOW )
    time.sleep(sleep_time)
    GPIO.output(YELLOW, GPIO.HIGH )
    time.sleep(sleep_time)
    GPIO.output(RED, GPIO.LOW )
    GPIO.output(YELLOW, GPIO.LOW )
    GPIO.output(GREEN, GPIO.HIGH )
    time.sleep(sleep_time)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH )
    time.sleep(sleep_time)

GPIO.cleanup ()