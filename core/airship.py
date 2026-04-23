import pygame
from settings import GAME_SPEED, img

class Airship(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(img("assets/images/airplane.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = GAME_SPEED