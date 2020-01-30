import requests

from EmulatorGUI import GPIO
# import RPi.GPIO as GPIO

URL = "http://www.isspelmanopen.com/changeStatus"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN) #11, ground
GPIO.setup(17, GPIO.OUT) #15, output

try:
    while True:
        GPIO.output( 17, GPIO.setup(22, GPIO.IN) )
        #r = requests.get(url = URL) 
        #print(r)
except KeyboardInterrupt:
    GPIO.cleanup()
