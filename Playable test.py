import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Clicker - Playable")

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

circle_x = 400
circle_y = 300
circle_radius = 50
circle_color = (0, 120, 255)
shape = "circle"
score = 0


def draw_shape(x, y, radius, color, shape):
    if shape == "circle":
        pygame.draw.circle(screen, color, (x, y), radius)

    elif shape == "square":
        pygame.draw.rect(screen, color, (x - radius, y - radius, radius * 2, radius * 2))

    elif shape == "triangle":
        p1 = (x, y - radius)
        p2 = (x - radius, y + radius)
        p3 = (x + radius, y + radius)
        pygame.draw.polygon(screen, color, [p1, p2, p3])


def draw_score(points):
    text = font.render("Score: " + str(points), True, (255, 255, 255))
    screen.blit(text, (20, 20))


def is_inside_shape(mouse_x, mouse_y, x, y, radius, shape):
    if shape == "circle":
        dx = mouse_x - x
        dy = mouse_y - y
        return dx * dx + dy * dy <= radius * radius

    elif shape == "square":
        return x - radius <= mouse_x <= x + radius and y - radius <= mouse_y <= y + radius

    elif shape == "triangle":
        return x - radius <= mouse_x <= x + radius and y - radius <= mouse_y <= y + radius


def get_next_position(radius):
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

            if is_inside_shape(mouse_x, mouse_y, circle_x, circle_y, circle_radius, shape):
                score = score + 1
                circle_radius = circle_radius - 3
                circle_color = get_random_color()
                shape = random.choice(["circle", "square", "triangle"])
                circle_x, circle_y = get_next_position(circle_radius)
            else:
                score = score - 1

    if circle_radius < 10:
        circle_radius = 50

    screen.fill((30, 30, 30))
    draw_shape(circle_x, circle_y, circle_radius, circle_color, shape)
    draw_score(score)
    pygame.display.update()
    clock.tick(60)

pygame.quit()