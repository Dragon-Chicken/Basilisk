import pygame
import main

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('game')

font = pygame.font.Font('Assets/Pixel-type.ttf', 15)

images = []
SFXs = []

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

# draw


def import_image(image, object_name):
    global images
    object_name = object_name.lower()
    images.append([object_name, pygame.image.load(image).convert_alpha()])


def draw(object_name, x, y):
    x = int(x)
    y = int(y)
    global images
    object_name = object_name.lower()
    for image in images:
        if image[0] == object_name:
            surf = image[1]
            surf = pygame.transform.scale(surf, (surf.get_width()*10, surf.get_height()*10))
            rect = surf.get_rect(topleft=(x*10, y*10))
            screen.blit(surf, rect)


def text(text_to_display, x, y, colour=(255, 255, 255)):
    x = int(x)
    y = int(y)
    surf = font.render(f'{text_to_display}', False, colour)
    surf = pygame.transform.scale_by(surf, 6)
    rect = surf.get_rect(topleft=(x * 10, y * 10))
    screen.blit(surf, rect)


clock = pygame.time.Clock()

main.init_engine()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    main.update()
    main.draw()
    pygame.display.update()
    clock.tick(60)
