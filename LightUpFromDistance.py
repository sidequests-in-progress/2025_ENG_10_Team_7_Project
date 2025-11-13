# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This is the "Hello, world!" of CircuitPython: Blinky! This example blinks the little red LED on
and off!"""

import time
import board
import digitalio
import pulseio

# Ultrasonic sensor setup
trig = digitalio.DigitalInOut(board.A1)
trig.direction = digitalio.Direction.OUTPUT
echo = pulseio.PulseIn(board.A2)
echo.pause()
echo.clear()

# LED setup
led_green = digitalio.DigitalInOut(board.A3)
led_yellow = digitalio.DigitalInOut(board.A4)
led_red = digitalio.DigitalInOut(board.A5)

for led in [led_green, led_yellow, led_red]:
    led.direction = digitalio.Direction.OUTPUT
    led.value = False

def get_distance():
    # Send trigger pulse
    trig.value = True
    time.sleep(0.00001)  # 10 µs pulse
    trig.value = False

    # Measure echo pulse
    echo.clear()
    echo.resume()
    time.sleep(0.05)
    echo.pause()

    if len(echo) == 0:
        return None

    pulse_time = echo[0] / 1_000_000  
    distance = pulse_time * 343 / 2 * 100  
    return distance

while True:
    distance = get_distance()

    if distance is None:
        for led in [led_green, led_yellow, led_red]:
            led.value = False
    else:

        # Reset LEDs
        led_green.value = led_yellow.value = led_red.value = False

        # Distance thresholds (adjust as needed)
        if distance > 50:
            led_green.value = True  # Safe distance
        elif 20 < distance <= 50:
            led_yellow.value = True  # Warning zone
        else:
            led_red.value = True  # Danger zone

    time.sleep(0.5)
 
# Write your code here :-)
