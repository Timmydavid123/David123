import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the snake and food
snake_pos = [(width // 2, height // 2)]
snake_body = [(width // 2, height // 2), (width // 2 - 10, height // 2), (width // 2 - 20, height // 2)]
food_pos = (random.randint(0, width - 10) // 10 * 10, random.randint(0, height - 10) // 10 * 10)
food_spawned = True

# Set up the game clock
clock = pygame.time.Clock()

# Set up initial snake direction
direction = "RIGHT"
change_to = direction

# Set up game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update snake direction
    direction = change_to

    # Update snake position
    if direction == "UP":
        snake_pos = (snake_pos[0], snake_pos[1] - 10)
    elif direction == "DOWN":
        snake_pos = (snake_pos[0], snake_pos[1] + 10)
    elif direction == "LEFT":
        snake_pos = (snake_pos[0] - 10, snake_pos[1])
    elif direction == "RIGHT":
        snake_pos = (snake_pos[0] + 10, snake_pos[1])

    # Check for collision with food
    if snake_pos == food_pos:
        food_spawned = False
        snake_body.append((0, 0))

    # Move the snake
    snake_body.insert(0, snake_pos)
    if not food_spawned:
        food_pos = (random.randint(0, width - 10) // 10 * 10, random.randint(0, height - 10) // 10 * 10)
        food_spawned = True
    else:
        snake_body.pop()

    # Check for collision with the boundaries or itself
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height or snake_pos in snake_body[1:]:
        game_over = True

    # Draw the game window
    window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Refresh the game display
    pygame.display.flip()

    # Set the game speed
    clock.tick(15)

# Quit the game
pygame.quit()
