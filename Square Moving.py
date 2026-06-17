import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Target")

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

x, y = 400, 300
object_size = 50
speed = 10
points = 0
running = True

s1 = pygame.mixer.Sound("Mario.mp3")

x1 = random.randint(0, WIDTH - object_size)
y1 = random.randint(0, HEIGHT - object_size)

def draw_score(points):
    text = font.render("Score: " + str(points), True, (255, 255, 255))
    screen.blit(text, (20, 20))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += speed

    x %= WIDTH
    y %= HEIGHT

    # Create rectangles every frame
    player = pygame.Rect(x, y, object_size, object_size)
    target = pygame.Rect(x1, y1, object_size, object_size)

    if player.colliderect(target):
        points += 1
        s1.play()
        x1 = random.randint(0, WIDTH - object_size)
        y1 = random.randint(0, HEIGHT - object_size)

    screen.fill((159, 226, 191))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), target)
    draw_score(points)

    pygame.display.update()
    clock.tick(60)

pygame.quit()