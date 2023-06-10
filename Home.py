from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib


# HOME
xHome_GPIO=26
yHome_GPIO=19
zHome_GPIO=13

# X Motor Sürücü
xDirection= 20
xStep = 21

# Y Motor Sürücü
yDirection= 12
yStep = 16

# Z Motor Sürücü
zDirection=24 
zStep=25
GPIO_pins = (0, 0, 0)


xRange=192

GPIO.setmode(GPIO.BCM)

GPIO.setup(xHome_GPIO, GPIO.IN) 
GPIO.setup(yHome_GPIO, GPIO.IN) 
GPIO.setup(zHome_GPIO, GPIO.IN) 

xMotor = RpiMotorLib.A4988Nema(xDirection, xStep, GPIO_pins, "A4988")
yMotor = RpiMotorLib.A4988Nema(yDirection, yStep, GPIO_pins, "A4988")
zMotor = RpiMotorLib.A4988Nema(zDirection, zStep, GPIO_pins, "A4988")

def xHome():
    while GPIO.input(xHome_GPIO):
        xMotor.motor_go(True, "Full" , 10, .001, False, .001)
    return
    
def yHome():
    while GPIO.input(yHome_GPIO):
        yMotor.motor_go(False, "Full" , 10, .001, False, .001)
    return

def zHome():
    while GPIO.input(zHome_GPIO):
        zMotor.motor_go(False, "Full" , 10, .001, False, .001)
    return
def xGo(step):
    for i in range(0,step):
        xMotor.motor_go(False, "Full" , 10, .001, False, .001)
    return

def yGo(step):
    for i in range(0,step):
        yMotor.motor_go(True, "Full" , 10, .001, False, .001)
    return

def zGo(step):
    for i in range(0,step):
        zMotor.motor_go(True, "Full" , 10, .001, False, .001)
    return
    
xHome()
yHome()
zHome()

xGo(192)
yGo(250)
zGo(85)
# xGo(xRange)
# yHome=
# zHome=

