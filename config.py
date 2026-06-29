# config.py
# Configuration parameters for the robot

# Distance threshold for obstacle avoidance (cm)
OBSTACLE_THRESHOLD = 20.0

# Speed settings (PWM duty cycle 0-100)
MOTOR_SPEED = 25
TURN_SPEED = 25
BACKUP_SPEED = 20

# Timing durations (seconds)
TURN_DURATION = 0.5
BACKUP_DURATION = 0.2
LOOP_INTERVAL = 0.1
SONAR_TIMEOUT = 0.1

# Line following thresholds (for IR sensors, example values)
LINE_WHITE = 800   # ADC value for white surface
LINE_BLACK = 200   # ADC value for black line

# GPIO pin assignments
TRIG_PIN = 23
ECHO_PIN = 24
ENA_PIN = 12
IN1_PIN = 5
IN2_PIN = 6
ENB_PIN = 13
IN3_PIN = 20
IN4_PIN = 21

# Optional IR sensor pins (for line following)
# IR_LEFT = 17
# IR_CENTER = 27
# IR_RIGHT = 22
