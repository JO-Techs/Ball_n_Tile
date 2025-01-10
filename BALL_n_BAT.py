import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Collector Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets (basket and ball)
basket_image = pygame.Surface((100, 20))
basket_image.fill(WHITE)

ball_image = pygame.Surface((20, 20))
pygame.draw.circle(ball_image, WHITE, (10, 10), 10)

# Game variables
basket_x = (width - 100) // 2
basket_y = height - 50
ball_x = random.randint(50, width - 50)
ball_y = 0
ball_speed = 5
score = 0
is_bouncing = False
bounce_count = 0
bounce_height = 20  # Bounce height
bounce_limit = 5  # Number of frames to bounce
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= 10  # Move basket left
    if keys[pygame.K_RIGHT] and basket_x < width - 100:
        basket_x += 10  # Move basket right

    # Move the ball
    if not is_bouncing:
        ball_y += ball_speed
        if ball_y > height:
            ball_y = 0
            ball_x = random.randint(50, width - 50)  # Reset ball position

    # Check for collision with basket
    if (basket_x < ball_x < basket_x + 100) and (basket_y < ball_y < basket_y + 20):
        if not is_bouncing:
            is_bouncing = True
            bounce_count = 0

    # Handle the bounce effect
    if is_bouncing:
        if bounce_count < bounce_limit:
            ball_y -= bounce_height  # Bounce up
            bounce_count += 1
        else:
            is_bouncing = False
            ball_y = 0  # Reset ball position after the bounce
            ball_x = random.randint(50, width - 50)  # New ball position
            score += 1  # Increase score

    # Fill the background
    screen.fill(BLACK)

    # Draw the basket and ball
    screen.blit(basket_image, (basket_x, basket_y))
    screen.blit(ball_image, (ball_x, ball_y))

    # Display score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
