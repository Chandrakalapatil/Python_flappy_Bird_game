import pygame
import random

pygame.init()

# Window dimensions
WIDTH = 400
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Bird dimensions
BIRD_WIDTH = 50
BIRD_HEIGHT = 40

# Pipe dimensions
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(100, 400)
PIPE_GAP = 150

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

def draw_bird(x, y):
    pygame.draw.rect(window, BLUE, (x, y, BIRD_WIDTH, BIRD_HEIGHT))

def draw_pipe(x, height):
    pygame.draw.rect(window, GREEN, (x, 0, PIPE_WIDTH, height))
    pygame.draw.rect(window, GREEN, (x, height + PIPE_GAP, PIPE_WIDTH, HEIGHT))

def check_collision(x, y, pipes):
    if y < 0 or y + BIRD_HEIGHT > HEIGHT:
        return True
    for pipe in pipes:
        if pygame.Rect(x, y, BIRD_WIDTH, BIRD_HEIGHT).colliderect(pygame.Rect(pipe[0], 0, PIPE_WIDTH, pipe[1])) \
                or pygame.Rect(x, y, BIRD_WIDTH, BIRD_HEIGHT).colliderect(
            pygame.Rect(pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP)):
            return True
    return False

x = 50
y = HEIGHT // 2
y_speed = 0

pipes = []

game_over = False

score = 0
font = pygame.font.Font(None, 36)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            y_speed = -7

    y += y_speed
    y_speed += 0.2

    window.fill(WHITE)
    draw_bird(x, y)

    for pipe in pipes:
        pipe[0] -= 3
        draw_pipe(pipe[0], pipe[1])
        if pipe[0] == x:
            score += 1
        if pipe[0] + PIPE_WIDTH < 0:
            pipes.remove(pipe)

    if len(pipes) < 2:
        pipe_height = random.randint(100, 400)
        pipes.append([WIDTH, pipe_height])

    if check_collision(x, y, pipes):
        game_over = True

    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
