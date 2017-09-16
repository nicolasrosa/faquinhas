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
 
brightness = 0  # Global variable to store brightness level
inc = 1         # How much to increment the brightness by
pause = 1       # Delay in ms between each step 

# Create a setup function:
def setup():
  # nothing to do here
  pass

# Create a main function:
def loop():
  global brightness, inc

  # Set the PWM duty cycle:
  analogWrite(motor0_pwm, brightness)
  analogWrite(motor1_pwm, brightness)
  analogWrite(motor2_pwm, brightness)
  analogWrite(motor3_pwm, brightness)

  # Increment value:
  brightness += inc
  if ((brightness == 255) or (brightness == 0)):
    # Change increment direction:
    inc *= -1

  # Sleep a bit:
  delay(pause)

# Start the loop:
run(setup, loop)
