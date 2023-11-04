import ADS1115
import time
from threading import Thread
ads = ADS1115.ADS1115()



class ADC(object):
    currentMeasurement = [0,0,0,0]
    lastMeasurementRuntime = 0
    delay = 0.1

    def __init__(self,delay=0.1):
        print("Real ADC")
        self.delay = delay
        self.dataGetterThread = Thread(target=self.gatherNewValues)
        self.dataGetterThread.start()

    def gatherNewValues(self):  
        while 1:
            print("Ran FakeData")
            for i in range(0,4):
                volt = ads.readADCSingleEnded(channel=i , pga=4096)
                self.currentMeasurement[i] = volt;
                self.lastMeasurementRuntime = time.thread_time()

                time.sleep(self.delay)

    def getCurrentValues(self):
        return (self.lastMeasurementRuntime, self.currentMeasurement)






