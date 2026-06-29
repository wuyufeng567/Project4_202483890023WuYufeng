# behaviors.py
# Robot behaviors: obstacle avoidance, line following, following

import time
import random
from motor import MotorController
from ultrasonic import UltrasonicSensor
from line_sensor import LineSensor
from config import *

class Behavior:
    def __init__(self):
        self.motor = MotorController()
        self.sonar = UltrasonicSensor(TRIG_PIN, ECHO_PIN)
        # Optional line sensors (uncomment if available)
        # self.line = LineSensor(IR_LEFT, IR_CENTER, IR_RIGHT)

    def avoid_obstacle(self):
        """Obstacle avoidance behavior with random turn"""
        dist = self.sonar.get_distance()
        print(f"Distance: {dist:.1f} cm")
        if dist < OBSTACLE_THRESHOLD:
            self.motor.stop()
            time.sleep(0.05)
            # Back up
            self.motor.backward(BACKUP_SPEED)
            time.sleep(BACKUP_DURATION)
            self.motor.stop()
            time.sleep(0.05)
            # Random turn
            if random.choice([True, False]):
                self.motor.turn_left(TURN_SPEED)
            else:
                self.motor.turn_right(TURN_SPEED)
            time.sleep(TURN_DURATION)
            self.motor.stop()
            time.sleep(0.05)
            return True  # obstacle handled
        else:
            self.motor.forward()
            return False

    def follow_object(self, target_distance=30.0, kp=0.8):
        """
        Follow an object maintaining a target distance.
        Uses a simple proportional controller.
        """
        dist = self.sonar.get_distance()
        error = target_distance - dist
        speed = max(0, min(100, int(kp * error)))  # limit 0-100
        print(f"Distance: {dist:.1f}, Speed: {speed}")
        if dist < target_distance - 5:
            # Too close – stop or reverse
            self.motor.stop()
        elif dist > target_distance + 5:
            # Too far – move forward
            self.motor.forward(speed)
        else:
            # Within dead zone – maintain position
            self.motor.stop()

    def line_follow(self):
        """
        Line following using three IR sensors.
        Requires actual sensors; this is a stub implementation.
        """
        # left, center, right = self.line.read()
        # For demonstration, use dummy values (no line)
        left = center = right = False
        if center:
            self.motor.forward()
        elif left:
            self.motor.turn_left()
        elif right:
            self.motor.turn_right()
        else:
            # Lost line – stop or search
            self.motor.stop()

    def turn(self, direction, duration=None):
        """Turn left or right for a given duration."""
        dur = duration if duration is not None else TURN_DURATION
        if direction == 'left':
            self.motor.turn_left()
        elif direction == 'right':
            self.motor.turn_right()
        else:
            return
        time.sleep(dur)
        self.motor.stop()

    def cleanup(self):
        self.motor.cleanup()
