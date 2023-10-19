import w1thermsensor
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT )
led = GPIO.PWM(40,50)
fill = 0
led.start( fill )
sensor = w1thermsensor.W1ThermSensor()
for i in range(0,60):

    
    time.sleep(0.5)
    temp = sensor.get_temperature()
    print(temp)

    if temp > 25 and temp <=35:
        fill = (temp-25)*10
        
    led.ChangeDutyCycle(fill)

led.stop ()
GPIO.cleanup ()

