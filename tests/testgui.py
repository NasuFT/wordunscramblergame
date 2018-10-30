import os

import pygame


GAME_TITLE = "Autistic Induced Word Unscrambler"
GAME_WIDTH = 1280
GAME_HEIGHT = 720
GAME_FPS = 60
GAME_ASSETS_DIR = "Assets"


pygame.init()

def load_image(file, dest = (0, 0)):
    rect = pygame.image.load(os.path.join(GAME_ASSETS_DIR, file))

    if dest == 'center':
        dest = center(rect)

    game.screen.blit(rect, dest)

    return rect

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

    load_image('bg.jpg')

    load_image('DlhwzN7WwAEZlFD.jpg', 'center')

    pygame.display.flip()
    game.clock.tick(GAME_FPS)



