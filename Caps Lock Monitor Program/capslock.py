import keyboard
import tkinter as tk

# Function to handle mouse dragging
def move_window(event):
    window.geometry(f"+{event.x_root}+{event.y_root}")

# Function to change color based on Caps Lock state
def change_color():
    global is_caps_lock_on, current_color

    caps_lock_state = keyboard.is_pressed('caps lock')
    
    if caps_lock_state and not is_caps_lock_on:
        current_color = "green" if current_color == "red" else "red"
        canvas.itemconfig(circle, fill=current_color)
        is_caps_lock_on = True
    elif not caps_lock_state and is_caps_lock_on:
        is_caps_lock_on = False
    
    window.after(100, change_color)

# Create the main window
window = tk.Tk()
window.overrideredirect(True)  # Removes window decorations
window.attributes('-transparentcolor', 'white')  # Set the transparent color
window.attributes('-topmost', True)  # Make the window always on top

# Function to handle mouse dragging
window.bind('<B1-Motion>', move_window)

is_caps_lock_on = False
current_color = "red"

# Create a canvas
canvas = tk.Canvas(window, width=100, height=100, bg='white', highlightthickness=0)
canvas.pack()

# Create a circular frame to give it a glassy feel
canvas.create_oval(5, 5, 95, 95, fill="lightgrey", outline="white", width=5)

# Create a circle on the canvas
circle = canvas.create_oval(10, 10, 90, 90, fill=current_color)

change_color()

window.mainloop()
