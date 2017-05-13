#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

import Adafruit_DHT

import time

import datetime

import sqlite3 as mydb

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

GPIO.setwarnings(False)

#sensor = Adafruit_DHT.DHT22

#pin = 4

#Parse command line parameters.
#sensor_args = { '11': Adafruit_DHT.DHT11,
#               '22': Adafruit_DHT.DHT22,
#                '2302': Adafruit_DHT.AM2302 }
#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#    sensor = sensor_args[sys.argv[1]]
#    pin = sys.argv[2]
#else:
#    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
#    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
#    sys.exit(1)
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

# Un-comment the line below to convert the temperature to Fahrenheit.


# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
#int pulse
#int timeFrame
#String TF

#timePulse = ""



def maxTime():
        
	timeFrame = int(raw_input('What is the desired time frame in ' + timePulse + '? Please input a number.' + '\n')) 
        if timePulse == "Seconds":
                for i in range (0,timeFrame):
                        GPIO.output(4,True)
                        time.sleep(1)
                        storeTemp()
	elif timePulse == "Minutes":
                for i in range (0,timeFrame):
                        GPIO.output(4,True)
                        time.sleep(60)
                        storeTemp()        

	elif timePulse == "Hours":
                for i in range (0,timeFrame):
                        GPIO.output(4,True)
                        time.sleep(3600)
                        storeTemp()
	
	else:
	    maxTime()
        
        #storeTemp()

def readTemp():
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
    		stored = str('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    		print(stored)
	else:
    		print('Failed to get reading. Try again!')
        return [stored]

con = mydb.connect('temperature.db')

with con:
        con.execute('DROP TABLE IF EXISTS temperatureTable')
        con.execute(''' CREATE TABLE temperatureTable
                                (STORED STRING NOT NULL);''')
        con.commit()
        
def storeTemp():
                
                try:
                        
			[stored] = readTemp()
			print "Current temperature is: %s stored" %stored
			print "Temperture Read"
			cur = con.cursor()
			#sql = "insert into temperatureTable values(?,?)"
			cur.execute("INSERT INTO temperatureTable VALUES('%s')"%(stored))
			con.commit()
			print "Temperature has been Stored"
		except:
			print "Error!!! :("
	
def recordTime():
        global timePulse
	timePulse = raw_input('How often do you want a reading? Seconds, Minutes, or Hours.' + '\n')
	
	if timePulse == "Seconds":
	    pulse = 1
	    maxTime()
	
	elif timePulse == "Minutes":
	    pulse = 60
	    maxTime()

	elif timePulse == "Hours":
	    pulse = 3600
	    maxTime()
	
	else:
	    recordTime()
recordTime()	
