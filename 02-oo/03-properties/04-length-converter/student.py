class LengthConverter:
    FEET_PER_METER = 3.28084
    INCH_PER_METER = 39.3701

    def __init__(self):
        self.__length_in_meter = 0
        
    @property
    def meter(self):
        return self.__length_in_meter 

    @meter.setter
    def meter(self, value):
        self.__length_in_meter = value

    @property
    def feet(self):
        return LengthConverter.FEET_PER_METER * self.__length_in_meter

    @feet.setter
    def feet(self, value):
        LengthConverter.FEET_PER_METER / self.__length_in_meter
    
    @property
    def inch(self):
        return self.__length_in_meter * LengthConverter.INCH_PER_METER

    @inch.setter
    def inch(self, value):
        self.__length_in_meter / LengthConverter.INCH_PER_METER
    