#check platform, load realADC when started on Linux, bur fakeADC when started on WIndows
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
#create singleton DataContainer
DC = DataContainer().getInstance()

#takes data from ADC and puts them into DataContainer
def getDataRunner():
    while 1:
        print(thread_time(), ADModule.getCurrentValues()[1][0]);
        DC.setMeasurements(ADModule.getCurrentValues()[1][0],ADModule.getCurrentValues()[1][1],thread_time())




#thread to get data from ADC to Datacontainer
dataTransfer = Thread (target = getDataRunner)
dataTransfer.start()

#web thread
webThread = Thread(target = FlaskWebInterface.startWebInterface, args=(True, ))
webThread.start()





