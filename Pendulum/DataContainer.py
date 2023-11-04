class DataContainer(object):
   
    MeasurementA = 0
    MeasurementB = 0
    lastTime = 0
    measurementList = []


    __instance = None

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



    def setMeasurements(cls, A, B, time):
        cls.MeasurementA = A
        cls.MeasurementB = B 
        cls.lastTime = time
        cls.measurementList.append((time,A,B))
        if len(cls.measurementList)>1000:
            cls.measurementList.pop(0)






