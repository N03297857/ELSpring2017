import time
def dateTime():
        Time = time.strftime("%H:%M:%S")
        Date = time.strftime("%d/%m/%Y")
        return [Time, Date]
dateTime()
