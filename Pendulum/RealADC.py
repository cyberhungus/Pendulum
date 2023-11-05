import ADS1115
import time
from threading import Thread
ads = ADS1115.ADS1115()

#this class ist for reading the actual ADS1115 module

class ADC(object):
    currentMeasurement = [0,0,0,0]
    lastMeasurementRuntime = 0
    delay = 0.1

    #init object, start data getter thread
    def __init__(self,delay=0.1):
        print("Real ADC")
        self.delay = delay
        self.dataGetterThread = Thread(target=self.gatherNewValues)
        self.dataGetterThread.start()

    #loop. gets data and stores it in variables
    def gatherNewValues(self):  
        while 1:
            print("Ran FakeData")
            for i in range(0,4):
                volt = ads.readADCSingleEnded(channel=i , pga=4096)
                self.currentMeasurement[i] = volt;
                self.lastMeasurementRuntime = time.thread_time()

                time.sleep(self.delay)
    #getter, returns tuple with last time and the list of measurements
    def getCurrentValues(self):
        return (self.lastMeasurementRuntime, self.currentMeasurement)






