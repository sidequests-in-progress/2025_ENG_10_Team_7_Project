import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp


# Servo 1 setup
pwm1 = pwmio.PWMOut(board.A1, duty_cycle=0, frequency=50)
servo1 = servo.Servo(pwm1)
angle1 = 90
servo1.angle = angle1

# Servo 2 setup
pwm2 = pwmio.PWMOut(board.A2, duty_cycle=0, frequency=50)
servo2 = servo.Servo(pwm2)
angle2 = 90
servo2.angle = angle2

dir1 = 1     # Servo 1 direction (+1 or -1)
dir2 = 1     # Servo 2 direction (+1 or -1)

# Previous button state for new button direction
lastA = False
lastB = False

while True:

# Button A controls servo 1
    if cp.button_a:
        if not lastA:       # New press flips direction
            dir1 *= -1

        # Move servo while held
        angle1 += dir1 * 3      # Step size
        angle1 = max(0, min(180, angle1))
        servo1.angle = angle1

    lastA = cp.button_a  # Update last state

# Button A controls servo 2
    if cp.button_b:
        if not lastB:       # New press flips direction
            dir2 *= -1

        # Move servo while held
        angle2 += dir2 * 3
        angle2 = max(0, min(180, angle2))
        servo2.angle = angle2

    lastB = cp.button_b  # Update last state


    time.sleep(0.03)   # Adjust for speed
