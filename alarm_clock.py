"""
Python Alarm Clock: A simple program that sets an alarm for a specified time,
plays an alarm sound when the time is reached, and allows the user to stop
the alarm by pressing the 's' key.
"""

import time
import datetime
import pygame
import keyboard


def set_alarm(alarm_time):
    """Set an alarm for the specified time and play a sound when time is reached."""
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm_clock.mp3"  # Define the path to the alarm sound file
    is_running = True  # Flag to control the main alarm loop

    # Loop to continuously check the current time
    while is_running:
        try:
            # Get the current time in HH:MM:SS format
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\rCurrent Time: {current_time}", end="")  # Print in-place to update time display

            # Check if current time matches the alarm time
            if current_time == alarm_time:
                print("\nWAKE UP! 😂 (Press 's' to stop the alarm)")

                # Initialize pygame mixer and play the alarm sound
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                # Loop to keep playing the alarm until stopped or 's' key is pressed
                while pygame.mixer.music.get_busy():
                    # Check if the user pressed 's' to stop the alarm
                    if keyboard.is_pressed('s'):
                        print("\nAlarm stopped by user.")
                        pygame.mixer.music.stop()  # Stop the alarm sound
                        break
                    time.sleep(0.5)  # Shorter sleep for more responsive key press checking

                is_running = False  # Exit main loop after alarm goes off or is stopped

            # Wait 1 second before checking the time again to avoid excessive CPU usage
            time.sleep(1)

        except pygame.error as e:
            # Handle potential errors from pygame (e.g., sound file issues)
            print(f"\nError with pygame or sound file: {e}")
            is_running = False  # Exit the loop if there's an error


def validate_time(input_time):
    """Validate if the input time is in HH:MM:SS format."""
    try:
        # Try parsing the time to confirm it's in the correct format
        datetime.datetime.strptime(input_time, "%H:%M:%S")
        return True
    except ValueError:
        # If parsing fails, inform the user of the correct format
        print("Invalid time format! Please use HH:MM:SS")
        return False


if __name__ == "__main__":
    # Prompt user to enter an alarm time
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")

    # Validate the entered time format and set the alarm if it's correct
    if validate_time(alarm_time):
        set_alarm(alarm_time)
