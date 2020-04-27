import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print('GPIO21: %s' % (GPIO.input(21)))
    time.sleep(1)
