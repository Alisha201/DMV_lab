import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

radius = float(input("Enter radius of the circle: "))
x_pos = float(input("Enter initial X position: "))
y_pos = float(input("Enter initial Y position: "))

fig, ax = plt.subplots()

circle = plt.Circle((x_pos, y_pos), radius, color='blue')
ax.add_patch(circle)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

step = 0.5

def on_key(event):
    global x_pos, y_pos
    
    if event.key == 'up':
        y_pos += step
    elif event.key == 'down':
        y_pos -= step
    elif event.key == 'left':
        x_pos -= step
    elif event.key == 'right':
        x_pos += step
    
    circle.center = (x_pos, y_pos)
    fig.canvas.draw()


def animate(frame):
    return circle,

fig.canvas.mpl_connect('key_press_event', on_key)

ani = FuncAnimation(fig, animate, interval=50)

plt.title("Animated Circle with Keyboard Control")
plt.show()