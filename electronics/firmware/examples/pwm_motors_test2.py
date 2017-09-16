# fade.py - Alexander Hiam - 10/2012
# Uses pulse width modulation to fade an LED on PWM1A
# (pin 14 on header P9).
#
# This example is in the public domain

# Import PyBBIO library:
from bbio import *

motor0_pwm = PWM1A # P9_14
motor1_pwm = PWM1B # P9_16
motor2_pwm = PWM2B # P8_13
motor3_pwm = PWM2A # P8_19

GPIO0 = GPIO0_30
GPIO1 = GPIO0_31
GPIO2 = GPIO1_16
GPIO3 = GPIO0_5


# pause = 1       # Delay in ms between each step 

def setDutyCycle(pwm_pin, duty_float):
    # assert duty_float >= 0.0 and duty_float <= 1.0, "Houston, We have a problem! Duty Cycle value should be between [0.0,1.0]."
    duty = round(255*duty_float)
    analogWrite(pwm_pin, duty) # duty range: 0-255

# Create a setup function:
def setup():
    pinMode(GPIO0, OUTPUT)
    pinMode(GPIO1, OUTPUT)
    pinMode(GPIO2, OUTPUT)
    pinMode(GPIO3, OUTPUT)

    digitalWrite(GPIO0,HIGH)
    digitalWrite(GPIO1,LOW)
    digitalWrite(GPIO2,HIGH)
    digitalWrite(GPIO3, LOW)

    pass

# Create a main function:
def loop():
    # Get PWM duty cycle:
    
    motor0_duty = float(input("motor0_duty: "))
    motor1_duty = float(input("motor1_duty: "))
    # motor2_duty = float(input("motor2_duty: "))
    # motor3_duty = float(input("motor3_duty: "))

    # Set the PWM duty cycle:
    setDutyCycle(motor0_pwm, motor0_duty)
    setDutyCycle(motor1_pwm, motor1_duty)
    # setDutyCycle(motor2_pwm, motor2_duty)
    # setDutyCycle(motor3_pwm, motor3_duty)
    
    # Sleep a bit:
    # delay(pause)

# Start the loop:
run(setup, loop)
