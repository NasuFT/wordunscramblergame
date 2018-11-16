import os

import pygame


GAME_TITLE = "Autistic Induced Word Unscrambler"
GAME_WIDTH = 1280
GAME_HEIGHT = 720
GAME_ASSETS_DIR = "Assets"
GAME_FPS = 30


pygame.init()

def load_image(file, dest = (0, 0)):
    rect = pygame.image.load(os.path.join(GAME_ASSETS_DIR, file)).convert_alpha()

    if dest == 'center':
        dest = center(rect)

    game.screen.blit(rect, dest)

    return rect

def scale(rect, size):
    rect_x = rect.get_rect().x
    rect_y = rect.get_rect().y

    img = pygame.transform.scale(rect, size)
    game.screen.blit(img, (rect_x, rect_y))

    return img

def center(rect):
    width = GAME_WIDTH
    height = GAME_HEIGHT
    rect_width = rect.get_rect().width
    rect_height = rect.get_rect().height

    center_x = (width / 2) - (rect_width / 2)
    center_y = (height / 2) - (rect_height / 2)

    return (center_x, center_y)


class Settings:
    """ Initializing GUI Settings
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(GAME_TITLE)


game = Settings()
width = GAME_WIDTH
height = GAME_HEIGHT
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    scale(load_image('bg.jpg'), (width, height))

    load_image('DlhwzN7WwAEZlFD.jpg', 'center')

    pygame.display.update()
    game.clock.tick(GAME_FPS)



