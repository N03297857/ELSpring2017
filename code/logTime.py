#!/usr/bin/python
import time
import sqlite3 as mydb
import sys
def dateTime():
        Time = time.strftime("%H:%M:%S")
        Date = time.strftime("%d/%m/%Y")
        return [Time, Date]
def logTime():
        con = mydb.connect("time.db")
        print ("Database Created.")
        con.execute('''CREATE TABLE Time (TIME TEXT NOT NULL,
                                        DATE TEXT NOT NULL);''')
        try:
                [T, D] = dateTime()
                cur = con.cursor()
                cur.execute('Insert into Time Values(?,?)', (T, D))
                print "Time Logged"
        except:
                print "Error!"
dateTime()
logTime()
