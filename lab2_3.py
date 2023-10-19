import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import w1thermsensor
import time

lcd=CharLCD(pin_rs=15, pin_rw =18, pin_e=16, pins_data=[21,22,23,24], numbering_mode = GPIO.BOARD, cols=16, rows=2, dotsize=8)

lcd.clear ()
lcd.write_string ("Industry 4.0 ")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT )
contrast = GPIO.PWM(40,50)
fill = 50
contrast.start(fill)
sensor = w1thermsensor.W1ThermSensor()
for i in range(0,60):

    time.sleep(1)
    temp = sensor.get_temperature()
    print(f"Temp: {temp:.2f}")
    lcd.clear ()
    lcd.write_string (f"Temp: {temp:.2f}")

contrast.stop ()
GPIO.cleanup ()