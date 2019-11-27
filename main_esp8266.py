from dcmotor import DCMotor
from machine import Pin, PWM

frequency = 15000

"""
#define ENAR   14         --> Enable/speed motors Right        GPIO14(D5)
#define ENBL   12         --> Enable/speed motors Left         GPIO12(D6)
#define pin1  15          --> L298N in1 motors Right           GPIO15(D8)
#define pin2  13          --> L298N in2 motors Right           GPIO13(D7)
#define pin3  2           --> L298N in3 motors Left            GPIO2(D4)
#define pin4  0           --> L298N in4 motors Left            GPIO0(D3)
"""

pin1 = Pin(15, Pin.OUT)
pin2 = Pin(13, Pin.OUT)
enableFB = PWM(Pin(14), frequency)
dc_motorFB = DCMotor(pin1, pin2, enableFB, 350, 1023)

enableRL = PWM(Pin(12), frequency)
pin3 = Pin(2, Pin.OUT)
pin4 = Pin(0, Pin.OUT)
dc_motorRL = DCMotor(pin3, pin4, enableRL, 350, 1023)


def cont(y, x,s):
    print('h,v,s=', y, x,s)
    r = 1023 / (2 ** .5)

    if (-r < x and x < r and y > 0):  # forward
        dc_motorFB.forward(s)
        dc_motorRL.stop()
        print("forword")
    elif (-r < x and x < r and y < 0):  # backward
        dc_motorFB.backwards(s)
        dc_motorRL.stop()
        print("backward")
    elif (0 < y and y < r and x > 0):  # rightForword
        dc_motorFB.forward(s)
        dc_motorRL.forward(40)
        print("right_Forward")
    elif (-r < y and y < 0 and x > 0):  # rightBactwards
        dc_motorFB.backwards(s)
        dc_motorRL.forward(40)
        print("rigthBackward")

    elif (0 < y and y < r and x < 0):  # leftForward
        print("leftForword")
        dc_motorFB.forward(s)
        dc_motorRL.backwards(40)

    elif (-r < y and y < 0 and x < 0):  # leftBackwards
        print('leftBackward')
        dc_motorFB.backwards(s)
        dc_motorRL.backwards(40)

    elif (y == 0 and x == 0):
        dc_motorFB.stop()
        dc_motorRL.stop()
        print("stop")
