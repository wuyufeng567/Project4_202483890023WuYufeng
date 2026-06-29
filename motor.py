# motor.py
# Motor control using L298N driver and PWM

import RPi.GPIO as GPIO
from config import *

class MotorController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(IN1_PIN, GPIO.OUT)
        GPIO.setup(IN2_PIN, GPIO.OUT)
        GPIO.setup(IN3_PIN, GPIO.OUT)
        GPIO.setup(IN4_PIN, GPIO.OUT)
        GPIO.setup(ENA_PIN, GPIO.OUT)
        GPIO.setup(ENB_PIN, GPIO.OUT)
        self.pwm_left = GPIO.PWM(ENA_PIN, 1000)
        self.pwm_right = GPIO.PWM(ENB_PIN, 1000)
        self.pwm_left.start(0)
        self.pwm_right.start(0)
        self.speed = MOTOR_SPEED

    def set_speed(self, speed):
        self.speed = max(0, min(100, speed))

    def forward(self, speed=None):
        s = speed if speed is not None else self.speed
        GPIO.output(IN1_PIN, GPIO.HIGH)
        GPIO.output(IN2_PIN, GPIO.LOW)
        GPIO.output(IN3_PIN, GPIO.HIGH)
        GPIO.output(IN4_PIN, GPIO.LOW)
        self.pwm_left.ChangeDutyCycle(s)
        self.pwm_right.ChangeDutyCycle(s)

    def backward(self, speed=None):
        s = speed if speed is not None else self.speed
        GPIO.output(IN1_PIN, GPIO.LOW)
        GPIO.output(IN2_PIN, GPIO.HIGH)
        GPIO.output(IN3_PIN, GPIO.LOW)
        GPIO.output(IN4_PIN, GPIO.HIGH)
        self.pwm_left.ChangeDutyCycle(s)
        self.pwm_right.ChangeDutyCycle(s)

    def turn_left(self, speed=None):
        s = speed if speed is not None else self.speed
        GPIO.output(IN1_PIN, GPIO.LOW)
        GPIO.output(IN2_PIN, GPIO.HIGH)
        GPIO.output(IN3_PIN, GPIO.HIGH)
        GPIO.output(IN4_PIN, GPIO.LOW)
        self.pwm_left.ChangeDutyCycle(s)
        self.pwm_right.ChangeDutyCycle(s)

    def turn_right(self, speed=None):
        s = speed if speed is not None else self.speed
        GPIO.output(IN1_PIN, GPIO.HIGH)
        GPIO.output(IN2_PIN, GPIO.LOW)
        GPIO.output(IN3_PIN, GPIO.LOW)
        GPIO.output(IN4_PIN, GPIO.HIGH)
        self.pwm_left.ChangeDutyCycle(s)
        self.pwm_right.ChangeDutyCycle(s)

    def stop(self):
        GPIO.output(IN1_PIN, GPIO.LOW)
        GPIO.output(IN2_PIN, GPIO.LOW)
        GPIO.output(IN3_PIN, GPIO.LOW)
        GPIO.output(IN4_PIN, GPIO.LOW)
        self.pwm_left.ChangeDutyCycle(0)
        self.pwm_right.ChangeDutyCycle(0)

    def cleanup(self):
        self.stop()
        self.pwm_left.stop()
        self.pwm_right.stop()
        GPIO.cleanup()
