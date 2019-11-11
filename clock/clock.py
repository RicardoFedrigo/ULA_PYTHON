from time import sleep
from portasLogicas import NOT
class Clock(object):
    
    def __init__(self,time):
        self.clockTimeWait = float(time)
        self.clock = int(0)

    def perildo(self):

            sleep(self.clockTimeWait)
            self.setEstadoClock()

    def setEstadoClock(self):
        self.clock = NOT(self.clock)

    def getEstadoClock(self):

        return self.clock