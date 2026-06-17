import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Clicker - Playable")

background = pygame.image.load("res/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

obj = pygame.image.load("res/maxground.png").convert_alpha()
obj = pygame.transform.scale(obj,(100, 100))

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

circle_x = 400
circle_y = 300
circle_radius = 50
circle_color = (0, 120, 255)
score = 0


def draw_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)


def draw_score(points):
    text = font.render("Score: " + str(points), True, (255, 255, 255))
    screen.blit(text, (20, 20))


def is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, radius):
    dx = mouse_x - circle_x
    dy = mouse_y - circle_y
    return dx * dx + dy * dy <= radius * radius


def get_next_circle_position(radius):
    new_x = random.randint(radius, WIDTH - radius)
    new_y = random.randint(radius, HEIGHT - radius)
    return new_x, new_y


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, circle_radius):
                score = score + 1
                circle_radius = circle_radius - 3
                circle_color = get_random_color()
                circle_x, circle_y = get_next_circle_position(circle_radius)
            else:
                score = score - 1

    if circle_radius < 10:
        circle_radius = 50

    screen.blit(background, (0, 0))
    screen.blit(obj, (circle_x - circle_radius, circle_y - circle_radius))
    draw_score(score)
    pygame.display.update()
    clock.tick(60)

pygame.quit()