"""
Dino Jump - minimal base
A dino jumps over a cactus. Loads YOUR images and sounds.

It runs even if the asset files are missing (you'll see plain
colored boxes instead), so you can test the mechanic first and
drop your art in afterwards.

Controls:  SPACE / UP = jump,  R = restart,  ESC = quit
"""

import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump")
clock = pygame.time.Clock()
FPS = 60
GROUND_Y = 320

# ==========================================================================
# YOUR ASSETS  -  put these files in the SAME folder as this script,
# then change the names below to match your files.
# ==========================================================================
DINO_IMG   = "dino.png"
CACTUS_IMG = "cactus.png"
BG_IMG     = "background.png"   # optional - delete the file for a plain sky
JUMP_SND   = "jump.wav"
HIT_SND    = "hit.wav"

# On-screen size each image is drawn at (width, height).
# Match these to your image's shape so it doesn't look stretched.
DINO_SIZE   = (60, 62)
CACTUS_SIZE = (40, 60)
# ==========================================================================


def load_image(name, size, fallback_color):
    """Load + scale an image; if the file is missing, return a colored box."""
    try:
        img = pygame.image.load(name).convert_alpha()
        return pygame.transform.smoothscale(img, size)
    except Exception:
        box = pygame.Surface(size, pygame.SRCALPHA)
        box.fill(fallback_color)
        return box


def load_sound(name):
    try:
        return pygame.mixer.Sound(name)
    except Exception:
        return None


def play(snd):
    if snd:
        snd.play()


# Load everything once
dino_img   = load_image(DINO_IMG,   DINO_SIZE,   (80, 210, 190))   # teal box fallback
cactus_img = load_image(CACTUS_IMG, CACTUS_SIZE, (70, 150, 80))    # green box fallback
jump_snd   = load_sound(JUMP_SND)
hit_snd    = load_sound(HIT_SND)

try:
    background = pygame.transform.smoothscale(
        pygame.image.load(BG_IMG).convert(), (WIDTH, HEIGHT))
except Exception:
    background = None

font = pygame.font.SysFont(None, 36)


def game():
    """One playthrough. Returns True to restart, False to quit."""
    dino_x = 90
    dino_y = GROUND_Y - DINO_SIZE[1]
    vel_y = 0
    gravity = 1
    jump_strength = -17
    on_ground = True

    cactus_x = WIDTH + 200
    cactus_y = GROUND_Y - CACTUS_SIZE[1]
    speed = 7

    score = 0
    game_over = False

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP) and on_ground and not game_over:
                    vel_y = jump_strength
                    on_ground = False
                    play(jump_snd)
                if event.key == pygame.K_r and game_over:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

        if not game_over:
            # --- dino jump physics ---
            vel_y += gravity
            dino_y += vel_y
            if dino_y >= GROUND_Y - DINO_SIZE[1]:     # landed
                dino_y = GROUND_Y - DINO_SIZE[1]
                vel_y = 0
                on_ground = True

            # --- move the cactus, respawn when it goes off-screen ---
            cactus_x -= speed
            if cactus_x < -CACTUS_SIZE[0]:
                cactus_x = WIDTH + random.randint(150, 450)
                score += 1
                speed += 0.2                          # gets slightly faster

            # --- collision (boxes shrunk a little so it feels fair) ---
            dino_rect = pygame.Rect(dino_x, dino_y, *DINO_SIZE).inflate(-14, -10)
            cactus_rect = pygame.Rect(cactus_x, cactus_y, *CACTUS_SIZE).inflate(-8, -6)
            if dino_rect.colliderect(cactus_rect):
                game_over = True
                play(hit_snd)

        # --- draw ---
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((34, 30, 50))
            pygame.draw.line(screen, (200, 200, 210), (0, GROUND_Y), (WIDTH, GROUND_Y), 3)

        screen.blit(cactus_img, (cactus_x, cactus_y))
        screen.blit(dino_img, (dino_x, dino_y))

        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (20, 20))
        if game_over:
            msg = font.render("GAME OVER  -  press R to restart", True, (255, 255, 255))
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 150))

        pygame.display.flip()


def main():
    again = True
    while again:
        again = game()
    pygame.quit()


if __name__ == "__main__":
    main()