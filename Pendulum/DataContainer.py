#singleton for data management - this class holds all variables 
#acts like a translator between Flask and Python
class DataContainer(object):
   
    MeasurementA = 0
    MeasurementB = 0
    lastTime = 0
    measurementList = []


    __instance = None


    #Singleton, always call getInstance
    @staticmethod
    def getInstance():
        """ Static access method. """
        if DataContainer.__instance == None:
            DataContainer()
        return DataContainer.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DataContainer.__instance != None:
            raise Exception("This class is a DataContainer!")
        else:
            DataContainer.__instance = self
            print("DataContainer init")


    #called to set new data
    def setMeasurements(cls, A, B, time):
        cls.MeasurementA = A
        cls.MeasurementB = B 
        cls.lastTime = time
        cls.measurementList.append((time,A,B))
        if len(cls.measurementList)>1000:
            cls.measurementList.pop(0)






