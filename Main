# main.py
# Main program – select behavior mode

import sys
import time
from behaviors import Behavior

def print_menu():
    print("Robot Control Menu")
    print("1 - Obstacle Avoidance")
    print("2 - Object Following")
    print("3 - Line Following (requires IR sensors)")
    print("4 - Manual Turn Test")
    print("q - Quit")

def main():
    bot = Behavior()
    try:
        while True:
            print_menu()
            choice = input("Select mode: ").strip().lower()
            if choice == 'q':
                break
            elif choice == '1':
                print("Obstacle avoidance mode. Press Ctrl+C to stop.")
                try:
                    while True:
                        bot.avoid_obstacle()
                        time.sleep(LOOP_INTERVAL)
                except KeyboardInterrupt:
                    print("Exiting avoidance mode.")
            elif choice == '2':
                print("Object following mode. Press Ctrl+C to stop.")
                try:
                    while True:
                        bot.follow_object(target_distance=30.0)
                        time.sleep(LOOP_INTERVAL)
                except KeyboardInterrupt:
                    print("Exiting following mode.")
            elif choice == '3':
                print("Line following mode. Press Ctrl+C to stop.")
                try:
                    while True:
                        bot.line_follow()
                        time.sleep(LOOP_INTERVAL)
                except KeyboardInterrupt:
                    print("Exiting line following mode.")
            elif choice == '4':
                # Manual turn test
                print("Turning left for 1 second")
                bot.turn('left', 1.0)
                time.sleep(0.5)
                print("Turning right for 1 second")
                bot.turn('right', 1.0)
            else:
                print("Invalid choice.")
    finally:
        bot.cleanup()
        print("Program terminated.")

if __name__ == "__main__":
    main()
