import pygame
import random

pygame.init()

# window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch The Ball")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Paddle settings
paddle_width = 120
paddle_height = 15
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 48
paddle_speed = 7

# Ball settings
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 50
ball_speed_x = 4
ball_speed_y = 5

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Game loop
running = True
game_over = False

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        # Move paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x + paddle_width < WIDTH:
            paddle_x += paddle_speed
            
        # Move ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Ball bouncing off walls
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_speed_x *= -1
        if ball_y - ball_radius <= 0:
            ball_speed_y *= -1
            
        # Ball hits paddle 
        if (paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height and
                paddle_x <= ball_x <= paddle_x + paddle_width):
            ball_speed_y *= -1
            ball_speed_x = random.randint(-6, 6)
            ball_y = paddle_y - ball_radius
            score += 1
            
        # Ball falls past paddle
        if ball_y - ball_radius > HEIGHT:
            game_over = True
                
    # Draw everything
    screen.fill(BLACK)
            
    if not game_over:
        pygame.draw.rect(screen, BLUE,
            (paddle_x, paddle_y, paddle_width, paddle_height))
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
    else:
        game_over_text = font.render(
            f"Game Overrrr!!! Final Score: {score}", True, WHITE)
        restart_text = font.render(
            "Close the window to exit pleaase.", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
        screen.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 30))
                
    pygame.display.flip()

pygame.quit()    
        