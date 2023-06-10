import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
class Motor:
    __homeGPIO = None
    __direction = None
    __step = None
    __range = None
    __motor=None
    __GPIO_pins = (0, 0, 0)
    
    def __init__(self,homeGPIO,direction,step,range):
        self.__homeGPIO=homeGPIO
        self.__direction=direction
        self.__step=step
        self.__range=range
        GPIO.setup(self.__homeGPIO,GPIO.IN)
        self.__motor=RpiMotorLib.A4988Nema(self.__direction, self.__step, self.__GPIO_pins, "A4988")
    def Home(self):
        while GPIO.input(self.__homeGPIO):
            self.__motor.motor_go(True, "Full" , 10, .001, False, .001)
        return
    def Go(self):
        for i in range(0,self.__step):
            self.__motor.motor_go(False, "Full" , 10, .001, False, .001)
        return