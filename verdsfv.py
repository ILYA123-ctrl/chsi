import tkinter as tk
import time
import math

class Clock(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.width = 400
        self.height = 400
        self.radius = 150
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.create_rectangle(10, 10, self.width - 10, self.height - 10, outline="black", width=2)
        self.update_clock()
        self.pack()

    def draw_clock_face(self):
        self.delete("all")
        self.create_rectangle(10, 10, self.width - 10, self.height - 10, outline="black", width=2)
        self.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                         self.center_x + self.radius, self.center_y + self.radius, outline="black", width=2)

        for i in range(12):
            angle = math.radians(i * 30)  # 30 degrees for each hour
            x = self.center_x + (self.radius - 20) * math.sin(angle)
            y = self.center_y - (self.radius - 20) * math.cos(angle)
            self.create_text(x, y, text=str(i + 1), font=("Arial", 12))

    def draw_hands(self, hour, minute, second):
        # Draw hour hand
        hour_angle = math.radians((hour % 12 + minute / 60) * 30)
        hour_x = self.center_x + (self.radius - 60) * math.sin(hour_angle)
        hour_y = self.center_y - (self.radius - 60) * math.cos(hour_angle)
        self.create_line(self.center_x, self.center_y, hour_x, hour_y, fill="black", width=6)

        # Draw minute hand
        minute_angle = math.radians((minute + second / 60) * 6)
        minute_x = self.center_x + (self.radius - 40) * math.sin(minute_angle)
        minute_y = self.center_y - (self.radius - 40) * math.cos(minute_angle)
        self.create_line(self.center_x, self.center_y, minute_x, minute_y, fill="blue", width=4)

        # Draw second hand
        second_angle = math.radians(second * 6)
        second_x = self.center_x + (self.radius - 30) * math.sin(second_angle)
        second_y = self.center_y - (self.radius - 30) * math.cos(second_angle)
        self.create_line(self.center_x, self.center_y, second_x, second_y, fill="red", width=2)

        # Draw date triangle at the end of the hour hand
        triangle_size = 10
        triangle_points = [
            hour_x, hour_y,
            hour_x - triangle_size, hour_y + triangle_size,
            hour_x + triangle_size, hour_y + triangle_size
        ]
        self.create_polygon(triangle_points, fill="black")

        # Draw diamond at the end of the minute hand
        diamond_size = 10
        diamond_points = [
            minute_x, minute_y,
            minute_x - diamond_size, minute_y + diamond_size,
            minute_x, minute_y + 2 * diamond_size,
            minute_x + diamond_size, minute_y + diamond_size
        ]
        self.create_polygon(diamond_points, fill="blue")

    def update_clock(self):
        self.draw_clock_face()
        current_time = time.localtime()
        self.draw_hands(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Круглые часы")
    clock = Clock(master=root, width=400, height=400)
    root.mainloop()