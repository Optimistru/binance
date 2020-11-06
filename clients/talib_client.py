import numpy
import talib


class MathClient:
    def __init__(self):
        pass

    def MA(self, array, timeperiod):
        close = numpy.asarray(array)
        return talib.MA(close, timeperiod=timeperiod, matype=0)
