import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
PADDLE_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Pong")
font = pygame.font.Font(None, 36)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
left_score, right_score = 0, 0
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED
    ball.x += ball_dx
    ball.y += ball_dy
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx
    if ball.left <= 0:
        right_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
    if ball.right >= WIDTH:
        left_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx, ball_dy = -BALL_SPEED_X, BALL_SPEED_Y
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
