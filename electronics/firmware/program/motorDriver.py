#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ===========
#  Libraries
# ===========
from bbio import *
from time import sleep

# ===================
#  Class Declaration
# ===================
class MotorDriver(object):
    def __init__(self):
        self.printHello()

        # Variables
        nDirPins, nMotors = 2, 4;

        self.motor_pwm_pin = []
        self.motor_dir_pin = [[0 for x in range(nDirPins)] for y in range(nMotors)]

        self.MOTOR_DIR_CW = 0
        self.MOTOR_DIR_CCW = 1

    def printHello(self):
        print("Hello, motorDriver.")

    def configPWMpins(self):
        # Motor 0 PWM Pin
        self.motor_pwm_pin.append(PWM1A) # P9_14 

        # Motor 1 PWM Pin
        self.motor_pwm_pin.append(PWM1B) # P9_16

        # Motor 2 PWM Pin
        self.motor_pwm_pin.append(PWM2B) # P8_13

        # Motor 3 PWM Pin
        self.motor_pwm_pin.append(PWM2A) # P8_19

    def configGPIOpins(self):
        # Pins Definition
        # Motor 0 Direction Pins
        self.motor_dir_pin[0][0] = GPIO0_30  # P9_11
        self.motor_dir_pin[0][1] = GPIO0_31  # P9_13

        # Motor 1 Direction Pins
        self.motor_dir_pin[1][0] = GPIO1_16 # P9_15
        self.motor_dir_pin[1][1] = GPIO0_5  # P9_17

        # Motor 2 Direction Pins
        self.motor_dir_pin[2][0] = GPIO0_13 # P9_19
        self.motor_dir_pin[2][1] = GPIO0_3 # P9_21

        # Motor 3 Direction Pins
        self.motor_dir_pin[3][0] = GPIO1_17 # P9_23
        self.motor_dir_pin[3][1] = GPIO3_21 # P9_25

        # Pins Configuration
        pinMode(self.motor_dir_pin[0][0], OUTPUT)
        pinMode(self.motor_dir_pin[0][1], OUTPUT)

        pinMode(self.motor_dir_pin[1][0], OUTPUT)
        pinMode(self.motor_dir_pin[1][1], OUTPUT)

        pinMode(self.motor_dir_pin[2][0], OUTPUT)
        pinMode(self.motor_dir_pin[2][1], OUTPUT)

        pinMode(self.motor_dir_pin[3][0], OUTPUT)
        pinMode(self.motor_dir_pin[3][1], OUTPUT)

    # digitalWrite(GPIO0,HIGH)
    # digitalWrite(GPIO1,LOW)

    def setMotorDirection(self, motor, dir):
        if dir == self.MOTOR_DIR_CW:
            digitalWrite(self.motor_dir_pin[motor][0], HIGH)
            digitalWrite(self.motor_dir_pin[motor][1], LOW)
        if dir == self.MOTOR_DIR_CCW:
            digitalWrite(self.motor_dir_pin[motor][0], LOW)
            digitalWrite(self.motor_dir_pin[motor][1], HIGH)

    @staticmethod
    def setDutyCycle(pwm_pin, duty_float):
        assert duty_float >= 0.0 and duty_float <= 1.0, "Houston, We have a problem! Duty Cycle value should be between [0.0,1.0]."
        duty = round(255*duty_float)
        analogWrite(pwm_pin, duty) # duty range: 0-255

    def goRear(self,speed, time):
        # Set Motors direction for going forward
        self.setMotorDirection(0, self.MOTOR_DIR_CW)
        self.setMotorDirection(1, self.MOTOR_DIR_CCW)
        self.setMotorDirection(2, self.MOTOR_DIR_CCW)
        self.setMotorDirection(3, self.MOTOR_DIR_CW)

        # Set the desired speed to the motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], speed)

        # Sleep a bit:
        sleep(time)
        
        # Stops the Motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], 0)

    def goForward(self,speed,time):
        # Set Motors direction for going forward
        self.setMotorDirection(0, self.MOTOR_DIR_CCW)
        self.setMotorDirection(1, self.MOTOR_DIR_CW)
        self.setMotorDirection(2, self.MOTOR_DIR_CW)
        self.setMotorDirection(3, self.MOTOR_DIR_CCW)

        # Set the desired speed to the motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], speed)

        # Sleep a bit:
        sleep(time)
        
        # Stops the Motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], 0)

    def turnLeft(self,speed, time):
        # Set Motors direction for going forward
        self.setMotorDirection(0, self.MOTOR_DIR_CW)
        self.setMotorDirection(1, self.MOTOR_DIR_CW)
        self.setMotorDirection(2, self.MOTOR_DIR_CCW)
        self.setMotorDirection(3, self.MOTOR_DIR_CCW)

        # Set the desired speed to the motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], speed)

        # Sleep a bit:
        sleep(time)
        
        # Stops the Motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], 0)

    def turnRight(self,speed,time):
        # Set Motors direction for going forward
        self.setMotorDirection(0, self.MOTOR_DIR_CCW)
        self.setMotorDirection(1, self.MOTOR_DIR_CCW)
        self.setMotorDirection(2, self.MOTOR_DIR_CW)
        self.setMotorDirection(3, self.MOTOR_DIR_CW)

        # Set the desired speed to the motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], speed)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], speed)

        # Sleep a bit:
        sleep(time)
        
        # Stops the Motors
        MotorDriver.setDutyCycle(self.motor_pwm_pin[0], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[1], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[2], 0)
        MotorDriver.setDutyCycle(self.motor_pwm_pin[3], 0)