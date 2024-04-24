import turtle
import random

# Global variables
snake_coords = [(0, 0), (20, 0), (40, 0)]  # Initial snake body coordinates
food_coord = (random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)  # Initial food position
direction = "Right"  # Initial direction of the snake
ate_food = False  # Whether the snake has eaten the food

# Function to change the snake's direction
def change_direction(new_direction):
    global direction
    # Prevent reversing the snake's direction
    if new_direction == "Up" and direction != "Down":
        direction = new_direction
    elif new_direction == "Down" and direction != "Up":
        direction = new_direction
    elif new_direction == "Left" and direction != "Right":
        direction = new_direction
    elif new_direction == "Right" and direction != "Left":
        direction = new_direction

# Function to move the snake forward one step
def move_snake():
    global snake_coords, direction, ate_food
    head = snake_coords[-1]
    new_head = None
    
    # Determine the new head position based on the direction
    if direction == "Right":
        new_head = (head[0] + 20, head[1])
    elif direction == "Left":
        new_head = (head[0] - 20, head[1])
    elif direction == "Up":
        new_head = (head[0], head[1] + 20)
    elif direction == "Down":
        new_head = (head[0], head[1] - 20)
    
    # Check for collision with boundaries
    if (new_head[0] < -300 or new_head[0] > 300 or new_head[1] < -300 or new_head[1] > 300):
        game_over()
        return

    # Check for collision with the snake itself
    if new_head in snake_coords:
        game_over()
        return
    
    # Add the new head to the snake
    snake_coords.append(new_head)
    
    # If the snake did not eat the food, remove the tail
    if not ate_food:
        snake_coords.pop(0)
    else:
        # Reset the ate_food flag after growing the snake
        ate_food = False

# Function to check if the snake has collided with the food
def check_food():
    global food_coord, ate_food
    head = snake_coords[-1]
    
    # If the snake's head is at the food position, the snake ate the food
    if head == food_coord:
        print("Snake ate the food!")
        # The snake has eaten the food
        ate_food = True
        # Generate new food position
        food_coord = (random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
        # Update the food turtle's position
        food.goto(food_coord[0], food_coord[1])
    else:
        ate_food = False

# Function to draw the snake and food
def draw_game():
    # Clear snake's stamps, but do not clear the food stamps
    snake.clearstamps()
    
    # Draw the snake
    for coord in snake_coords:
        snake.goto(coord[0], coord[1])
        snake.stamp()
    
    # Update the food turtle's position without clearing
    food.goto(food_coord[0], food_coord[1])

# Function to update the game state
def update():
    # Disable automatic screen updates
    screen.tracer(0)
    
    move_snake()
    check_food()
    draw_game()
    
    # Manually update the screen to reduce blinking
    screen.update()
    
    # Schedule the next update after 100ms
    screen.ontimer(update, 100)

# Function to handle game over conditions
def game_over():
    print("Game Over!")
    screen.bye()

# Setup turtle screen and turtles
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create snake turtle
snake = turtle.Turtle()
snake.color("white")
snake.shape("square")
snake.penup()  # Avoid drawing lines

# Create food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()  # Avoid drawing lines
food.goto(food_coord[0], food_coord[1])

# Event bindings for changing direction
screen.onkey(lambda: change_direction("Up"), "Up")
screen.onkey(lambda: change_direction("Down"), "Down")
screen.onkey(lambda: change_direction("Left"), "Left")
screen.onkey(lambda: change_direction("Right"), "Right")
screen.listen()

# Initialize the game and start the update loop
update()

# Start the game loop
screen.mainloop()
