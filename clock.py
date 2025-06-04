import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Realistic Analog Clock")
        self.canvas_size = 400
        self.center = self.canvas_size // 2
        self.radius = self.center - 20

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white', highlightthickness=0)
        self.canvas.pack()

        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        # Draw subtle gradient background using concentric circles
        for i in range(20):
            color_val = 255 - i*6
            color = f'#{color_val:02x}{color_val:02x}{color_val:02x}'
            self.canvas.create_oval(10+i, 10+i, self.canvas_size-10-i, self.canvas_size-10-i, fill=color, outline=color)

        # Outer blue circle - thicker with slight shadow
        self.canvas.create_oval(10, 10, self.canvas_size-10, self.canvas_size-10, width=6, outline='blue')

        # Minute marks (smaller, thinner)
        for i in range(60):
            angle = math.pi/30 * i
            outer = self.radius
            inner = outer - 8 if i % 5 == 0 else outer - 4
            x_start = self.center + inner * math.sin(angle)
            y_start = self.center - inner * math.cos(angle)
            x_end = self.center + outer * math.sin(angle)
            y_end = self.center - outer * math.cos(angle)
            width = 3 if i % 5 == 0 else 1
            color = 'blue' if i % 5 == 0 else '#336699'
            self.canvas.create_line(x_start, y_start, x_end, y_end, width=width, fill=color)

        # Hour pins (thicker, rounded ends)
        for i in range(12):
            angle = math.pi/6 * i
            x_start = self.center + (self.radius - 25) * math.sin(angle)
            y_start = self.center - (self.radius - 25) * math.cos(angle)
            x_end = self.center + self.radius * math.sin(angle)
            y_end = self.center - self.radius * math.cos(angle)
            self.canvas.create_line(x_start, y_start, x_end, y_end, width=6, fill='blue', capstyle=tk.ROUND)

        # Hour numbers (serif font, blue)
        for i in range(1, 13):
            angle = math.pi/6 * (i - 3)  # shift so 12 is top
            x_text = self.center + (self.radius - 60) * math.cos(angle)
            y_text = self.center + (self.radius - 60) * math.sin(angle)
            self.canvas.create_text(x_text, y_text, text=str(i), font=("Times New Roman", 20, "bold"), fill='blue')

        # Glass shine effect: a white translucent arc
        self.canvas.create_arc(20, 20, self.canvas_size-20, self.canvas_size-20,
                               start=60, extent=120, style='arc', outline='white', width=12)

    def update_clock(self):
        self.canvas.delete("hands")

        # Current time
        t = time.localtime()
        sec = t.tm_sec
        minute = t.tm_min
        hour = t.tm_hour % 12

        # Calculate angles
        sec_angle = math.pi/30 * sec
        min_angle = math.pi/30 * minute + sec_angle / 60
        hour_angle = math.pi/6 * hour + min_angle / 12

        # Second hand (thin, red)
        sec_length = self.radius - 35
        x_sec = self.center + sec_length * math.sin(sec_angle)
        y_sec = self.center - sec_length * math.cos(sec_angle)
        self.canvas.create_line(self.center, self.center, x_sec, y_sec, fill='red', width=1, tag="hands")

        # Minute hand (sleek tapered)
        min_length = self.radius - 60
        x_min = self.center + min_length * math.sin(min_angle)
        y_min = self.center - min_length * math.cos(min_angle)
        self.canvas.create_line(self.center, self.center, x_min, y_min, fill='black', width=5, capstyle=tk.ROUND, tag="hands")

        # Hour hand (shorter, thicker, tapered)
        hour_length = self.radius - 90
        x_hour = self.center + hour_length * math.sin(hour_angle)
        y_hour = self.center - hour_length * math.cos(hour_angle)
        self.canvas.create_line(self.center, self.center, x_hour, y_hour, fill='black', width=8, capstyle=tk.ROUND, tag="hands")

        # Center dot with subtle shadow (blue)
        self.canvas.create_oval(self.center-10, self.center-10, self.center+10, self.center+10, fill='blue', outline='lightblue', width=2, tag="hands")

        # Update every second
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
