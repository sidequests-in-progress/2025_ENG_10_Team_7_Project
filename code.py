import time
import board
import digitalio
from adafruit_circuitplayground import cp
import pwmio
from adafruit_motor import servo

# Set up pin A1 as an output for the LED
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

pwm = pwmio.PWMOut(board.A2, duty_cycle=0, frequency=50)

my_servo = servo.Servo(pwm)
angle = 90  # start centered
my_servo.angle = angle

while True:
    if cp.button_a: # button a spins the motor clockwise
        angle -= 10
        if angle < 0:
            angle = 0
        my_servo.angle = angle
        time.sleep(0.2)

    if cp.button_b: # button b spins the motor counter clockwise
        angle += 10
        if angle > 180:
            angle = 180
        my_servo.angle = angle
        time.sleep(0.2)

