import tkinter as tk
from tkinter import Canvas
from datetime import datetime
import math
import time
import winsound

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog and Digital Clock")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        
        # To Change Sound State
        self.sound_on = True

        # Create a canvas for the analog clock
        self.canvas = Canvas(self.root, width=400, height=400, bg="#FDF6E3", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Digital clock label
        self.digital_label = tk.Label(
            self.root, text="", font=("Helvetica", 24, "bold"), fg="#5A5A5A", bg="#FDF6E3"
        )
        self.digital_label.pack(pady=10)

        # Mute/Unmute Button
        self.sound_button = tk.Button(
            self.root, text="Mute Sound", font=("Helvetica", 12), bg="red", command=self.toggle_sound
        )
        self.sound_button.pack(pady=10)

        # Initialize tick-tock state
        self.tick = True

        # Updating the clocks
        self.update_clock()

    def draw_analog_clock(self, hours, minutes, seconds):
        self.canvas.delete("all")

        # Draw the clock face
        self.canvas.create_oval(50, 50, 350, 350, outline="#B4CDED", width=4, fill="#FFFBF2")
        self.canvas.create_text(200, 70, text="12", font=("Helvetica", 14, "bold"), fill="#5A5A5A")
        self.canvas.create_text(200, 330, text="6", font=("Helvetica", 14, "bold"), fill="#5A5A5A")
        self.canvas.create_text(330, 200, text="3", font=("Helvetica", 14, "bold"), fill="#5A5A5A")
        self.canvas.create_text(70, 200, text="9", font=("Helvetica", 14, "bold"), fill="#5A5A5A")

        # Clock center
        center_x, center_y = 200, 200

        # Calculate hand lengths
        second_hand_length = 140
        minute_hand_length = 110
        hour_hand_length = 80

        # Calculate angles
        second_angle = math.radians((seconds / 60) * 360 - 90)
        minute_angle = math.radians((minutes / 60) * 360 - 90)
        hour_angle = math.radians((hours % 12 + minutes / 60) * 30 - 90)

        # Clock hands
        self.canvas.create_line(
            center_x, center_y,
            center_x + second_hand_length * math.cos(second_angle),
            center_y + second_hand_length * math.sin(second_angle),
            fill="#FF6F61", width=2
        )
        self.canvas.create_line(
            center_x, center_y,
            center_x + minute_hand_length * math.cos(minute_angle),
            center_y + minute_hand_length * math.sin(minute_angle),
            fill="#7FC97F", width=4
        )
        self.canvas.create_line(
            center_x, center_y,
            center_x + hour_hand_length * math.cos(hour_angle),
            center_y + hour_hand_length * math.sin(hour_angle),
            fill="#6699CC", width=6
        )

        # Clock center point
        self.canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="#5A5A5A")

    def play_tick_tock(self):
        if self.sound_on:
            if self.tick:
                winsound.Beep(800, 100)  # Tick sound
            else:
                winsound.Beep(600, 100)  # Tock sound
            self.tick = not self.tick

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        self.sound_button.config(text="Unmute Sound" if not self.sound_on else "Mute Sound")

    def update_clock(self):
        # Get the current time
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second

        # Update the digital clock
        current_time = now.strftime("%H:%M:%S")
        self.digital_label.config(text=f"Digital Clock: {current_time}")

        # Update the analog clock
        self.draw_analog_clock(hours, minutes, seconds)

        # Play tick-tock sound
        self.play_tick_tock()

        # Schedule the next update
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()