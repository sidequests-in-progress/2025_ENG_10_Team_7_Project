#-- ServoLightGauge.py - CircuitPython code for CP --#
# UPDATE:
#   this implementation uses an array of light reads to calc a rolling average
#   to supress the gittering behavior of the servo due to fluctuating abmient light level
#
#   this may cause the servo to be unresponsive to very slowly changing lights


import board
import pwmio
import time
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep

# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)

# Parameters
light_max = 320
freq = 20  # Hz
ignore_window_width = 15  # larger = less sensitive to light change
num_keep_measure = 10

# Stats
t = 0
i = 0
light_history = [0] * num_keep_measure
start = time.time()
avg_light = 0
target_pos = 90  # default servo position

# Helper functions
def light_to_servo_pos(light, light_max):
    return 180 - ((light / light_max) * 180)

def clamp(val, lo, hi):
    return max(lo, min(val, hi))

# Main loop
while True:
    # read light sensor 
    light_value = cp.light

    # Update rolling average
    light_history[i] = light_value
    i = (i + 1) % num_keep_measure
    avg_light = sum(light_history) / len(light_history)

    # Move servo only if light change is significant
    if abs(light_value - avg_light) > ignore_window_width:
        target_pos = light_to_servo_pos(light_value, light_max)
        servo.angle = clamp(target_pos, 0, 180)

    # update t each step
    t = time.time() - start
    print(f"t={t:6.2f}, light={light_value:6.2f}, avg={avg_light:6.2f}, target_pos={target_pos:6.2f}")
    
    # sleep according to freq
    sleep(1 / freq)
