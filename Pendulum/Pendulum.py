import imp
import platform
if platform.system() == "Windows":
    from FakeADC import FakeADC
    ADModule = FakeADC()
    print("selected windows")
else:
    from RealADC import ADC
    ADModule = ADC()
    print("selected linux")



from DataContainer import DataContainer
from time import thread_time
from threading import Thread
import FlaskWebInterface

print()
DC = DataContainer().getInstance()

def getDataRunner():
    while 1:
        print(thread_time(), ADModule.getCurrentValues()[1][0]);
        DC.setMeasurements(ADModule.getCurrentValues()[1][0],ADModule.getCurrentValues()[1][1],thread_time())





dataTransfer = Thread (target = getDataRunner)
dataTransfer.start()
webThread = Thread(target = FlaskWebInterface.startWebInterface, args=(True, ))
webThread.start()





