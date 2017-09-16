#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Libraries # 
# Import PyBBIO library:
from bbio import *

from motorDriver import *
from vision import *
from robotAI import *

# motorDriver.printHello()
# vision.printHello()
# robotAI.printHello()

# ===========
#  Variables
# ===========
# MotorDriver()
# Vision()
# RobotAI()

motorObj = MotorDriver()

def manual():
    # Get PWM duty cycle:
    motor0_duty = float(input("motor0_duty: "))
    motor1_duty = float(input("motor1_duty: "))
    # motor2_duty = float(input("motor2_duty: "))
    # motor3_duty = float(input("motor3_duty: "))

    # Set the PWM duty cycle:
    MotorDriver.setDutyCycle(motorObj.motor_pwm_pin[0], motor0_duty)
    MotorDriver.setDutyCycle(motorObj.motor_pwm_pin[1], motor1_duty)
    # setDutyCycle(motor2_pwm, motor2_duty)
    # setDutyCycle(motor3_pwm, motor3_duty)

# ======
#  Main
# ======
# Create a setup function:
def setup():
    motorObj.configPWMpins()        
    motorObj.configGPIOpins()
    
    # Initial Motors Direction
    motorObj.setMotorDirection(0, motorObj.MOTOR_DIR_CW)
    motorObj.setMotorDirection(1, motorObj.MOTOR_DIR_CCW)
    # motorObj.setMotorDirection(2, MOTOR_DIR_CW)
    # motorObj.setMotorDirection(3, MOTOR_DIR_CCW)

    # Initial Motors Speeds
    MotorDriver.setDutyCycle(motorObj.motor_pwm_pin[0], 0)
    MotorDriver.setDutyCycle(motorObj.motor_pwm_pin[1], 0)
    # MotorDriver.setDutyCycle(motorObj.motor_pwm_pin[2], 0)
    # MotorDriver.setDutyCycle(motorObj.motor_pwm_pin[3], 0)

    # Debug
    # print(motorObj.motor_pwm_pin)
    # print(motorObj.motor_dir_pin)
    # input("Press")

    motorObj.goForward(0.4, 1)
    motorObj.goRear(0.4, 1)
    motorObj.turnLeft(0.4, 1)
    motorObj.turnRight(0.4, 1)

# Create a main function:
def loop():
    # manual()

    pass

# Start the loop:
run(setup, loop)
