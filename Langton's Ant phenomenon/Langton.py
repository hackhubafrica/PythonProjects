import tkinter as tk
import time

class LangtonsAnt:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
        self.ant_pos = (width // 2, height // 2)  # Starting position at the center
        self.direction = 'up'  # Initial direction

    def turn_right(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        else:
            self.direction = 'up'

    def turn_left(self):
        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'right':
            self.direction = 'up'
        elif self.direction == 'down':
            self.direction = 'right'
        else:
            self.direction = 'down'

    def move_forward(self):
        x, y = self.ant_pos
        if self.direction == 'up':
            self.ant_pos = (x, (y - 1) % self.height)
        elif self.direction == 'right':
            self.ant_pos = ((x + 1) % self.width, y)
        elif self.direction == 'down':
            self.ant_pos = (x, (y + 1) % self.height)
        else:
            self.ant_pos = ((x - 1) % self.width, y)

    def update_grid(self):
        x, y = self.ant_pos
        if self.grid[y][x] == 0:  # White cell
            self.turn_right()
            self.grid[y][x] = 1  # Change cell color to black
        else:  # Black cell
            self.turn_left()
            self.grid[y][x] = 0  # Change cell color to white
        self.move_forward()

    def display_grid(self, canvas):
        cell_size = 10
        canvas.delete("all")
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = "black" if cell == 1 else "white"
                canvas.create_rectangle(x * cell_size, y * cell_size,
                                        (x + 1) * cell_size, (y + 1) * cell_size,
                                        fill=color)


def main():
    width = 50
    height = 30

    root = tk.Tk()
    root.title("Langton's Ant Simulation")
    canvas = tk.Canvas(root, width=width * 10, height=height * 10, bg='white')
    canvas.pack()

    ant = LangtonsAnt(width, height)

    while True:
        ant.update_grid()
        ant.display_grid(canvas)
        root.update_idletasks()
        root.update()
        time.sleep(0.1)  # Delay for visualization

    root.mainloop()


if __name__ == "__main__":
    main()
