# -- ServoLightGauge.py - CircuitPython code for CP -- #

import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep

# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=500, max_pulse=2400)

# Function Section
def light_to_servo_pos(light):
    # Limit the light value to prevent exceeding the range
    light_max = 1000  # Adjust according to actual environment
    light = min(light, light_max)

    # Map light to servo angle 0~180°
    angle = 180 - ((light / light_max) * 180)

    # Ensure angle stays within 0~180°
    angle = max(0, min(180, angle))
    return angle

# Loop Section
while True:
    servo.angle = light_to_servo_pos(cp.light)
    print("Light:", cp.light, "Angle:", servo.angle)
    sleep(0.5)
