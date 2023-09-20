import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Define the player's properties
player_width = 50
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 8

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame._LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Fill the screen with a background color
    screen.fill(WHITE)

    # Draw the player as a blue rectangle
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()




