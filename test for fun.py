import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Dino Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# player
player_x = 100
player_y = 500
player_size = 40
y_speed = 0
gravity = 0.6
jump_strength = -12
on_ground = True

# ground
ground_y = 540

# obstacle
obstacle_x = WIDTH
obstacle_y = 500
obstacle_width = 30
obstacle_height = 40
obstacle_speed = 12

score = 0
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # reset game
                player_y = 500
                y_speed = 0
                on_ground = True
                obstacle_x = WIDTH
                score = 0
                game_over = False

            if not game_over and event.key == pygame.K_SPACE and on_ground:
                y_speed = jump_strength
                on_ground = False

    if not game_over:
        # gravity
        y_speed += gravity
        player_y += y_speed

        # stop at ground
        if player_y >= 500:
            player_y = 500
            y_speed = 0
            on_ground = True

        # move obstacle
        obstacle_x -= obstacle_speed

        # bring obstacle back
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH + random.randint(0, 200)
            score += 1

        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

        if player_rect.colliderect(obstacle_rect):
            game_over = True

    # draw background
    screen.fill((255, 255, 255))

    # draw ground
    pygame.draw.line(screen, (0, 0, 0), (0, ground_y), (WIDTH, ground_y), 3)

    # draw player
    pygame.draw.rect(screen, (50, 50, 50), (player_x, player_y, player_size, player_size))

    # draw obstacle
    pygame.draw.rect(screen, (0, 150, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # draw score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    if game_over:
        over_text = font.render("Game Over! Press R to restart", True, (200, 0, 0))
        screen.blit(over_text, (200, 200))

    pygame.display.update()
    clock.tick(60)

pygame.quit()