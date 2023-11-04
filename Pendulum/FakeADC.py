from random import Random
from threading import Thread
from unittest import runner
from time import sleep, thread_time

class FakeADC(object):
    def __init__(self):
        print("FakeADC")
        self.dataGetterThread = Thread(target=self.makeNewValues)
        #Maybe use a dictionary here
        self.list = [0,0,0,0]
        self.dataGetterThread.start()

    def makeNewValues(self):
        r = Random()
        while 1:
            for i in range(0,4):
                self.list[i] = r.randint(0,5000)
            sleep(0.1)

    def getCurrentValues(self):
        return (thread_time, self.list)



