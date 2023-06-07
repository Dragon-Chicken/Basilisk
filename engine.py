# Basilisk Engine
# Version: 1.1

import sys
import pygame
import main as main

pygame.init()
display = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("Engine requirements/Basilisk.png"))
screen = pygame.Surface((64, 64))


font = pygame.font.Font("Engine stuff/Pixel-type.ttf", 15)

images = []
SFXs = []

mouse_scroll = 0

# sfx


def import_sfx(sfx, sfx_name):
    global SFXs
    sfx_name = sfx_name.lower()
    SFXs.append([sfx_name, pygame.mixer.Sound(sfx)])


def play_sfx(sfx_name):
    global SFXs
    sfx_name = sfx_name.lower()
    for sfx in SFXs:
        if sfx[0] == sfx_name:
            sfx[1].play()

# update


def key_down(key):
    key = "pygame." + key
    keys = pygame.key.get_pressed()
    if keys[eval(key)]:
        return True


def movement(x, y, movement_speed):
    if key_down("K_w") or key_down("K_UP"):
        y -= movement_speed
    if key_down("K_s") or key_down("K_DOWN"):
        y += movement_speed
    if key_down("K_a") or key_down("K_LEFT"):
        x -= movement_speed
    if key_down("K_d") or key_down("K_RIGHT"):
        x += movement_speed

    return x, y


def mouse_clicks(mouse_button):
    left, middle, right = pygame.mouse.get_pressed()
    if mouse_button == "left" or mouse_button == "l" and left:
        return True
    elif mouse_button == "middle" or mouse_button == "m" and middle:
        return True
    elif mouse_button == "right" or mouse_button == "r" and right:
        return True
    elif mouse_button == "all":
        return left, middle, right


def mouse_pos():
    x, y = pygame.mouse.get_pos()
    return int(x/10), int(y/10)


# draw


def tile_map(tiles):
    if tiles is None:
        tiles = []
    i = 0
    for y in range(0, 8):
        for x in range(0, 8):
            draw(str(tiles[i]), x*8, y*8)
            i += 1


def image_import(image, image_name):
    global images
    object_name = image_name.lower()
    images.append([object_name, pygame.image.load(image).convert_alpha()])


def draw(object_name, x, y):
    global images
    object_name = object_name.lower()
    for image in images:
        if image[0] == object_name:
            surf = image[1]
            rect = surf.get_rect(topleft=(x, y))
            screen.blit(surf, rect)


def draw_rect(tx, ty, bx, by, colour=(255, 255, 255)):
    draw_line(tx, ty, by, ty, colour)
    draw_line(bx, ty, bx, by, colour)
    draw_line(bx, by, tx, by, colour)
    draw_line(tx, by, tx, ty, colour)


def draw_rect_filled(tx, ty, bx, by, colour=(255, 255, 255)):
    bx -= tx
    by -= ty
    pygame.draw.rect(screen, colour, (tx, ty, bx, by))


def draw_line(x1, y1, x2, y2, colour=(255, 255, 255)):
    pygame.draw.line(screen, colour, (x1, y1), (x2, y2), 1)


def text(text_to_display, x, y, colour=(255, 255, 255)):
    surf = font.render(f"{text_to_display}", False, colour)
    rect = surf.get_rect(topleft=(x, y))
    screen.blit(surf, rect)


main.init()

clock = pygame.time.Clock()

z = 0

while True:

    screen = pygame.transform.scale(screen, (64, 64))
    screen.fill((0, 0, 0))

    dt = clock.tick(10000) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEWHEEL:
            mouse_scroll = event.y

    if z > 0.034:
        print("***********************************\n"
              "WARNING RUNNING AT LESS THAN 30 FPS\n"
              "***********************************")

    if z >= 0.033:
        main.update()
        main.update()
        z = 0
    elif z >= 0.016:
        main.update()
        z = 0
    else:
        z += 1 * dt

    main.draw()

    screen = pygame.transform.scale(screen, (640, 640))
    display.blit(screen, (0, 0))
    pygame.display.update()
