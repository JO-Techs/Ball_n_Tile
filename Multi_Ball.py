import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball and paddle properties
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

player1_x, player1_y = WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30
player2_x, player2_y = WIDTH // 2 - PADDLE_WIDTH // 2, 20

player1_score, player2_score = 0, 0

clock = pygame.time.Clock()
running = True
game_time = 30  # in seconds
timer = pygame.time.get_ticks()

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= BALL_RADIUS or ball_x >= WIDTH - BALL_RADIUS:
        ball_dx *= -1

    if ball_y <= BALL_RADIUS:
        ball_dy *= -1
        player1_score += 1

    if ball_y >= HEIGHT - BALL_RADIUS:
        ball_dy *= -1
        player2_score += 1

    # Paddle collision
    if (player1_y <= ball_y + BALL_RADIUS <= player1_y + PADDLE_HEIGHT and
            player1_x <= ball_x <= player1_x + PADDLE_WIDTH):
        ball_dy *= -1

    if (player2_y <= ball_y - BALL_RADIUS <= player2_y + PADDLE_HEIGHT and
            player2_x <= ball_x <= player2_x + PADDLE_WIDTH):
        ball_dy *= -1

    # Check for ball falling off
    if ball_y > HEIGHT:
        winner = "Player 2 Wins!"
        running = False

    if ball_y < 0:
        winner = "Player 1 Wins!"
        running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1_x > 0:
        player1_x -= 6
    if keys[pygame.K_d] and player1_x < WIDTH - PADDLE_WIDTH:
        player1_x += 6
    if keys[pygame.K_LEFT] and player2_x > 0:
        player2_x -= 6
    if keys[pygame.K_RIGHT] and player2_x < WIDTH - PADDLE_WIDTH:
        player2_x += 6

    # Draw ball and paddles
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.rect(screen, RED, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, BLUE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Display scores
    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    screen.blit(player1_text, (10, HEIGHT - 40))
    screen.blit(player2_text, (10, 10))

    # Timer
    elapsed_time = (pygame.time.get_ticks() - timer) // 1000
    time_left = max(0, game_time - elapsed_time)
    timer_text = font.render(f"Time Left: {time_left}s", True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))

    if time_left <= 0:
        if player1_score > player2_score:
            winner = "Player 1 Wins!"
        elif player2_score > player1_score:
            winner = "Player 2 Wins!"
        else:
            winner = "It's a Draw!"
        running = False

    pygame.display.flip()
    clock.tick(60)

# End game message
screen.fill(BLACK)
end_text = font.render(winner, True, WHITE)
screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
