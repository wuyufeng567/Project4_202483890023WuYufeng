# ultrasonic.py
# HC-SR04 ultrasonic distance measurement

import RPi.GPIO as GPIO
import time
from config import SONAR_TIMEOUT

class UltrasonicSensor:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def get_distance(self):
        # Send trigger pulse
        GPIO.output(self.trig, False)
        time.sleep(0.000002)
        GPIO.output(self.trig, True)
        time.sleep(0.000010)
        GPIO.output(self.trig, False)

        # Wait for echo start
        start_time = time.time()
        while GPIO.input(self.echo) == 0:
            if time.time() - start_time > SONAR_TIMEOUT:
                return 999.0
        pulse_start = time.time()

        # Wait for echo end
        while GPIO.input(self.echo) == 1:
            if time.time() - start_time > SONAR_TIMEOUT:
                return 999.0
        pulse_end = time.time()

        duration = pulse_end - pulse_start
        distance = duration * 34300 / 2.0  # speed of sound in cm/s
        return distance
