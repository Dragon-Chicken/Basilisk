import pygame
import main

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('game')

font = pygame.font.Font('Assets/Pixel-type.ttf', 15)

surfs = []

# update


def key_down(key):
    key = "pygame." + key
    keys = pygame.key.get_pressed()
    if keys[eval(key)]:
        return True

# draw


def import_image(image, name):
    global surfs
    surfs.append([name, pygame.image.load(image).convert_alpha()])


def draw(object_name, x, y):
    x = int(x)
    y = int(y)
    global surfs
    for image in surfs:
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
