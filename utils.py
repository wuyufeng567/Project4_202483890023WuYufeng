# utils.py
# Utility functions

import time

def wait(seconds):
    time.sleep(seconds)

def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))
