import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Starter")

clock = pygame.time.Clock()
FPS = 60
high_scores = {"easy": 0, "hard": 0, "insane": 0}

WHITE = (255, 255, 225)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

GROUND_Y = 380

background = pygame.image.load("res/Selection.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

credits_bg = pygame.image.load("res/Credits.png")
credits_bg = pygame.transform.scale(credits_bg, (WIDTH, HEIGHT))

easy_bg = pygame.image.load("res/EasyBackground.png")
easy_bg = pygame.transform.scale(easy_bg, (WIDTH, HEIGHT))

hard_bg = pygame.image.load("res/HardBackground.png")
hard_bg = pygame.transform.scale(hard_bg, (WIDTH, HEIGHT))

insane_bg = pygame.image.load("res/InsaneBackground.png")
insane_bg = pygame.transform.scale(insane_bg, (WIDTH, HEIGHT))

pygame.mixer.init()
pygame.mixer.music.load("res/Menu.mp3")

easy_music = "res/easy_music.mp3"
hard_music = "res/hard_music.mp3"
insane_music = "res/insane_music.mp3"

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 28)


def draw_text(text, x, y, color=BLACK, big=True):
    used_font = font if big else small_font
    img = used_font.render(text, True, color)
    screen.blit(img, (x, y))


def main_menu():
    while True:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("res/Menu.mp3")
            pygame.mixer.music.play(-1)

        screen.blit(background, (0, 0))

        draw_text("DINO GAME", 310, 80)
        draw_text("1 - Easy Game", 300, 130, big=False)
        draw_text("2 - Hard Game", 300, 170, big=False)
        draw_text("3 - Insane Game", 300, 210, big=False)
        draw_text("4 - Credits", 300, 250, big=False)
        draw_text("ESC - Quit", 300, 290, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer.music.stop()
                    game_loop("easy")
                elif event.key == pygame.K_2:
                    pygame.mixer.music.stop()
                    game_loop("hard")
                elif event.key == pygame.K_3:
                    pygame.mixer.music.stop()
                    game_loop("insane")
                elif event.key == pygame.K_4:
                    credits()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


def credits():
    while True:
        screen.blit(credits_bg, (0, 0))

        draw_text("Credits", 50, 80, color=WHITE)
        draw_text("Created by Charlie Yin", 50, 150, color=WHITE, big=False)
        draw_text("Press BACKSPACE to return", 50, 190, color=WHITE, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return


def game_loop(mode):
    global high_scores
    if mode == "easy":
        pygame.mixer.music.load(easy_music)
        pygame.mixer.music.play(-1)
    elif mode == "hard":
        pygame.mixer.music.load(hard_music)
        pygame.mixer.music.play(-1)
    elif mode == "insane":
        pygame.mixer.music.load(insane_music)
        pygame.mixer.music.play(-1)

    dino_x = 100
    dino_y = GROUND_Y - 50
    dino_width = 40
    dino_height = 50

    velocity_y = 0
    gravity = 1
    jump_strength = -18
    on_ground = True

    obstacle_width = 20
    obstacle_height = 40
    obstacle_x = WIDTH
    obstacle_y = GROUND_Y - obstacle_height

    if mode == "easy":
        obstacle_speed = 5
    elif mode == "hard":
        obstacle_speed = 7
    else:
        obstacle_speed = 11

    score = 0
    frame_count = 0
    running = True
    game_over = False

    while running:
        clock.tick(FPS)
        if mode == "easy":
            screen.blit(easy_bg, (0, 0))
        elif mode == "hard":
            screen.blit(hard_bg, (0, 0))
        elif mode == "insane":
            screen.blit(insane_bg, (0, 0))
        else:
            screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground and not game_over:
                    velocity_y = jump_strength
                    on_ground = False

                if event.key == pygame.K_r and game_over:
                    return game_loop(mode)

                if event.key == pygame.K_BACKSPACE:
                    pygame.mixer.music.stop()
                    return

        if not game_over:
            dino_y += velocity_y
            velocity_y += gravity

            if dino_y >= GROUND_Y - dino_height:
                dino_y = GROUND_Y - dino_height
                velocity_y = 0
                on_ground = True

            frame_count += 1
            if frame_count % 6 == 0:
                score += 1
            if frame_count % 600 == 0:
                obstacle_speed += 1

            obstacle_x -= obstacle_speed

            if obstacle_x < -obstacle_width:
                obstacle_x = WIDTH + random.randint(100, 400)

            dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

            if dino_rect.colliderect(obstacle_rect):
                game_over = True
                pygame.mixer.music.stop()
                if score > high_scores[mode]:
                    high_scores[mode] = score

        pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))

        pygame.draw.rect(screen, GRAY, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        if mode == "insane":
            draw_text("Score: " + str(score), 20, 20, color=WHITE, big=False)
            draw_text("Mode: " + mode, 20, 50, color=WHITE, big=False)
            draw_text("High Score: " + str(high_scores[mode]), 560, 20, color=WHITE, big=False)
        else:
            draw_text("Score: " + str(score), 20, 20, big=False)
            draw_text("Mode: " + mode, 20, 50, big=False)
            draw_text("High Score: " + str(high_scores[mode]), 560, 20, big=False)

        if game_over:
            draw_text("GAME OVER", 310, 140)
            draw_text("Press R to restart", 300, 200, big=False)
            draw_text("Press BACKSPACE for menu", 270, 240, big=False)

        pygame.display.update()


main_menu()