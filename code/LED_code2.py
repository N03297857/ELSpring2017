#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
def Blink():
 try:
  while True:
   for i in range(0,3):
    print "blink #" + str(i+1)
    GPIO.output(17,True)
    time.sleep(1)
    GPIO.output(17,False)
    time.sleep(1)
   time.sleep(5)
   for j in range(0,4):
    print "blink #" + str(j+1)
    GPIO.output(17,True)
    time.sleep(1)
    GPIO.output(17,False)
    time.sleep(1)
   time.sleep(5)
 except KeyboardInterrupt:
   print ("done!!")
Blink()
GPIO.cleanup()
