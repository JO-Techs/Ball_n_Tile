import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nokia Cricket Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Bat properties
bat_width, bat_height = 100, 15
bat_x = WIDTH // 2 - bat_width // 2
bat_y = HEIGHT - 40
bat_speed = 10

# Ball properties
ball = {
    "x": random.randint(20, WIDTH - 20),
    "y": 20,
    "speed_x": 0,  # No horizontal speed initially
    "speed_y": random.randint(4, 6),
    "bounced": False,
    "is_spin": random.choice([True, False])  # Randomly decide if it's a spin ball
}

# Score and retries
score = 0
retries = 3  # Number of retries allowed
level = 1
level_threshold = 5  # Points needed to level up

# Clock for FPS
clock = pygame.time.Clock()

# Font for score and messages
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
ball_active = True
game_over = False

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Bat movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bat_x > 0:
            bat_x -= bat_speed
        if keys[pygame.K_RIGHT] and bat_x < WIDTH - bat_width:
            bat_x += bat_speed

        # Ball logic
        if ball_active:
            ball["y"] += ball["speed_y"]
            ball["x"] += ball["speed_x"]

            # Bounce logic
            if not ball["bounced"] and ball["y"] >= HEIGHT // 2 + random.randint(20, 50):
                ball["bounced"] = True
                ball["speed_y"] = abs(ball["speed_y"])  # Ensure downward speed
                ball["speed_x"] = random.choice([-2, 2]) if ball["is_spin"] else 0

            # Gravity effect after bounce
            if ball["bounced"]:
                ball["speed_y"] += 0.2  # Simulate gravity

            # Check if bat hits the ball
            if bat_y < ball["y"] + 10 < bat_y + bat_height and bat_x < ball["x"] < bat_x + bat_width:
                ball_active = False
                score += 1

                # Level up logic
                if score % level_threshold == 0:
                    level += 1

                # Reset the ball
                ball["x"] = random.randint(20, WIDTH - 20)
                ball["y"] = 20
                ball["speed_x"] = 0
                ball["speed_y"] = random.randint(4, 6)
                ball["bounced"] = False
                ball["is_spin"] = random.choice([True, False])
                ball_active = True

            # Check if ball missed
            if ball["y"] > HEIGHT:
                retries -= 1
                ball_active = False

                # Check for game over
                if retries <= 0:
                    game_over = True
                else:
                    # Reset the ball
                    ball["x"] = random.randint(20, WIDTH - 20)
                    ball["y"] = 20
                    ball["speed_x"] = 0
                    ball["speed_y"] = random.randint(4, 6)
                    ball["bounced"] = False
                    ball["is_spin"] = random.choice([True, False])
                    ball_active = True

        # Draw the ball
        ball_color = BLUE if ball["is_spin"] else RED
        pygame.draw.circle(screen, ball_color, (int(ball["x"]), int(ball["y"])), 10)

        # Draw the bat
        pygame.draw.rect(screen, GREEN, (bat_x, bat_y, bat_width, bat_height))

        # Display score, level, and retries
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        retries_text = font.render(f"Retries: {retries}", True, BLACK)
        # Adjust positions to display on different lines
        screen.blit(score_text, (10, 10))          # Score at the top
        screen.blit(level_text, (10, 50))          # Level below score
        screen.blit(retries_text, (10, 90))        # Retries below level

    else:
        # Game over screen
        game_over_text = font.render("Game Over!", True, RED)
        final_score_text = font.render(f"Your Score: {score}", True, BLACK)
        retry_text = font.render("Press R to Try Again", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))
        screen.blit(retry_text, (WIDTH // 2 - 130, HEIGHT // 2 + 40))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game variables
            score = 0
            retries = 3
            level = 1
            ball["x"] = random.randint(20, WIDTH - 20)
            ball["y"] = 20
            ball["speed_x"] = 0
            ball["speed_y"] = random.randint(4, 6)
            ball["bounced"] = False
            ball["is_spin"] = random.choice([True, False])
            ball_active = True
            game_over = False

    # Update display
    pygame.display.flip()

    # Control FPS
    clock.tick(30)

pygame.quit()
