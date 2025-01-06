import pygame
import sys
import time
def main():
    pygame.init()
    WIDTH, HEIGHT = 1000, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DEEP_BLUE = (30, 30, 100)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paddle Ball Game")
    clock = pygame.time.Clock()
    FPS = 60
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 20
    PADDLE_RADIUS = 10
    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    paddle_y = HEIGHT - 50
    paddle_speed = 10
    BALL_RADIUS = 6
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = 0
    ball_speed_y = 0
    initial_speed_x = 2
    initial_speed_y = 2
    speed_increment = 0.005
    WALL_THICKNESS = 10
    score = 0
    font = pygame.font.Font(None, 36)
    running = True
    ball_moving = False
    pygame.draw.rect(screen, DEEP_BLUE, (0, 0, WALL_THICKNESS, HEIGHT))  
    pygame.draw.rect(screen, DEEP_BLUE, (WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT))  
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT), border_radius=PADDLE_RADIUS)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > WALL_THICKNESS:
            paddle_x -= paddle_speed
            if not ball_moving:
                ball_speed_x = initial_speed_x
                ball_speed_y = initial_speed_y
                ball_moving = True
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - WALL_THICKNESS - PADDLE_WIDTH:
            paddle_x += paddle_speed
            if not ball_moving:
                ball_speed_x = initial_speed_x
                ball_speed_y = initial_speed_y
                ball_moving = True
        if ball_moving:
            ball_x += ball_speed_x
            ball_y += ball_speed_y
            ball_speed_x += speed_increment if ball_speed_x > 0 else -speed_increment
            ball_speed_y += speed_increment if ball_speed_y > 0 else -speed_increment
        if ball_x - BALL_RADIUS <= WALL_THICKNESS or ball_x + BALL_RADIUS >= WIDTH - WALL_THICKNESS:
            ball_speed_x = -ball_speed_x
        if ball_y - BALL_RADIUS <= 0:
            ball_speed_y = -ball_speed_y
        if (
            paddle_y <= ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT
            and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH
        ):
            ball_speed_y = -ball_speed_y
            score += 1
        if ball_y > HEIGHT:
            print("Game Over!")
            if restart_game(screen, WIDTH, HEIGHT, BLACK, WHITE):
                main()
            else:
                running = False
        pygame.draw.rect(screen, DEEP_BLUE, (0, 0, WALL_THICKNESS, HEIGHT))  
        pygame.draw.rect(screen, DEEP_BLUE, (WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT))  
        pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT), border_radius=PADDLE_RADIUS)
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()
def restart_game(screen, width, height, background_color, text_color):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over!", True, text_color)
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
    screen.fill(background_color)
    screen.blit(text, text_rect)
    restart_text = font.render("Press R to Restart", True, text_color)
    restart_rect = restart_text.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
main()