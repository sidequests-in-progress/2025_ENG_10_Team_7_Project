
# Import Section
import board
import digitalio
import time
from time import sleep
import adafruit_motor.servo as servo
import pwmio

# Setup section for servo
pwm = pwmio.PWMOut(board.A2, duty_cycle=0, frequency=50)
servo = servo.Servo(pwm)

# Setup Section for led
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

# Loop Section
while True:
    # Led check(optional)
    led.value = True
    sleep(0.5)
    led.value = False
    sleep(0.5)

    # ***You can only have 1 of the tests active in
    # the code at a time***
    # Remove the '#' to activate the code
    # Servo sweep test -

    for i in range(180):
        servo.angle = i
        time.sleep(0.01)
    print("Sweep from 180 to 0")
    for i in range(180):
        servo.angle = 180 - i
        time.sleep(0.01)

    # ***You can only have 1 of the tests active in
    # the code at a time***
    # Remove the '#' to activate the code
    # Servo angle selection test (only accepts numbers) -

#    degree = int(input('Input angle(0-180): ')) # variable for angle selection
#    servo.angle = degree # changes angle depending on input in the serial(terminal)

