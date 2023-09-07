#engine
import pygame
import sys

class engine_:
    
    def __init__(self) -> None:
        pygame.init()
        self.display = pygame.display.set_mode((640, 640))
        pygame.display.set_caption('game')
        pygame.display.set_icon(pygame.image.load("Engine requirements/Basilisk.png"))
        self.screen = pygame.Surface((64, 64))
        self.font = pygame.font.Font("Engine requirements/Pixel-type.ttf", 15)
        self.images = []
        self.SFXs = []
        self.mouse_scroll = 0

    def pass_down(self, initialize, draw_, update):
        self.initialize = initialize
        self.draw_ = draw_
        self.update = update

    def import_sfx(self, sfx, sfx_name):
        self.sfx_name = sfx_name.lower()
        self.SFXs.append([sfx_name, pygame.mixer.Sound(sfx)]) 

    def play_sfx(self, sfx_name):
        self.sfx_name = sfx_name.lower()
        for sfx in self.SFXs:
            if sfx[0] == self.sfx_name:
                sfx[1].play()

    def key_down(self, key) -> bool:
        #self.key = "pygame." + key
        #self.keys = pygame.key.get_pressed()
        #if self.keys[eval(key)]:
            #return True
        key = getattr(pygame, key)  # Get the Pygame key constant
        self.keys = pygame.key.get_pressed()
        if self.keys[key]:
            return True

    def movement(self, x, y, movement_speed) -> int:
        if self.key_down("K_w") or self.key_down("K_UP"):
            y -= movement_speed
        if self.key_down("K_s") or self.key_down("K_DOWN"):
            y += movement_speed
        if self.key_down("K_a") or self.key_down("K_LEFT"):
            x -= movement_speed
        if self.key_down("K_d") or self.key_down("K_RIGHT"):
            x += movement_speed

        return x, y

    def mouse_clicks(self, mouse_button):
        self.left, self.middle, self.right = pygame.mouse.get_pressed()
        if mouse_button == "left" or mouse_button == "l" and self.left:
            return True
        elif mouse_button == "middle" or mouse_button == "m" and self.middle:
            return True
        elif mouse_button == "right" or mouse_button == "r" and self.right:
            return True
        elif mouse_button == "all":
            return self.left, self.middle, self.right

    def mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return int(x / 10), int(y / 10)

    def tile_map(self, tiles):
        if tiles is None:
            tiles = []
        i = 0
        for y in range(0, 8):
            for x in range(0, 8):
                self.draw(str(tiles[i]), x * 8, y * 8)
                i += 1

    def image_import(self, image, image_name):
        self.object_name = image_name.lower()
        self.images.append([self.object_name, pygame.image.load(image).convert_alpha()])

    def draw(self, object_name, x, y):
        object_name = object_name.lower()
        for image in self.images:
            if image[0] == object_name:
                surf = image[1]
                rect = surf.get_rect(topleft=(x, y))
                self.screen.blit(surf, rect)

    def draw_rect(self, tx, ty, bx, by, colour=(255, 255, 255)):
        self.draw_line(tx, ty, by, ty, colour)
        self.draw_line(bx, ty, bx, by, colour)
        self.draw_line(bx, by, tx, by, colour)
        self.draw_line(tx, by, tx, ty, colour)

    def draw_rect_filled(self, tx, ty, bx, by, colour=(255, 255, 255)):
        bx -= tx
        by -= ty
        pygame.draw.rect(self.screen, colour, (tx, ty, bx, by))

    def draw_line(self, x1, y1, x2, y2, colour=(255, 255, 255)):
        pygame.draw.line(self.screen, colour, (x1, y1), (x2, y2), 1)

    def text(self, text_to_display, x, y, colour=(255, 255, 255)):
        surf = self.font.render(f"{text_to_display}", False, colour)
        rect = surf.get_rect(topleft=(x, y))
        self.screen.blit(surf, rect)

    def run(self):
        self.clock = pygame.time.Clock()
        self.initialize()
        self.z = 0
        self.screen.fill((0, 0, 0))
        self.screen = pygame.transform.scale(self.screen, (64, 64))
        
        while True:
            dt = self.clock.tick(10000) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEWHEEL:
                    self.mouse_scroll = event.y

            if self.z > 0.034:
                print("***********************************\n"
                      "WARNING RUNNING AT LESS THAN 30 FPS\n"
                      "***********************************")

            if self.z >= 0.033:
                self.update()
                self.update()
                self.z = 0
            elif self.z >= 0.016:
                self.update()
                self.z = 0
            else:
                self.z += 1 * dt

            self.draw_()

            self.screen = pygame.transform.scale(self.screen, (640, 640))
            self.display.blit(self.screen, (0, 0))
            pygame.display.update()
