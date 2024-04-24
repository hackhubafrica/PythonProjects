import pygame
import random

# Initialize Pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the snake and food coordinates
snake_coords = [(160, 240), (170, 240), (180, 240)]
food_coord = (random.randint(0, 63) * 10, random.randint(0, 47) * 10)  # Ensuring food coordinates are multiples of 10

# Direction and growth flags
direction = 'RIGHT'
grow_snake = False

# Game state variables
level = 1
score = 0
obstacles = []

# Create initial obstacles
def create_obstacles():
    global obstacles
    # Clear existing obstacles
    obstacles.clear()
    # Create obstacles based on the current level
    if level >= 2:
        # Example: create two obstacles for level 2 and higher
        obstacles.append((100, 100))
        obstacles.append((200, 300))
    # Add more obstacles for higher levels as desired
    if level >= 3:
        obstacles.append((300, 200))
        obstacles.append((400, 350))

# Function to move the snake based on the current direction
def move_snake():
    global snake_coords, direction, grow_snake
    
    head = snake_coords[-1]
    x, y = head

    # Move snake based on direction
    if direction == 'RIGHT':
        new_head = (x + 10, y)
    elif direction == 'LEFT':
        new_head = (x - 10, y)
    elif direction == 'UP':
        new_head = (x, y - 10)
    elif direction == 'DOWN':
        new_head = (x, y + 10)

    # Add the new head to the snake
    snake_coords.append(new_head)

    # If the snake did not eat food, remove the tail
    if not grow_snake:
        snake_coords.pop(0)
    else:
        grow_snake = False

# Function to check if the snake has collided with the food
def check_food():
    global food_coord, grow_snake, score
    
    # Get the snake's head
    head = snake_coords[-1]

    # Check if the snake's head is at the food position
    if head == food_coord:
        print("Snake ate the food!")
        grow_snake = True
        score += 10

        # Generate a new food position avoiding the snake and obstacles
        while True:
            food_coord = (random.randint(0, 63) * 10, random.randint(0, 47) * 10)
            if food_coord not in snake_coords and food_coord not in obstacles:
                break

# Function to check for game over conditions
def check_game_over():
    head = snake_coords[-1]

    # Check for collision with the snake's body
    if head in snake_coords[:-1]:
        print("Game Over! The snake collided with itself.")
        return True

    # Check for collision with obstacles
    if head in obstacles:
        print("Game Over! The snake collided with an obstacle.")
        return True

    # Check for collision with the screen boundaries
    x, y = head
    if x < 0 or x >= 640 or y < 0 or y >= 480:
        print("Game Over! The snake collided with the boundary.")
        return True
    
    return False

# Function to draw the snake, food, and obstacles
def draw_game():
    screen.fill(BLACK)
    
    # Draw the snake
    for coord in snake_coords:
        pygame.draw.rect(screen, GREEN, (coord[0], coord[1], 10, 10))
    
    # Draw the food
    pygame.draw.rect(screen, RED, (food_coord[0], food_coord[1], 10, 10))
    
    # Draw the obstacles
    for coord in obstacles:
        pygame.draw.rect(screen, BLUE, (coord[0], coord[1], 10, 10))

# Main game loop
running = True

# Initialize obstacles
create_obstacles()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change snake direction based on arrow keys
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    # Update the game state
    move_snake()
    check_food()
    
    # Check game over conditions
    if check_game_over():
        running = False
    
    # Draw the game objects
    draw_game()
    
    # Update the display
    pygame.display.update()
    
    # Control the frame rate (15 FPS)
    clock.tick(15)

# Quit Pygame
pygame.quit()
